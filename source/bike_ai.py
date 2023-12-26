"""Bike AI module"""
from state_space_search_tree import S3T
from simulator import SimulatorState, SimulatorCommand

class Bike_AI:
    COMMANDS = [
        SimulatorCommand.COMMAND_NONE,
        SimulatorCommand.COMMAND_SPEED,
        SimulatorCommand.COMANND_SLOW,
        SimulatorCommand.COMMAND_JUMP,
        SimulatorCommand.COMMAND_WAIT,
        SimulatorCommand.COMMAND_UP,
        SimulatorCommand.COMMAND_DOWN,
    ]

    commands = [
        "SPEED",
        "SPEED",
        "SPEED",
        "SLOW",
        "JUMP",
        "WAIT",
        "WAIT",
        "SPEED",
        "SPEED",
        "SPEED",
        "SPEED",
    ]
    command_index = 0

    def __init__(self, simulator, data):
        self.simulator = simulator        
        self.total_bikes = simulator.total_bikes
        self.required_bikes = simulator.required
        self.lanes = simulator.lanes
        self.speed = data["speed"]
        root_state = SimulatorState(None)
        root_state.remaining_bikes = self.total_bikes
        for bike in data["bikes"]:
            root_state.bikes.append(bike.copy())

        self.__s3t__ = S3T(root_state)
        for command in self.COMMANDS:
            if command != 0:
                state = root_state.clone()
                state.command = command
                new_state = self.simulator.process(state)
                child_node = S3T(new_state, self.__s3t__)
                self.__s3t__.children.append(child_node)

    def process(self, data):
        self.speed = data["speed"]
        self.bikes = data["bikes"]

        command = ""
        if self.command_index < len(self.commands):
            command = self.commands[self.command_index]
            self.command_index = self.command_index + 1

        return command
