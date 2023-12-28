"""Test cases for Simulator"""

def simulation0():
    return {
        "name": "Sim 1: One lonley hole",
        "total_bikes": 2,
        "required": 1,
        "speed": 0,
        
        # "lanes": [
        #     "....",
        #     "..0.",
        #     "....",
        #     "....",
        # ],

        "lanes": [
            "..........",
            "..........",
            "......0...",
            "..........",
        ],

        "bikes": [
            [0, 2, 1],
            [0, 3, 1]
        ],
        "commands": [
            "SPEED",
            "UP",
            "SPEED",
            "SPEED",
        ],
    }

def simulation1():
    return {
        "name": "Sim 1: One lonley hole",
        "total_bikes": 1,
        "required": 1,
        "speed": 0,
        "lanes": [
            "..................................",
            "..................................",
            "...........0......................",
            "..................................",
        ],
        "bikes": [
            [0, 2, 1]
        ],
        "commands": [
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
        ],
    }


def simulation2():
    return {
        "name": "Sim 2",
        "total_bikes": 2,
        "required": 1,
        "speed": 0,
        "lanes": [
            "....0.............................",
            "................0.................",
            "......................00..........",
            "............0.....................",
        ],
        "bikes": [
            [0, 0, 1],
            [0, 3, 1],
        ],
        "commands": [
            "SPEED",
        ],
    }


def simulation3():
    return {
        "name": "Sim 3: Jump into hole",
        "total_bikes": 1,
        "required": 1,
        "speed": 0,
        "lanes": [
            "......0...........................",
            "..................................",
            "..................................",
            "..................................",
        ],
        "bikes": [
            [0, 0, 1],
        ],
        "commands": [
            "SPEED",
            "WAIT",
            "WAIT",
            "WAIT",
            "JUMP",
        ],
    }

def simulation4():
    return {
        "name": "Sim 4: Jump over hole",
        "total_bikes": 1,
        "required": 1,
        "speed": 0,
        "lanes": [
            "......0...........................",
            "..................................",
            "..................................",
            "..................................",
        ],
        "bikes": [
            [0, 0, 1],
        ],
        "commands": [
            "SPEED",
            "SPEED",
            "JUMP",
        ],
    }

def simulation5():
    return {
        "name": "Sim 5: Jump over hole",
        "total_bikes": 1,
        "required": 1,
        "speed": 0,
        "lanes": [
            "......0...........................",
            "..................................",
            "..................................",
            "..................................",
        ],
        "bikes": [
            [0, 0, 1],
        ],
        "commands": [
            "SPEED",
            "SPEED",
            "JUMP",
            "SPEED",
            "SPEED",
            "SPEED",
            "SPEED",
            "SPEED",
            "SPEED",
        ],
    }
