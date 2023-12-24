#!/usr/bin/python3

"""
Simulation Tester
This module invokes the main.py module and runs one or more simulations.
"""
import os
import fcntl
import subprocess
from simulator import Simulator
from simulations import simulation1, simulation2, simulation3, simulation4, simulation5


def send_simulation_initial_data(process, data):
    process.stdin.write(f"{data['total_bikes']}\n")
    process.stdin.write(f"{data['required']}\n")
    for lane in data["lanes"]:
        process.stdin.write(f"{lane}\n")
    process.stdin.flush()


def send_simulation_data(process, simulation):
    process.stdin.write(f"{simulation.speed}\n")
    for bike in simulation.bikes:
        process.stdin.write(f"{bike}\n")
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

    # simulation_data = simulation1()
    # simulation_commands = simulation_data["commands"]
    # for i in range(50 - len(simulation_commands)):
    #     simulation_commands.append("WAIT")
    # run_simulation(simulation_commands, simulation_data)

    data = simulation1()
    sim = Simulator(data)
    sim.render(-1, "")

    send_simulation_initial_data(process, data)

    i = 0
    while True:
        send_simulation_data(process, sim)
        # try:
        #     send_simulation_data(process, sim)
        # except:
        #     break

        command = process.stdout.readline().strip()
        if command != "":
            print(f"Command recieved: {command}")

        game_over, success_bikes = sim.process(command)
        sim.render(i + 1, command)
        if game_over or command == "":
            print("\nGAME OVER")
            print(f"Bikes accross bridge: {success_bikes}")
            if success_bikes < int(data["required"]):
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
        # the real code does filtering here
        print(f"   {line.rstrip()}")

    for pipe in [process.stdin, process.stdout, process.stderr]:
        try:
            pipe.close()
        except:
            pass
    print("\n")


if __name__ == "__main__":
    main()
