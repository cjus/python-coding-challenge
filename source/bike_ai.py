"""Bike AI module"""
from state_space_search_tree import S3T


class Bike_AI:
    COMMAND_NONE = 0
    COMMAND_SPEED = 1
    COMANND_SLOW = 2
    COMMAND_JUMP = 3
    COMMAND_WAIT = 4
    COMMAND_UP = 5
    COMMAND_DOWN = 6
    COMMANDS = [
        COMMAND_NONE,
        COMMAND_SPEED,
        COMANND_SLOW,
        COMMAND_JUMP,
        COMMAND_WAIT,
        COMMAND_UP,
        COMMAND_DOWN,
    ]
    COMMANDS_STRS = ["SPEED", "SLOW", "JUMP", "WAIT", "UP", "DOWN"]

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

    def __init__(self, data):
        self.total_bikes = data["total_bikes"]
        self.required_bikes = data["required_bikes"]
        self.lanes = data["lanes"]
        self.__s3t__ = S3T({"parent": None, "score": 0, "command": self.COMMAND_NONE})
        self.__build_S3T__()
        self.speed = 0

    def __build_S3T__(self):
        for command in self.COMMANDS:
            if command != 0:
                self.__s3t__.children.append(
                    {"parent": self.__s3t__, "score": 0, "command": command}
                )

    def process(self, data):
        self.speed = data["speed"]
        self.bikes = data["bikes"]

        command = ""
        if self.command_index < len(self.commands):
            command = self.commands[self.command_index]
            self.command_index = self.command_index + 1

        return command
