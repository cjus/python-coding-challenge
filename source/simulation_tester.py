#!/usr/bin/python3

"""
Simulation Tester
This module invokes the main.py module and runs one or more simulations.
"""
import os
import fcntl
import subprocess

from simulator import Simulator, SimulatorState, SimulatorCommand
from simulations import SIM_TESTS
from bike_ai import Bike_AI

COMMAND_TO_INT = {
    "": 0,
    "SPEED": SimulatorCommand.COMMAND_SPEED,
    "WAIT": SimulatorCommand.COMMAND_WAIT,
    "JUMP": SimulatorCommand.COMMAND_JUMP,
    "UP": SimulatorCommand.COMMAND_UP,
    "DOWN": SimulatorCommand.COMMAND_DOWN,
    "SLOW": SimulatorCommand.COMMAND_SLOW,
}


def num_with_commas(num):
    return f"{num:,}".replace(".", ",")


def send_simulation_initial_data(process, data):
    process.stdin.write(f"{data['total_bikes']}\n")
    process.stdin.write(f"{data['required']}\n")
    for lane in data["lanes"]:
        process.stdin.write(f"{lane}\n")
    process.stdin.flush()


def send_simulation_data(process, state, speed):
    process.stdin.write(f"{speed}\n")
    for bike in state.bikes:
        x, y, a = bike
        process.stdin.write(f"{x} {y} {a}\n")
    process.stdin.flush()


def output_steps(commands, data):
    sim = Simulator(data)

    state = SimulatorState(None)
    state.speed = data["speed"]
    state.remaining_bikes = data["remaining_bikes"]
    for bike in data["bikes"]:
        state.bikes.append(bike.copy())

    sim.render(state)

    for i in range(len(commands)):
        state = state.clone()
        state.command = COMMAND_TO_INT[commands[i]]
        print(f"Processing: {commands[i]}")
        state = sim.process(state)
        sim.render(state)
        if state.game_over:
            print("GAME OVER")
            print(f"Bikes accross bridge: {state.remaining_bikes}")
            if state.remaining_bikes < int(data["required"]):
                print(f"Your mission was not successful.\n")
            else:
                print(f"Congratuations, your mission was successful!\n")
            break


def run_internal_sim(sim, data):
    print(f"\nStarting Bike_AI on {sim.name}\n")
    bike_ai = Bike_AI(sim, use_graphviz=False, debug=True)
    step_data = {
        "speed": data["speed"],
        "remaining_bikes": data["total_bikes"],
        "bikes": data["bikes"],
    }
    step_data["speed"] = data["speed"]
    step_data["bikes"] = data["bikes"]
    # step_data["speed"] = 4
    # step_data["bikes"] = [
    #     [9, 0, 1],
    #     [9, 1, 1],
    #     [9, 2, 1],
    #     [9, 3, 1],
    # ]
    winning_line = bike_ai.process_move(step_data)

    print(f"\nBike_AI elapsed time: {round(bike_ai.get_elapsed_time(),2)} seconds.")
    print(
        f"Examined a total of {num_with_commas(bike_ai.node_id)} nodes out of a maximum possible {num_with_commas(bike_ai.get_maximum_nodes())} nodes by depth: {bike_ai.max_depth_reached}"
    )
    print(f"Winning line is: {bike_ai.get_winning_line()}\n")

    winning_line.pop()

    reset_data = data
    reset_data["remaining_bikes"] = data["total_bikes"]
    reset_data["bikes"] = step_data["bikes"]
    reset_data["speed"] = step_data["speed"]
    output_steps(winning_line, reset_data)


def run_external_sim(sim, data):
    process = subprocess.Popen(
        ["python3", "./main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # convert process stderr to non-blocking
    fd = process.stderr.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

    state = SimulatorState(None)
    state.remaining_bikes = sim.total_bikes
    for bike in data["bikes"]:
        state.bikes.append(bike.copy())
    current_speed = data["speed"]
    state.speed = current_speed
    send_simulation_initial_data(process, data)
    sim.render(state)

    while True:
        send_simulation_data(process, state, current_speed)

        command = process.stdout.readline().strip()
        if command != "":
            print(f"Command received: {command}")

        state.command = COMMAND_TO_INT[command]
        state = sim.process(state)
        current_speed = state.speed

        sim.render(state)

        if state.game_over or state.command == "":
            print("\nGAME OVER")
            print(f"Bikes accross bridge: {state.remaining_bikes}")
            if state.remaining_bikes < int(data["required"]):
                print(f"Your mission was not successful.\n")
            else:
                print(f"Congratuations, your mission was successful!\n")
            break

    print("Process output: ")
    while True:
        line = process.stderr.readline()
        if not line:
            break
        print(f"   {line.rstrip()}")

    try:
        for pipe in [process.stdin, process.stdout, process.stderr]:
            pipe.close()
    except:
        pass
    print("\n")


def main():
    data = SIM_TESTS.simulation12()
    sim = Simulator(data)

    run_internal_sim(sim, data)
    # run_external_sim(sim, data)


if __name__ == "__main__":
    main()
