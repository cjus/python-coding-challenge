"""Test cases for Simulator"""


def simulation1():
    return {
        "name": "Sim 1: One lonley hole",
        "total_bikes": 1,
        "required": 1,
        "speed": 0,
        "lanes": [
            "..............................",
            "..............................",
            "...........0..................",
            "..............................",
        ],
        "bikes": [
            [0, 2, 1],
        ],
        "commands": [
            "SPEED",
            "SPEED",
            "SPEED",
            "SPEED",
            "JUMP",
            "SPEED",
            "SPEED",
            "SPEED",
        ],
    }


def simulation2():
    return {
        "name": "Sim 2: Chained jumps over increasing length",
        "total_bikes": 4,
        "required": 4,
        "speed": 1,
        "lanes": [
            "..........000......0000..............000000.............",
            "..........000......0000..............000000.............",
            "..........000......0000..............000000.............",
            "..........000......0000..............000000.............",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 1, 1],
            [0, 2, 1],
            [0, 3, 1],
        ],
        "commands": [
            "SPEED",
            "SPEED",
            "SPEED",
            "JUMP",
            "SPEED",
            "JUMP",
            "SPEED",
            "SPEED",
            "JUMP",
            "SPEED",
            "SPEED",
        ],
    }


def simulation3():
    return {
        "name": "Sim 3: Chained jumps over decreasing length",
        "total_bikes": 4,
        "required": 4,
        "speed": 8,
        "lanes": [
            "..............00000......0000.....00......",
            "..............00000......0000.....00......",
            "..............00000......0000.....00......",
            "..............00000......0000.....00......",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 1, 1],
            [0, 2, 1],
            [0, 3, 1],
        ],
        "commands": [],
    }


def simulation4():
    return {
        "name": "Sim 4: Chained jumps of equal length",
        "total_bikes": 4,
        "required": 4,
        "speed": 1,
        "lanes": [
            "..............00..00..00............",
            "..............00..00..00............",
            "..............00..00..00............",
            "..............00..00..00............",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 1, 1],
            [0, 2, 1],
            [0, 3, 1],
        ],
        "commands": [
            "SPEED",
            "SPEED",
            "SPEED",
            "JUMP",
            "JUMP",
            "JUMP",
            "JUMP",
            "SPEED",
            "SPEED",
        ],
    }


def simulation5():
    return {
        "name": "Sim 5: Diagonal columns of holes + 3 hole row",
        "total_bikes": 4,
        "required": 3,
        "speed": 6,
        "lanes": [
            ".............0.............0........",
            "..............0.............0.......",
            "...............0.............0......",
            "................0..........000......",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 1, 1],
            [0, 2, 1],
            [0, 3, 1],
        ],
        "commands": ["JUMP", "JUMP", "JUMP", "SPEED", "JUMP", "SPEED"],
    }


def simulation6():
    return {
        "name": "Sim 6: Scattered pits",
        "total_bikes": 2,
        "required": 2,
        "speed": 2,
        "lanes": [
            "...0......0....0........0..0..0..0.....",
            "....0............000........0...0......",
            ".....0..........000..........0.0.......",
            "...0......0....0........0..0..0..0.....",
        ],
        "bikes": [
            [0, 1, 1],
            [0, 2, 1],
        ],
        "commands": [
            "SPEED",
            "JUMP",
            "SPEED",
            "SPEED",
            "JUMP",
            "JUMP",
            "JUMP",
            "JUMP",
            "SPEED",
        ],
    }


def simulation7():
    return {
        "name": "Sim 7: Big jump chained with hole columns",
        "total_bikes": 3,
        "required": 2,
        "speed": 7,
        "lanes": [
            ".........0000000............................0.0.0.0.0.0.0.0.....",
            ".................0..........................0.0.0.0.0.0.0.0.....",
            ".........0000000............................0.0.0.0.0.0.0.0.....",
            "............................................0.0.0.0.0.0.0.0.....",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 1, 1],
            [0, 2, 1],
        ],
        "commands": [
            "SPEED",
            "JUMP",
            "JUMP",
            "SPEED",
            "SPEED",
            "JUMP",
            "JUMP",
            "SPEED",
        ],
    }


def simulation8():
    return {
        "name": "Sim 8: Diagonal columns of holes + 4 hole row with mandatory sacrifice",
        "total_bikes": 4,
        "required": 3,
        "speed": 6,
        "lanes": [
            ".............0.............0........",
            "..............0.............0.......",
            "...............0.............0......",
            "................0..........0000.....",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 1, 1],
            [0, 2, 1],
            [0, 3, 1],
        ],
        "commands": ["JUMP", "JUMP", "JUMP", "SPEED", "JUMP", "SPEED"],
    }


def simulation9():
    return {
        "name": "Sim 9: Obstacle course for 1 bike",
        "total_bikes": 1,
        "required": 1,
        "speed": 4,
        "lanes": [
            ".............................0..0....",
            ".0.0..................000....000.....",
            "....000.........0.0...000............",
            "............0.0......................",
        ],
        "bikes": [
            [0, 2, 1],
        ],
        "commands": [],
    }


def simulation10():
    return {
        "name": "Sim 10: Obstacle course for 2 bikes",
        "total_bikes": 2,
        "required": 2,
        "speed": 4,
        "lanes": [
            "............00000......00000.......",
            "...........0000..............0.....",
            "............00000......0000........",
            "...........00000.............0.....",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 2, 1],
        ],
        "commands": ["SPEED", "SPEED", "JUMP", "DOWN", "SLOW", "JUMP", "SPEED"],
    }


def simulation11():
    return {
        "name": "Sim 11: Mandatory sacrifices",
        "total_bikes": 4,
        "required": 1,
        "speed": 3,
        "lanes": [
            "...0........0........0000.....",
            "....00......0.0...............",
            ".....000.......00.............",
            ".............0.0..............",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 1, 1],
            [0, 2, 1],
            [0, 3, 1],
        ],
        "commands": [
            "SPEED",
            "JUMP",
            "SLOW",
            "JUMP",
            "JUMP",
            "SPEED",
            "SPEED",
            "SPEED",
        ],
    }


def simulation12():
    return {
        "name": "Sim 12: Well worn road",
        "total_bikes": 2,
        "required": 1,
        "speed": 1,
        "lanes": [
            "................000000000........00000........000.............00.",
            ".0.0..................000....000......0.0..................00000.",
            "....000.........0.0...000................000............000000.0.",
            "............0.000000...........0000...............0.0.....000000.",
        ],
        "bikes": [
            [0, 1, 1],
            [0, 2, 1],
        ],
        "commands": [],
    }
