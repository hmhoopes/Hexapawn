from node import Node
from board import Board
class GameTree:
    def __init__(self):
        self.idTracker = 0
        self.root = Node(Board(), self.idTracker)
        self.idTracker +=1

    def buildTree(self, cur_node):
        moves = cur_node.entry.moves
        if moves == 0:
            return
        for move in moves:
            cur_node.children.append(Node(move,self.idTracker))
            self.idTracker += 1
        for child in cur_node.children:
            self.buildTree(child)
    
    def update(self, target):
        self.rec_update(self.root, target)
    
    def rec_update(self, cur_node, target):
        if cur_node.entry.turn == 'w' and self.isDirectChildOf(cur_node, target):
            cur_node.val = -1
            return
        if cur_node.id == target and cur_node.entry.turn == 'w':
            cur_node.val = -1
            return
        for child in cur_node.children:
            if self.isChildOf(child, target):
                self.rec_update(child, target)
    
    def isDirectChildOf(self, cur_node, target):
        for child in cur_node.children:
            if child.id == target:
                return True
        return False

    def isChildOf(self, cur_node, target):
        if cur_node.id == target:
            return True
        for child in cur_node.children:
            if child.id == target:
                return True
            if self.isChildOf(child, target):
                return True
        return False

    def in_print(self):
        self.rec_print(self.root,0)
    
    def rec_print(self, cur_node, level):
        for child in cur_node.children:
            self.rec_print(child, level+1)
        print(f'level = {level} id = {cur_node.id} turn = {cur_node.entry.turn} winner = {cur_node.entry.winner} \ncur = \n{cur_node.entry}')

    

    