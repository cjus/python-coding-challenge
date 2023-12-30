#!/usr/bin/python3

"""
Simulation Tester
This module invokes the main.py module and runs one or more simulations.
"""
import os
import fcntl
import subprocess

from simulator import Simulator, SimulatorState, SimulatorCommand

from simulations import (
    simulation1,
    simulation2,
    simulation3,
    simulation4,
    simulation5,
    simulation6,
    simulation7,
    simulation8,
    simulation9, # Failed 
    simulation10,
    simulation11,
    simulation12, # Failed
)
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


def run_simulation(commands, data):
    print(f"[{data['name'].upper()}]\n")

    sim = Simulator(data)

    state = SimulatorState(None)
    state.remaining_bikes = sim.total_bikes
    state.speed = data["speed"]
    for bike in data["bikes"]:
        state.bikes.append(bike.copy())

    sim.render(state)

    for i in range(len(commands)):
        if i != 0:
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

def num_with_commas(num):
    return f'{num:,}'.replace('.',',')

def main():
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

    data = simulation9()

    # sim = Simulator(data)
    run_simulation(["", 'DOWN', 'SPEED', 'UP', 'JUMP', 'DOWN', 'SPEED', 'SPEED'], data)

    # print(f"\n\nStarting Bike_AI on {sim.name}\n")
    # bike_ai = Bike_AI(sim, data, False, True)
    # print(f"\n\nBike_AI elapsed time: {round(bike_ai.get_elapsed_time(),2)} seconds.")
    # print(f"Examined a total of {num_with_commas(bike_ai.node_id)} nodes out of a maximum possible {num_with_commas(bike_ai.get_maximum_nodes())} nodes by depth: {bike_ai.max_depth_reached}")
    # print(f"Winning line is: {bike_ai.get_winning_line()}\n")


    state = SimulatorState(None)
    state.remaining_bikes = sim.total_bikes

    for bike in data["bikes"]:
        state.bikes.append(bike.copy())

    simulation_states = []
    simulation_states.append(state)

    sim.render(state)

    send_simulation_initial_data(process, data)

    i = 1
    while True:
        send_simulation_data(process, state)

        command = process.stdout.readline().strip()
        if command != "":
            print(f"Command recieved: {command}")

        state.command = COMMAND_TO_INT[command]
        state = sim.process(state)

        sim.render(state)
        simulation_states.append(state)

        if state.game_over or state.command == "":
            print("\nGAME OVER")
            print(f"Bikes accross bridge: {state.remaining_bikes}")
            if state.remaining_bikes < int(data["required"]):
                print(f"Your mission was not successful.\n")
            else:
                print(f"Congratuations, your mission was successful!\n")
            break

        i = i + 1

    print("Process output: ")
    while True:
        line = process.stderr.readline()
        if not line:
            break
        print(f"   {line.rstrip()}")

    for pipe in [process.stdin, process.stdout, process.stderr]:
        try:
            pipe.close()
        except:
            pass

    # print("\nState Stack Output:\n")
    # for state in simulation_states:
    #     print(state)
    #     sim.render(state)
    #     print("==================================================\n")

    # sim.render(simulation_states[8])
    print("\n")


if __name__ == "__main__":
    main()
