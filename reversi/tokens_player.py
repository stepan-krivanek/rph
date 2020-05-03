import random
import copy

class MyPlayer:
    '''This Player plays randomly'''
    def __init__(self, my_color, opponent_color):
        self.name = 'krivast1'
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.size = 8

        self.moves = [(-1,-1), (+1,+1), (-1,+1), (+1,-1), (+1,0), (0,+1), (-1,0), (0,-1)]

        self.eval_matrix = [
            [20,0 ,10,10,10,10,0 ,20],
            [0 ,0 ,2 ,2 ,2 ,2 ,0 ,0 ],
            [10,2 ,10,8 ,8 ,10,2 ,10],
            [10,2 ,8 ,5 ,5 ,8 ,2 ,10],
            [10,2 ,8 ,5 ,5 ,8 ,2 ,10],
            [10,2 ,10,8 ,8 ,10,2 ,10],
            [0 ,0 ,2 ,2 ,2 ,2 ,0 ,0 ],
            [20,0 ,10,10,10,10,0 ,20]]

    def move(self, board):
        max_token_flips = self.size**2
        my_tokens, enemy_tokens, free_tokens = self.get_coords(board, self.my_color)
        my_possible_moves = self.get_possible_moves(my_tokens, enemy_tokens, free_tokens)
        evaluated_moves = []

        for coords in my_possible_moves:
            new_board = self.swap_stones(board, coords, self.my_color, self.opponent_color)

            max_value = self.early_game_minimax(
                    new_board,
                    self.opponent_color,
                    self.my_color,
                    1,
                    -max_token_flips,
                    max_token_flips,
                    False)
            
            value = max_value
            evaluated_moves.append(value)

        if my_possible_moves:
            return my_possible_moves[evaluated_moves.index(max(evaluated_moves))]
        else:
            return None

    def early_game_minimax(self, board, own_color, opponent_color, depth, alpha, beta, maximize):
        my_tokens, enemy_tokens, free_tokens = self.get_coords(board, own_color)
        my_possible_moves = self.get_possible_moves(my_tokens, enemy_tokens, free_tokens)

        if depth == 0:
            opponent_possible_moves = self.get_possible_moves(enemy_tokens, my_tokens, free_tokens)
            return len(my_tokens) - len(enemy_tokens)

        max_token_flips = self.size**2
        if maximize:
            max_value = -max_token_flips

            for coords in my_possible_moves:
                new_board = self.swap_stones(board, coords, own_color, opponent_color)
                max_tokens = self.early_game_minimax(new_board, opponent_color, own_color, depth - 1, alpha, beta, False)
                max_value = max(max_value, max_tokens)
                alpha = max(alpha, max_tokens)

                if beta <= alpha:
                    break
            return max_value
        else:
            min_value = max_token_flips

            for coords in my_possible_moves:
                new_board = self.swap_stones(board, coords, own_color, opponent_color)
                min_tokens = self.early_game_minimax(new_board, opponent_color, own_color, depth - 1, alpha, beta, True)
                min_value = min(min_value, min_tokens)
                beta = min(beta, min_tokens)

                if beta <= alpha:
                    break
            return min_value
    
    def swap_stones(self, board, coords, own_color, opponent_color):
        new_board = copy.deepcopy(board)
        new_board[coords[0]][coords[1]] = own_color
        
        for move in self.moves:
            next_row = coords[0] + move[0]
            next_col = coords[1] + move[1]
            row_border = next_row < self.size and next_row >= 0
            col_border = next_col < self.size and next_col >= 0
            if not row_border or not col_border: continue
            
            while new_board[next_row][next_col] == opponent_color:
                next_row += move[0]
                next_col += move[1]
                row_border = next_row < self.size and next_row >= 0
                col_border = next_col < self.size and next_col >= 0
                if not row_border or not col_border: break

            if not row_border or not col_border: continue
            if new_board[next_row][next_col] == own_color:
                while next_row != coords[0] or next_col != coords[1]:
                    new_board[next_row][next_col] = own_color
                    next_row -= move[0]
                    next_col -= move[1]
        return new_board

    def prt(self, board):
        for i in board:
            line = ""
            for j in i:
                if j == -1:
                    j = 'a'
                line += " " + str(j)
            print(line)
        print("\n")


    def get_coords(self, board, color):
        my_tokens = []
        enemy_tokens = []
        free_tokens = []

        for row in range(self.size):
            for col in range(self.size):
                if board[row][col] == -1:
                    free_tokens.append((row,col))
                elif board[row][col] == color:
                    my_tokens.append((row,col))
                else:
                    enemy_tokens.append((row,col))

        return my_tokens, enemy_tokens, free_tokens

    def get_possible_moves(self, my_tokens, enemy_tokens, free_tokens):
        possible_moves = []

        for my_token in my_tokens:
            for i in range(len(self.moves)):
                position = tuple(x + y for x, y in zip(my_token, self.moves[i]))

                if position in enemy_tokens:
                    while position in enemy_tokens:
                        position = tuple(x + y for x, y in zip(position, self.moves[i]))

                    if position in free_tokens:
                        possible_moves.append(position)

        return possible_moves
