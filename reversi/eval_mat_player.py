import random

class MyPlayer:
    '''This Player plays randomly'''
    def __init__(self, my_color, opponent_color):
        self.name = 'krivast1'
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.size = 8

        self.moves = [(-1,-1), (+1,+1), (-1,+1), (+1,-1), (+1,0), (0,+1), (-1,0), (0,-1)]

        self.evalMatrix = [
            [20,0 ,10,10,10,10,0 ,20],
            [0 ,0 ,2 ,2 ,2 ,2 ,0 ,0 ],
            [10,2 ,10,8 ,8 ,10,2 ,10],
            [10,2 ,8 ,5 ,5 ,8 ,2 ,10],
            [10,2 ,8 ,5 ,5 ,8 ,2 ,10],
            [10,2 ,10,8 ,8 ,10,2 ,10],
            [0 ,0 ,2 ,2 ,2 ,2 ,0 ,0 ],
            [20,0 ,10,10,10,10,0 ,20]]

    def move(self, board):
        self.get_coords(board)
        self.get_possible_moves()

        if self.possible_moves:
            ret = self.chooseBestMove()
        else:
            ret = None
        return ret

    def chooseBestMove(self):
        bestValue = -1
        for move in self.possible_moves:
            moveValue = self.evalMatrix[move[0]][move[1]]
            if moveValue > bestValue:
                bestValue = moveValue
                bestMove = move
        return bestMove

    def get_coords(self, board):
        self.free_tokens = []
        self.my_tokens = []
        self.enemy_tokens = []

        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == -1:
                    self.free_tokens.append((row,col))
                elif board[row][col] == self.my_color:
                    self.my_tokens.append((row,col))
                else:
                    self.enemy_tokens.append((row,col))

    def get_possible_moves(self):
        self.possible_moves = []
        for my_token in self.my_tokens:
            for i in range(len(self.moves)):
                position = tuple(x + y for x, y in zip(my_token, self.moves[i]))

                if position in self.enemy_tokens:
                    while position in self.enemy_tokens:
                        position = tuple(x + y for x, y in zip(position, self.moves[i]))

                    if position in self.free_tokens:
                        self.possible_moves.append(position)
