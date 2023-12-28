"""GraphViz wrapper class to build and render tree visualization"""

from graphviz import Digraph
from IPython.display import Image


class GraphViz:
    def __init__(self, name):
        self.name = name
        self.dot = Digraph(filename=f"{name}.gv")
        self.dot.format = "pdf"
        self.dot.fontname = "Helvetica,Arial,sans-serif"
        self.dot.graph_attr["layout"] = "dot"
        self.dot.graph_attr["fontsize"] = "12"
        self.dot.graph_attr["splines"] = "true"
        self.dot.graph_attr["overlap"] = "false"
        self.dot.graph_attr["rankdir"] = "TB"
        self.dot.graph_attr["beautify"] = "true"

        self.label_color = "#FFFFFF"
        self.label_win_color = "#00FF00"
        self.label_lose_color = "#FF0000"
        self.font_size = "18"
        self.node_color = "#444444"
        self.edge_color = "#000000"

    def add_node(self, node_name, ev, has_win, game_over):
        node_color = self.label_color
        if has_win:
            node_color = self.label_win_color
        elif game_over:
            node_color = self.label_lose_color
        self.dot.node(
            name=node_name,
            label=f"{node_name}\nev: {ev}",
            fontcolor=node_color,
            fontsize=f"{self.font_size}",
            color=self.node_color,
            style="filled",
        )

    def add_edge(self, parent_node_name, child_node_name, label):
        self.dot.edge(
            parent_node_name,
            child_node_name,
            color=self.edge_color,
            label=label,
            labelfontsize="6",
        )

    def render(self):
        self.dot.render()
        Image(f"{self.name}.{self.dot.format}")
