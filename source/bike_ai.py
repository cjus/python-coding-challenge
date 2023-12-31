"""Bike AI module"""
import time
from state_space_search_tree import S3T_Node
from simulator import SimulatorState, SimulatorCommand
from graph_viz import GraphViz


class Bike_AI:
    MAX_DEPTH = 50
    COMMANDS = [
        SimulatorCommand.COMMAND_NONE,
        SimulatorCommand.COMMAND_SPEED,
        SimulatorCommand.COMMAND_JUMP,
        SimulatorCommand.COMMAND_UP,
        SimulatorCommand.COMMAND_DOWN,
        SimulatorCommand.COMMAND_SLOW,
        SimulatorCommand.COMMAND_WAIT,
    ]
    COMMANDS_STRS = [
        "",
        "SPEED",
        "JUMP",
        "UP",
        "DOWN",
        "SLOW",
        "WAIT",
    ]

    commands = [
        "SPEED",
        "UP",
        "SPEED",
        "SPEED",
    ]

    command_index = 0

    def __init__(self, simulator, use_graphviz=False, debug=False, full_search=False):
        self.start = time.time()
        self.simulator = simulator
        self.total_bikes = simulator.total_bikes
        self.required_bikes = simulator.required
        self.lanes = simulator.lanes
        self.highest_score = -9999
        self.max_depth_reached = 0
        self.use_graphviz = use_graphviz
        self.winning_node = None
        self.node_id = 0
        self.debug = debug
        self.full_search = full_search
        self.end_search = False
        self.winning_line = {}

    def process_move(self, data):
        self.node_id = 0
        state = SimulatorState(None)
        state.speed = data["speed"]
        state.remaining_bikes = data["remaining_bikes"]
        for bike in data["bikes"]:
            state.bikes.append(bike.copy())

        if self.use_graphviz:
            self.graph_viz = GraphViz("bikes")

        self.s3t_node = S3T_Node(state, f"root-{self.node_id}")
        self.build_search_tree(self.s3t_node, 0, self.MAX_DEPTH)
        self.end = time.time()

        if self.use_graphviz:
            self.graph_viz.render()

        return self.get_winning_line()

    def build_search_tree(self, node, depth, max_depth):
        if self.end_search:
            return

        if depth == max_depth or node.get_data().game_over:
            return

        if self.use_graphviz:
            self.graph_viz.add_node(node.label, round(node.score, 4), False, False)

        for command in self.COMMANDS:
            if command != 0:
                if node.data.speed == 0 and command != SimulatorCommand.COMMAND_SPEED:
                    continue

                new_state = node.data.clone()
                new_state.command = command

                child_state = self.simulator.process(new_state)
                score = child_state.remaining_bikes - ((node.depth + 1) * 0.01)
                if score < self.highest_score:
                    continue

                self.node_id += 1
                if self.debug:
                    print(f"... adding node {self.node_id}", end="\r")
                child_node = S3T_Node(child_state, f"{self.node_id}", node)
                child_depth = child_node.get_depth()
                if child_depth > self.max_depth_reached:
                    self.max_depth_reached = child_depth

                child_node.set_score(score)
                node.append_child(child_node)

                game_over = child_state.game_over
                has_win = (
                    game_over and child_state.remaining_bikes >= self.required_bikes
                )
                if has_win:
                    if score > self.highest_score:
                        if not self.full_search:
                            self.end_search = True

                        self.highest_score = score
                        self.winning_node = child_node

                        if self.debug:
                            self.end = time.time()
                            print(
                                f"Found a winning line at node ({self.node_id}) with a score of {self.highest_score} in {round(self.get_elapsed_time(),4)} seconds"
                            )
                            print(f"\t{self.output_winning_line(child_node)}")

                        if self.use_graphviz:
                            self.graph_viz.add_node(
                                child_node.label, round(score, 4), has_win, game_over
                            )
                            self.graph_viz.add_edge(
                                node.label,
                                child_node.label,
                                self.COMMANDS_STRS[command],
                            )

                if self.use_graphviz:
                    self.graph_viz.add_node(
                        child_node.label, round(score, 4), has_win, game_over
                    )
                    self.graph_viz.add_edge(
                        node.label,
                        child_node.label,
                        f"{self.COMMANDS_STRS[command]}-{depth}",
                    )

                if not has_win:
                    self.build_search_tree(child_node, depth + 1, max_depth)

    def output_winning_line(self, node):
        if node is None:
            return []
        winning_moves = [node.get_score()]
        while node != None:
            state = node.get_data()
            if state.command == 0:
                break
            winning_moves.append(self.COMMANDS_STRS[state.command])
            node = node.get_parent()
        winning_moves.reverse()
        return winning_moves

    def get_maximum_nodes(self):
        commands_per_node = len(self.COMMANDS) - 1
        nodes_at_depth = []
        nodes_at_level = 1
        for j in range(1, self.max_depth_reached + 1):
            nodes_at_depth.append(nodes_at_level * commands_per_node)
            nodes_at_level = nodes_at_level * commands_per_node
        return sum(nodes_at_depth)

    def get_winning_line(self):
        return self.output_winning_line(self.winning_node)

    def get_elapsed_time(self):
        return self.end - self.start

    def process(self, data):
        self.speed = data["speed"]
        self.bikes = data["bikes"]

        command = ""
        if self.command_index < len(self.commands):
            command = self.commands[self.command_index]
            self.command_index = self.command_index + 1

        return command
