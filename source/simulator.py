"""
Simulator
This module invokes the main.py module and runs the meta simulation.
Notes:
  - in a larger program simulator state could be encoded using Bit fields
"""


class SimulatorCommand:
    COMMAND_NONE = 0
    COMMAND_SPEED = 1
    COMMAND_JUMP = 2
    COMMAND_UP = 3
    COMMAND_DOWN = 4
    COMMAND_SLOW = 5
    COMMAND_WAIT = 6


class SimulatorState:
    def __init__(self, state):
        """constructor"""
        if state == None:
            self.remaining_bikes = 0
            self.speed = 0
            self.bikes = []
            self.command = SimulatorCommand.COMMAND_NONE
            self.game_over = False
            self.last_command = SimulatorCommand.COMMAND_NONE
        else:
            self.remaining_bikes = state.total_bikes
            self.speed = state.speed
            self.bikes = []
            for bike in state.bikes:
                self.bikes.append(bike.copy())
            self.command = self.command
            self.game_over = False
            self.last_command = state.command

    def clone(self):
        new_state = SimulatorState(None)
        new_state.remaining_bikes = self.remaining_bikes
        new_state.speed = self.speed
        new_state.bikes = []
        for bike in self.bikes:
            new_state.bikes.append(bike.copy())
        new_state.command = self.command
        new_state.last_command = self.command
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
            f"  remaining_bikes: {self.remaining_bikes}>\n",
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
        self.max_hole_location = -1
        for lane in self.lanes:
            location = 0
            for slot in lane:
                if slot == "0":
                    if location > self.max_hole_location:
                        self.max_hole_location = location
                location += 1

    def render(self, state):
        """Render function to output the current state of the simulation"""
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
        is_moving_up = False
        is_moving_down = False

        if state.remaining_bikes == 0:
            state.game_over = True
            return state

        if state.command == SimulatorCommand.COMMAND_SPEED:  # handle SPEED
            state.speed = state.speed + 1
        elif state.command == SimulatorCommand.COMMAND_SLOW:  # handle SLOW
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
            if first_active_bike > -1 and state.bikes[first_active_bike][1] > 0:
                is_moving_up = True
        elif state.command == SimulatorCommand.COMMAND_DOWN:  # handle DOWN
            last_active_bike = -1
            for b in reversed(range(len_bike_data)):
                if state.bikes[b][2]:
                    last_active_bike = b
                    break
            if (
                last_active_bike > -1
                and state.bikes[last_active_bike][1] < len(self.lanes) - 1
            ):
                is_moving_down = True

        for b in range(len_bike_data):
            x, y, a = state.bikes[b]
            if a == 0:  # Bike is inactive, ignore
                continue

            # determine result of speed operation
            landing_slot = x + state.speed
            for j in range(x + 1, landing_slot):
                if j >= self.max_iterations:
                    break

                # if moving up check for holes on current path before moving up
                if (
                    is_moving_up
                    and state.last_command != SimulatorCommand.COMMAND_JUMP
                    and j != landing_slot
                ):
                    if self.lanes[y - 1][j] == "0":
                        state.remaining_bikes = state.remaining_bikes - 1
                        a = 0
                        x = j
                        break

                # if moving down check for holes on current path before moving down
                if (
                    is_moving_down
                    and state.last_command != SimulatorCommand.COMMAND_JUMP
                    and j != landing_slot
                ):
                    if self.lanes[y + 1][j] == "0":
                        state.remaining_bikes = state.remaining_bikes - 1
                        a = 0
                        x = j
                        break

                # if current square has a whole and the last operation was not a jump then lose bike
                if (
                    self.lanes[y][j] == "0"
                    and state.last_command != SimulatorCommand.COMMAND_JUMP
                ):
                    state.remaining_bikes = state.remaining_bikes - 1
                    a = 0
                    x = j
                    break

            if is_moving_up:
                y = y - 1
                state.bikes[b][1] = y

            if is_moving_down:
                y = y + 1
                state.bikes[b][1] = y

            # if land on hole,lose bike
            if (
                landing_slot < self.max_iterations
                and self.lanes[y][landing_slot] == "0"
            ):
                state.remaining_bikes = state.remaining_bikes - 1
                a = 0
                # x = j

            if a != 0:
                x = landing_slot
                if x >= self.max_iterations:
                    x = self.max_iterations
                    state.bikes[b][0] = x - 1
                    state.game_over = True
                else:
                    state.bikes[b][0] = x
            else:
                state.bikes[b][0] = x
                state.bikes[b][2] = 0

        if state.remaining_bikes < self.required:
            state.game_over = True
        if state.game_over == True:
            return state

        if state.remaining_bikes == 0:
            state.game_over = True
            return state

        state.game_over = False
        return state
