"""
Simulator
This module invokes the main.py module and runs the meta simulation.
Notes:
  - in a larger program simulator state could be encoded using Bit fields
"""


class SimulatorCommand:
    COMMAND_NONE = 0
    COMMAND_SPEED = 1
    COMANND_SLOW = 2
    COMMAND_JUMP = 3
    COMMAND_WAIT = 4
    COMMAND_UP = 5
    COMMAND_DOWN = 6


class SimulatorState:
    def __init__(self, state):
        """constructor"""
        if state == None:
            self.score = 0
            self.remaining_bikes = 0
            self.success_bikes = 0
            self.speed = 0
            self.bikes = []
            self.command = SimulatorCommand.COMMAND_NONE
            self.game_over = False
        else:
            self.score = 0
            self.remaining_bikes = state.total_bikes
            self.success_bikes = state.success_bikes
            self.speed = state.speed
            self.bikes = []
            for bike in state.bikes:
                self.bikes.append(bike.copy())
            self.command = self.command
            self.game_over = False

    def clone(self):
        new_state = SimulatorState(None)
        new_state.score = self.score = 0
        new_state.remaining_bikes = self.remaining_bikes
        new_state.success_bikes = self.success_bikes
        new_state.speed = self.speed
        new_state.bikes = []
        for bike in self.bikes:
            new_state.bikes.append(bike.copy())
        new_state.command = self.command
        # new_state.last_command = self.last_command
        new_state.game_over = self.game_over
        return new_state

    def __str__(self):
        bike_data = []
        for bike in self.bikes:
            bike_data.append(f"{bike}")
        output = [
            "<SimulatorState\n",
            f"  command: {self.command}\n",
            f"  speed: {self.speed}\n",
            f"  bikes:\n",
            f"    {''.join(bike_data)}\n"
            f"  remaining_bikes: {self.remaining_bikes}\n",
            f"  success_bikes: {self.success_bikes}\n" ">\n",
        ]
        return "".join(output)


class Simulator:
    """Simulator class. Encapsulates a running instance of a simulation"""

    COMMANDS_STRS = ["", "SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]

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
            print(f"Command: {self.COMMANDS_STRS[state.command]})")

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

    def process(self, state):
        """Process a single command or iteration of the simulation"""
        state = state.clone()
        len_bike_data = len(state.bikes)

        if state.remaining_bikes == 0:
            state.game_over = True
            return state

        if state.command == SimulatorCommand.COMMAND_SPEED:  # handle SPEED
            state.speed = state.speed + 1
        elif state.command == "SLOW":  # handle SLOW
            state.speed = state.speed - 1
            if state.speed < 0:
                state.speed = 0
        elif state.command == SimulatorCommand.COMMAND_JUMP:  # handle JUMP
            pass
        elif state.command == SimulatorCommand.COMMAND_WAIT:  # handle WAIT
            pass
        elif state.command == SimulatorCommand.COMMAND_UP:  # handle UP
            first_active_bike = -1
            for b in range(len_bike_data):
                if state.bikes[b][2]:
                    first_active_bike = b
                    break
            if first_active_bike > -1:
                if state.bikes[first_active_bike][1] > 0:
                    for b in range(len_bike_data):
                        if state.bikes[b][2]:
                            state.bikes[b][1] = state.bikes[b][1] - 1
        elif state.command == SimulatorCommand.COMMAND_DOWN:  # handle DOWN
            last_active_bike = -1
            for b in reversed(range(len_bike_data)):
                if state.bikes[b][2]:
                    last_active_bike = b
                    break
            if last_active_bike > -1:
                if state.bikes[last_active_bike][1] < len(self.lanes) - 1:
                    for b in range(len_bike_data):
                        if state.bikes[b][2]:
                            state.bikes[b][1] = state.bikes[b][1] + 1

        for b in range(len_bike_data):
            x, y, a = state.bikes[b]
            if a == 0:
                continue

            for j in range(x, x + state.speed + 1):
                if j >= self.max_iterations:
                    break
                if (
                    self.lanes[y][j] == "0"
                    and state.last_command != SimulatorCommand.COMMAND_JUMP
                ):
                    state.remaining_bikes = state.remaining_bikes - 1
                    a = 0
                    x = j
                    break

            if a != 0:
                x = x + state.speed
                if x >= self.max_iterations:
                    x = self.max_iterations - 1
                    state.success_bikes = state.success_bikes + 1
                    state.remaining_bikes = state.remaining_bikes - 1
            else:
                state.bikes[b][2] = 0

            state.bikes[b][0] = x

        state.game_over = False
        return state
