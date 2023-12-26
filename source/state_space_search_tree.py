"""Basic implementation of a State Space Search Tree (S3T)"""


class S3T:
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.children = []
