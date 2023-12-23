#!/usr/bin/python3

"""
Simulation Tester
This module invokes the main.py module and runs the meta simulation.
"""
import sys
import math
import subprocess
from simulator import Simulator
from simulations import simulation4


def send_simulation_data(process, data):
    process.stdin.write(f"{data['total_bikes']}\n")
    process.stdin.write(f"{data['required']}\n")
    for lane in data["lanes"]:
        process.stdin.write(f"{lane}\n")
    process.stdin.write(f"{data['speed']}\n")
    for bike in data["bikes"]:
        process.stdin.write(f"{bike}\n")


def run_simulation(commands, data):
    print(f"[ {data['name']} ]\n")

    sim = Simulator(data)
    sim.render(0, "")

    for i in range(len(commands)):
        command = commands[i]
        game_over, success_bikes = sim.process(command)
        sim.render(i + 1, command)
        if game_over:
            print("GAME OVER")
            print(f"Bikes accross bridge: {success_bikes}")
            if success_bikes < int(data["required"]):
                print(f"Your mission was not successful.\n")
            else:
                print(f"Congratuations, your mission was successful!\n")
            break
    sim.reset()


def main():
    process = subprocess.Popen(
        ["python3", "./main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    simulation_data = simulation4()
    simulation_commands = simulation_data.commands
    for i in range(50 - len(simulation_commands)):
        simulation_commands.append("WAIT")

    # send_simulation_data(process, simulation_data)

    run_simulation(simulation_commands, simulation_data)

    # stdout, stderr = process.communicate()  # Read stdout and stderr

    # # Print the output
    # print(f"===Output:\n{stdout}\n")
    # print(f"===Debug:\n{stderr}\n")

    process.stdin.close()


if __name__ == "__main__":
    main()
