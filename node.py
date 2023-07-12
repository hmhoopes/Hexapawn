class Node:
    def __init__(self, entry, id):
        #val will be a list representing board position at this entry
        self.entry = entry
        self.id = id
        self.val = 0
        self.children = []
    