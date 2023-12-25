"""
Simulator
This module invokes the main.py module and runs the meta simulation.
"""


class SimulatorState:
    def __init__(self, simulation_data):
        """constructor"""
        if simulation_data != None:
            self.remaining_bikes = simulation_data["total_bikes"]
            self.success_bikes = 0
            self.speed = simulation_data["speed"]
            self.bikes = simulation_data["bikes"]
            self.command = ""
            self.last_command = ""
            self.iteration = 0
            self.game_over = False

    def clone(self):
        new_state = SimulatorState(None)
        new_state.remaining_bikes = self.remaining_bikes
        new_state.success_bikes = self.success_bikes
        new_state.speed = self.speed
        new_state.bikes = []
        for bike in self.bikes:
            new_state.bikes.append(bike.copy())

        new_state.command = self.command
        new_state.last_command = self.last_command
        new_state.iteration = self.iteration
        new_state.game_over = self.game_over
        return new_state

    def __str__(self):
        bike_data = []
        for bike in self.bikes:
            bike_data.append(f"{bike}")
        output = [
            "<SimulatorState\n",
            f"  iteration: {self.iteration}\n",
            f"  command: {self.command}\n",
            f"  last_command :{self.last_command}\n",
            f"  speed: {self.speed}\n",
            f"  bikes:\n",
            f"    {''.join(bike_data)}\n"
            f"  remaining_bikes: {self.remaining_bikes}\n",
            f"  success_bikes: {self.success_bikes}\n" ">\n",
        ]
        return "".join(output)


class Simulator:
    """Simulator class. Encapsulates a running instance of a simulation"""

    """Possible commands ["SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]"""

    def __init__(self, simulation_data):
        """constructor"""
        self.name = simulation_data["name"]
        self.total_bikes = simulation_data["total_bikes"]
        self.required = simulation_data["required"]
        self.lanes = [
            list(simulation_data["lanes"][0]),
            list(simulation_data["lanes"][1]),
            list(simulation_data["lanes"][2]),
            list(simulation_data["lanes"][3]),
        ]
        self.max_iterations = len(self.lanes[0])

    def render(self, state):
        """Render function to output the current state of the simulation"""
        if state.iteration == 0:
            print(f"Initial State")
        else:
            print(f"Iteration: {state.iteration} ({state.command})")

        print(f"Speed: {state.speed}")

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
        for bike in state.bikes:
            x, y, a = bike
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

    def process(self, state, command, iteration):
        """Process a single command or iteration of the simulation"""
        cloned_state = state.clone()
        cloned_state.command = command
        cloned_state.iteration = iteration

        len_bike_data = len(cloned_state.bikes)

        if cloned_state.remaining_bikes == 0:
            cloned_state.game_over = True
            return cloned_state

        if cloned_state.command == "SPEED":
            cloned_state.speed = state.speed + 1
        elif cloned_state.command == "SLOW":
            cloned_state.speed = state.speed - 1
            if cloned_state.speed < 0:
                cloned_state.speed = 0
        elif cloned_state.command == "JUMP":
            pass
        elif cloned_state.command == "WAIT":
            pass
        elif cloned_state.command == "UP":
            first_active_bike = -1
            for b in range(len_bike_data):
                if cloned_state.bikes[b][2]:
                    first_active_bike = b
                    break
            if first_active_bike > -1:
                if cloned_state.bikes[first_active_bike][1] > 0:
                    for b in range(len_bike_data):
                        if cloned_state.bikes[b][2]:
                            cloned_state.bikes[b][1] = cloned_state.bikes[b][1] - 1
        elif cloned_state.command == "DOWN":
            last_active_bike = -1
            for b in reversed(range(len_bike_data)):
                if cloned_state.bikes[b][2]:
                    last_active_bike = b
                    break
            if last_active_bike > -1:
                if cloned_state.bikes[last_active_bike][1] < len(self.lanes) - 1:
                    for b in range(len_bike_data):
                        if cloned_state.bikes[b][2]:
                            cloned_state.bikes[b][1] = cloned_state.bikes[b][1] + 1

        for b in range(len_bike_data):
            x, y, a = cloned_state.bikes[b]
            if a == 0:
                continue

            for j in range(x, x + cloned_state.speed + 1):
                if j >= self.max_iterations:
                    break
                if self.lanes[y][j] == "0" and cloned_state.last_command != "JUMP":
                    cloned_state.remaining_bikes = cloned_state.remaining_bikes - 1
                    a = 0
                    x = j
                    break

            if a != 0:
                x = x + cloned_state.speed
                if x >= self.max_iterations:
                    x = self.max_iterations - 1
                    cloned_state.success_bikes = cloned_state.success_bikes + 1
                    cloned_state.remaining_bikes = cloned_state.remaining_bikes - 1
            else:
                cloned_state.bikes[b][2] = 0

            cloned_state.bikes[b][0] = x

        cloned_state.last_command = cloned_state.command
        cloned_state.game_over = False
        return cloned_state
