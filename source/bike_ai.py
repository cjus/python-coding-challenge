"""Bike AI module"""
import math
from state_space_search_tree import S3T_Node
from state_stack import Stack, Stack_Node
from simulator import SimulatorState, SimulatorCommand
from graph_viz import GraphViz


class Bike_AI:
    COMMANDS = [
        SimulatorCommand.COMMAND_NONE,
        SimulatorCommand.COMMAND_SPEED,
        SimulatorCommand.COMMAND_WAIT,
        SimulatorCommand.COMMAND_JUMP,
        SimulatorCommand.COMMAND_UP,
        SimulatorCommand.COMMAND_DOWN,
        SimulatorCommand.COMANND_SLOW,
    ]
    # COMMANDS = [
    #     SimulatorCommand.COMMAND_NONE,
    #     SimulatorCommand.COMMAND_SPEED,
    #     SimulatorCommand.COMMAND_UP,
    #     SimulatorCommand.COMMAND_DOWN,
    # ]
    COMMANDS_STRS = ["", "SPEED", "WAIT", "JUMP", "UP", "DOWN", "SLOW",]

    # commands = [
    #     "SPEED",
    #     "SPEED",
    #     "SPEED",
    #     "SLOW",
    #     "JUMP",
    #     "WAIT",
    #     "WAIT",
    #     "SPEED",
    #     "SPEED",
    #     "SPEED",
    #     "SPEED",
    # ]

    commands = [
        "SPEED",
        "UP",
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
        self.highest_score = -9999

        self.stack = Stack()
        state = SimulatorState(None)
        state.remaining_bikes = self.total_bikes
        for bike in data["bikes"]:
            state.bikes.append(bike.copy())

        self.graph_viz = GraphViz("bikes")

        self.node_id = 0
        self.s3t_node = S3T_Node(state, f"root-{self.node_id}")
        self.stack.push(self.s3t_node)
        self.build_search_tree(self.s3t_node, 0, 20)

        self.graph_viz.render()

    def build_search_tree(self, node, depth, max_depth):
        if depth == max_depth or node.get_data().game_over:
            return
        if (node.score <= self.highest_score):
            return

        self.graph_viz.add_node(node.label, round(node.score, 4), False, False)
        for command in self.COMMANDS:
            if command != 0:
                new_state = node.data.clone()
                new_state.command = command

                child_state = self.simulator.process(new_state)

                self.node_id += 1
                child_node = S3T_Node(child_state, f"{self.node_id}", node)
                self.stack.push(child_node)
                node.append_child(child_node)
                score = child_state.remaining_bikes - (child_node.get_depth() * 0.01)
                    
                child_node.set_score(score)
                game_over = child_node.get_data().game_over
                has_win = (
                    game_over
                    and child_state.remaining_bikes >= self.required_bikes
                )
                if has_win:
                    if score > self.highest_score:
                        self.highest_score = score
                        print(f"Highest score: {self.highest_score}")
                        self.graph_viz.add_node(child_node.label, round(score, 4), has_win, game_over)
                        self.graph_viz.add_edge(
                            node.label, child_node.label, self.COMMANDS_STRS[command]
                        )
                        break

                if (score <= self.highest_score):
                    break

                self.graph_viz.add_node(child_node.label, round(score, 4), has_win, game_over)
                self.graph_viz.add_edge(
                    node.label, child_node.label, self.COMMANDS_STRS[command]
                )

                if game_over:
                    break

                if not has_win:
                    self.build_search_tree(child_node, depth + 1, max_depth)

    def process(self, data):
        self.speed = data["speed"]
        self.bikes = data["bikes"]

        command = ""
        if self.command_index < len(self.commands):
            command = self.commands[self.command_index]
            self.command_index = self.command_index + 1

        return command
