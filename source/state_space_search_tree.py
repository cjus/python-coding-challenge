"""Basic implementation of a State Space Search Tree (S3T)"""


class S3T_Node:
    def __init__(self, data, label=None, parent=None):
        self.data = data
        self.score = 0
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.label = f"{label}-{self.depth}"
        self.parent = parent
        self.children = []

    def append_child(self, data):
        self.children.append(data)

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent

    def get_depth(self):
        return self.depth
    
    def get_score(self):
        return self.score

    def get_children(self):
        return self.children

    def set_score(self, score):
        self.score = score