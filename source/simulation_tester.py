#!/usr/bin/python3

"""
Simulation Tester
This module invokes the main.py module and runs one or more simulations.
"""
import os
import fcntl
import subprocess
from simulator import Simulator, SimulatorState
from simulations import simulation0, simulation1, simulation2, simulation3, simulation4, simulation5
from bike_ai import Bike_AI


def send_simulation_initial_data(process, data):
    process.stdin.write(f"{data['total_bikes']}\n")
    process.stdin.write(f"{data['required']}\n")
    for lane in data["lanes"]:
        process.stdin.write(f"{lane}\n")
    process.stdin.flush()


def send_simulation_data(process, state):
    process.stdin.write(f"{state.speed}\n")
    for bike in state.bikes:
        x, y, a = bike
        process.stdin.write(f"{x} {y} {a}\n")
    process.stdin.flush()


def run_simulation(commands, data):
    print(f"[{data['name'].upper()}]\n")

    sim = Simulator(data)
    sim.render(-1, "")

    for i in range(len(commands)):
        command = commands[i]
        game_over, success_bikes = sim.process(command)
        if not game_over:
            sim.render(i + 1, command)
        else:
            print("GAME OVER")
            print(f"Bikes accross bridge: {success_bikes}")
            if success_bikes < int(data["required"]):
                print(f"Your mission was not successful.\n")
            else:
                print(f"Congratuations, your mission was successful!\n")
            break
    sim.reset()

COMMAND_TO_INT = {
    "": 0,
    "SPEED": 1,
    "WAIT": 2,
    "JUMP": 3,
    "UP": 4,
    "DOWN": 5,
    "SLOW": 6,
}

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

    data = simulation0()
    sim = Simulator(data)

    bike_ai = Bike_AI(sim, data)

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
