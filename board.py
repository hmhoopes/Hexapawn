import copy
class Board:
    def __init__(self, board = [['b','b','b'],['x','x','x'],['w','w','w']], turn = 'w'):
        #in call: boardList[row][col] will give the piece at row x col
        self.boardList = board
        #indicates who's turn it is 
        self.turn = turn
        self.winner = 'x'
        self.moves = self.won()

    def won(self):
        #check if there aren't any enemies:
        enemyCount = 0
        for i in self.boardList:
            for j in i:
                if j !='x' and j !=self.turn:
                    enemyCount += 1
        if enemyCount == 0:
            self.winner = self.turn
            return []
        #check if reached the end:
        for i in range(3):
            if self.boardList[0][i] == 'w':
                self.winner = 'w'
                return []
            if self.boardList[2][i] == 'b':
                self.winner = 'b'
                return []

        moves = self.getMoves()
        if len(moves) == 0:
            self.winner = 'b' if self.turn == 'w' else 'w'
            return []
        return moves
        

    def getMoves(self):
        '''Returns a list of boards, each representing a possible game state from current one'''
        moves = []
        if self.winner != 'x':
            return moves
        play_pieces = []#list of tuples representing position of playable pieces
        for i in range(3):
            for j in range(3):
                if self.turn == 'w' and self.boardList[i][j] == 'w':
                    play_pieces.append((i,j))
                elif self.turn == 'b' and self.boardList[i][j] == 'b':
                    play_pieces.append((i,j))
        #print(play_pieces)
        if self.turn == 'w':
            for pos in play_pieces:
                row = pos[0]
                col = pos[1]
                cur_moves = []#list of potential positions for current piece
                #checks if space ahead is valid, and moves if so
                if row - 1 >= 0 and self.boardList[row-1][col] == 'x': 
                    cur_moves.append((row-1,col))
                #checks if space to left diagonal is valid, and moves if so
                if row-1 >=0 and col-1>=0 and self.boardList[row-1][col-1] == 'b':
                    cur_moves.append((row-1,col-1))
                #checks if space to right diagonal is vvalid, and moves if so
                if row-1>=0 and col+1<=2 and self.boardList[row-1][col+1] == 'b':
                    cur_moves.append((row-1,col+1))
                #print(cur_moves)
                for move in cur_moves:
                    n_row = move[0]
                    n_col = move[1]
                    n_boardList = copy.deepcopy(self.boardList)
                    n_boardList[row][col] = 'x'
                    n_boardList[n_row][n_col] = 'w'
                    moves.append(Board(board=n_boardList, turn = 'b'))
            return moves
        elif self.turn == 'b':
            for pos in play_pieces:
                row = pos[0]
                col = pos[1]
                cur_moves = []#list of potential positions for current piece
                #checks if space ahead is valid, and moves if so
                if row + 1 <= 2 and self.boardList[row + 1][col] == 'x': 
                    cur_moves.append((row + 1,col))
                #checks if space to left diagonal is valid, and moves if so
                if row + 1 <= 2 and col-1>=0 and self.boardList[row + 1][col-1] == 'w':
                    cur_moves.append((row + 1,col-1))
                #checks if space to right diagonal is vvalid, and moves if so
                if row + 1 <= 2 and col+1<=2 and self.boardList[row + 1][col+1] == 'w':
                    cur_moves.append((row + 1,col+1))
                #print(cur_moves)
                for move in cur_moves:
                    n_row = move[0]
                    n_col = move[1]
                    n_boardList = copy.deepcopy(self.boardList)
                    n_boardList[row][col] = 'x'
                    n_boardList[n_row][n_col] = 'b'
                    moves.append(Board(board=n_boardList, turn='w'))
            return moves

    def __str__(self) -> str:
        '''Returns str representation of current game position'''
        returnStr = ""
        for i in self.boardList:
            for j in i:
                if j == 'x':
                    returnStr += "~ "
                else:    
                    returnStr += j + " "
            returnStr += "\n"
        return returnStr
    
    def __repr__(self) -> str:
        return "\n"+str(self)
    