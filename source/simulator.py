#!/usr/bin/python3

"""
Simulator
This module invokes the main.py module and runs the meta simulation.
"""
import sys
import math
import subprocess


def simulation1():
    return {
        "name": "Sim 1: One lonley hole",
        "total_bikes": "1",
        "required": "1",
        "speed": "0",
        "lanes": [
            "..................................",
            "..................................",
            "...........0......................",
            "..................................",
        ],
        "bikes": [
            "0 2 1",
        ],
    }


def simulation2():
    return {
        "name": "Sim 2",
        "total_bikes": "2",
        "required": "1",
        "speed": "0",
        "lanes": [
            "....0.............................",
            "................0.................",
            "......................00..........",
            "............0.....................",
        ],
        "bikes": [
            "0 0 1",
            "0 3 1",
        ],
    }


def simulation3():
    return {
        "name": "Sim 3",
        "total_bikes": "3",
        "required": "2",
        "speed": "0",
        "lanes": [
            "..................................",
            ".............0....................",
            "..................................",
            "...0..............................",
        ],
        "bikes": [
            "0 1 1",
            "0 2 1",
            "0 3 1",
        ],
    }


def simulation4():
    return {
        "name": "Sim 4: Jump into hole",
        "total_bikes": "1",
        "required": "1",
        "speed": "0",
        "lanes": [
            "...0..............................",
            "..................................",
            "..................................",
            "..................................",
        ],
        "bikes": [
            "0 0 1",
        ],
    }


def send_simulation_data(process, data):
    process.stdin.write(f"{data['total_bikes']}\n")
    process.stdin.write(f"{data['required']}\n")
    for lane in data["lanes"]:
        process.stdin.write(f"{lane}\n")
    process.stdin.write(f"{data['speed']}\n")
    for bike in data["bikes"]:
        process.stdin.write(f"{bike}\n")


def render_iteration(iteration, data, command):
    if iteration == 0:
        print(f"Initial State")
    else:
        print(f"Iteration: {iteration} | After: {command}")
    lanes = [
        list(data["lanes"][0]),
        list(data["lanes"][1]),
        list(data["lanes"][2]),
        list(data["lanes"][3]),
    ]
    max_iterations = len(lanes[0])
    for i in range(max_iterations):
        value = "{:02d}".format(i)
        print(value[0], end="")
    print()
    for i in range(max_iterations):
        value = "{:02d}".format(i)
        print(value[1], end="")
    print()
    for i in range(max_iterations):
        print("-", end="")
    print()

    bike_index = 1
    for bike in data["bikes"]:
        x, y, a = [int(j) for j in bike.split()]
        if a == 0 or a == 1:
            lanes[y][x] = f"{bike_index}"
        else:
            lanes[y][x] = "."
        bike_index = bike_index + 1

    for lane in lanes:
        for i in range(len(lane)):
            c = lane[i]
            if c == "0":
                c = "x"
            print(c, end="")
        print()

    print("\n")


def process_simulation_iteration(command, data):
    pass


def run_simulation(commands, data):
    print(
        f"[ {data['name']} ] ===============================================================\n"
    )
    render_iteration(0, data, "")

    last_command = ""
    speed = int(data["speed"])
    bike_data = []
    for bike in data["bikes"]:
        bike_data.append([int(j) for j in bike.split()])

    total_bikes = len(bike_data)
    required_bikes = int(data["required"])
    remaining_bikes = total_bikes
    success_bikes = 0

    lanes = [
        list(data["lanes"][0]),
        list(data["lanes"][1]),
        list(data["lanes"][2]),
        list(data["lanes"][3]),
    ]
    max_iterations = len(lanes[0])

    for i in range(len(commands)):
        command = commands[i]
        if remaining_bikes == 0:
            print("GAME OVER")
            print(f"Bikes accross bridge: {success_bikes}")
            if success_bikes < required_bikes:
                print(f"Your mission was not successful.\n")
            else:
                print(f"Congratuations, your mission was successful!\n")
            break
        if command == "SPEED":
            speed = speed + 1
            data["speed"] = str(speed)
        elif command == "SLOW":
            speed = speed - 1
            if speed < 0:
                speed = 0
            data["speed"] = str(speed)
        elif commands == "JUMP":
            pass
        elif command == "WAIT":
            pass
        elif command == "UP":
            first_active_bike = -1
            for b in range(len(bike_data)):
                if bike_data[b][2]:
                    first_active_bike = b
                    break
            if first_active_bike > -1:
                if bike_data[first_active_bike][1] > 0:
                    for b in range(len(bike_data)):
                        if bike_data[b][2]:
                            bike_data[b][1] = bike_data[b][1] - 1
        elif command == "DOWN":
            last_active_bike = -1
            for b in reversed(range(len(bike_data))):
                if bike_data[b][2]:
                    last_active_bike = b
                    break
            if last_active_bike > -1:
                if bike_data[last_active_bike][1] < len(lanes) - 1:
                    for b in range(len(bike_data)):
                        if bike_data[b][2]:
                            bike_data[b][1] = bike_data[b][1] + 1

        for b in range(len(bike_data)):
            x, y, a = bike_data[b]
            if a == 0:
                continue
            print(f"Path({b} {x}-{x+speed+1}): [", end="")
            for j in range(x, x + speed + 1):
                if j >= max_iterations:
                    break
                print(f"{lanes[y][j]}", end="")
                if lanes[y][j] == "0" and last_command != "JUMP":
                    remaining_bikes = remaining_bikes - 1
                    a = 0
                    x = j
                    break

            print("]")
            print(f"Speed: {speed}")
            if a != 0:
                x = x + speed
                if x >= max_iterations:
                    x = max_iterations - 1
                    success_bikes = success_bikes + 1
                    remaining_bikes = remaining_bikes - 1
            else:
                bike_data[b][2] = 0

            bike_data[b][0] = x
            data["bikes"][b] = f"{x} {y} {a}"
        last_command = command

        render_iteration(i + 1, data, commands[i])


process = subprocess.Popen(
    ["python3", "./main.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

# ["SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]
simulation_commands = [
    "SPEED",
    "JUMP",
    "WAIT",
    "WAIT",
    "WAIT",
    "WAIT",
    "WAIT",
]
for i in range(50 - len(simulation_commands)):
    simulation_commands.append("WAIT")

simulation_data = simulation4()
send_simulation_data(process, simulation_data)

run_simulation(simulation_commands, simulation_data)


# stdout, stderr = process.communicate()  # Read stdout and stderr

# # Print the output
# print(f"===Output:\n{stdout}\n")
# print(f"===Debug:\n{stderr}\n")

process.stdin.close()
