from board import Board
from gametree import GameTree
import random

tree = GameTree()
tree.buildTree(tree.root)
w_wins = 0
b_wins = 0
while True:
    print('-----------------Game Start---------------------')
    round = 1
    winner = 'x'
    cur_node = tree.root
    while True:
        print(f'\n------Round: {round}------')
        print(cur_node.entry)
        if round % 2 == 0:
            #robot turn
            moves = cur_node.children
            if len(moves) == 0:
                print(f'{cur_node.entry.winner} wins!')
                winner = cur_node.entry.winner
                break
            r_str = ""
            for i in range(3):
                for k in range(len(moves)):
                    if i == 0:
                        r_str += f"{k+1}) "
                    else:
                        r_str += "   "
                    for j in moves[k].entry.boardList[i]:
                        if j == 'x':
                            j = '~'
                        r_str+= f"{j} "
                r_str += '\n'                    
            print(r_str)
            choices = []
            for move in moves:
                if move.val == 0:
                    choices.append(move)
            choice = moves.index(random.choice(choices))
            print(f'Robot choice: {choice + 1}')
            cur_node = cur_node.children[choice]
            round+=1
        else:
            #prints the available moves from current position
            moves = cur_node.children
            if len(moves) == 0:
                print(f'{cur_node.entry.winner} wins!')
                winner = cur_node.entry.winner
                break
            r_str = ''
            for i in range(3):
                for k in range(len(moves)):
                    if i == 0:
                        r_str += f"{k+1}) "
                    else:
                        r_str += "   "
                    for j in moves[k].entry.boardList[i]:
                        if j == 'x':
                            j = '~'
                        r_str+= f"{j} "
                r_str += '\n'                    
            print(r_str)
            choice = -1
            while True:
                choice = input('Enter move choice: ')
                try:
                    choice = int(choice)
                    if choice >= 1 and choice <= len(moves):
                        break
                    print('Please enter a valid int')
                except:
                    print("Please enter an int")
            choice -= 1
            cur_node = cur_node.children[choice]
            round+=1
    if winner == 'w':
        tree.update(cur_node.id)
        w_wins+=1
    else:
        b_wins+=1
    print('------------------Game End----------------------')
    print(f'white wins: {w_wins} | black wins: {b_wins}')


