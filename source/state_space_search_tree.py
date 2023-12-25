"""Basic implementation of a State Space Search Tree (S3T)"""


class S3T:
    def __init__(self, data):
        self.data = data
        self.children = []
