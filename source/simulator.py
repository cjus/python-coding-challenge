"""
Simulator
This module invokes the main.py module and runs the meta simulation.
"""


class Simulator:
    """Simulator class. Encapsulates a running instance of a simulation"""

    """Possible commands ["SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]"""

    def __init__(self, simulation_data):
        """constructor"""
        self.name = simulation_data["name"]
        self.total_bikes = int(simulation_data["total_bikes"])
        self.remaining_bikes = self.total_bikes
        self.success_bikes = 0
        self.required = int(simulation_data["required"])
        self.speed = int(simulation_data["speed"])
        self.lanes = [
            list(simulation_data["lanes"][0]),
            list(simulation_data["lanes"][1]),
            list(simulation_data["lanes"][2]),
            list(simulation_data["lanes"][3]),
        ]
        self.max_iterations = len(self.lanes[0])
        self.initial_bikes = simulation_data["bikes"]
        self.bikes = simulation_data["bikes"]
        self.last_command = ""

    def reset(self):
        """Restore simulation to initial state"""
        self.bikes = self.initial_bikes
        self.remaining_bikes = self.total_bikes
        self.speed = 0
        self.success_bikes = 0
        self.last_command = ""

    def render(self, iteration, command):
        """Render function to output the current state of the simulation"""
        if iteration == 0:
            print(f"Initial State")
        else:
            print(f"Iteration: {iteration} | After: {command}")
        for i in range(self.max_iterations):
            value = "{:02d}".format(i)
            print(value[0], end="")
        print()
        for i in range(self.max_iterations):
            value = "{:02d}".format(i)
            print(value[1], end="")
        print()
        for i in range(self.max_iterations):
            print("-", end="")
        print()

        shadow_lanes = []
        for lane in self.lanes:
            shadow_lanes.append(lane.copy())

        bike_index = 1
        for bike in self.bikes:
            x, y, a = [int(j) for j in bike.split()]
            if a == 0 or a == 1:
                shadow_lanes[y][x] = f"{bike_index}"
            bike_index = bike_index + 1

        for lane in shadow_lanes:
            for i in range(len(lane)):
                c = lane[i]
                if c == "0":
                    c = "x"
                print(c, end="")
            print()
        print("\n")

    def process(self, command):
        """Process a single command or iteration of the simulation"""
        last_command = self.last_command
        remaining_bikes = self.remaining_bikes
        speed = self.speed
        success_bikes = self.success_bikes

        bike_data = []
        for bike in self.bikes:
            bike_data.append([int(j) for j in bike.split()])

        if remaining_bikes == 0:
            return (True, success_bikes)

        if command == "SPEED":
            speed = speed + 1
            self.speed = speed
        elif command == "SLOW":
            speed = speed - 1
            if speed < 0:
                speed = 0
            self.speed = speed
        elif command == "JUMP":
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
                if bike_data[last_active_bike][1] < len(self.lanes) - 1:
                    for b in range(len(bike_data)):
                        if bike_data[b][2]:
                            bike_data[b][1] = bike_data[b][1] + 1

        for b in range(len(bike_data)):
            x, y, a = bike_data[b]
            if a == 0:
                continue
            print(f"Path({b} {x}-{x+speed+1}): [", end="")
            for j in range(x, x + speed + 1):
                if j >= self.max_iterations:
                    break
                print(f"{self.lanes[y][j]}", end="")
                if self.lanes[y][j] == "0" and last_command != "JUMP":
                    remaining_bikes = remaining_bikes - 1
                    a = 0
                    x = j
                    break

            print("]")
            print(f"Speed: {speed}")
            if a != 0:
                x = x + speed
                if x >= self.max_iterations:
                    x = self.max_iterations - 1
                    success_bikes = success_bikes + 1
                    remaining_bikes = remaining_bikes - 1
            else:
                bike_data[b][2] = 0

            bike_data[b][0] = x
            self.success_bikes = success_bikes
            self.remaining_bikes = remaining_bikes
            self.bikes[b] = f"{x} {y} {a}"
        self.last_command = command
        return (False, 0)
