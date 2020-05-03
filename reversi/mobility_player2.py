import random
import copy

class MyPlayer:
    '''This Player plays randomly'''
    def __init__(self, my_color, opponent_color):
        self.name = 'krivast1'
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.size = 8
        self.board_size = self.size**2

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
        max_token_flips = self.size**4
        my_tokens, enemy_tokens, free_tokens = self.get_coords(board, self.my_color)
        my_possible_moves = self.get_possible_moves(my_tokens, enemy_tokens, free_tokens)
        evaluated_moves = []
        '''
        if len(free_tokens) < 7:
            depth = 5
        else:
            depth = 1
        '''        
        depth = 1
        for coords in my_possible_moves:
            new_board = self.swap_stones(board, coords, self.my_color, self.opponent_color)

            max_value = self.minimax(
                    new_board,
                    self.opponent_color,
                    self.my_color,
                    depth,
                    -max_token_flips,
                    max_token_flips,
                    False)

            value = max_value
            evaluated_moves.append(value)

        if my_possible_moves:
            return my_possible_moves[evaluated_moves.index(max(evaluated_moves))]
        else:
            return None

    def evaluate(self, board, own_color):
        my_tokens, enemy_tokens, free_tokens = self.get_coords(board, own_color)

        if len(free_tokens) < self.board_size/4:
            return len(my_tokens) - len(enemy_tokens)
        
        my_possible_moves = self.get_possible_moves(my_tokens, enemy_tokens, free_tokens)
        enemy_possible_moves = self.get_possible_moves(enemy_tokens, my_tokens, free_tokens)
        frontier_tokens = self.get_frontier_tokens(board, my_tokens, enemy_tokens, free_tokens)
        amount_of_neighbors = self.get_amount_of_neighbors(board, my_tokens, enemy_tokens, free_tokens)
        sum_of_neighbors = self.get_sum_of_neighbors(board, my_tokens, enemy_tokens, free_tokens)
        stable_tokens = self.get_stable_tokens(board)
        
        my_mobility = len(my_possible_moves)
        enemy_mobility = len(enemy_possible_moves)
        mobility = round(1000*(my_mobility-enemy_mobility)/(my_mobility+enemy_mobility+2))

        potential_mobility = frontier_tokens + amount_of_neighbors + sum_of_neighbors

        my_mobility = 0
        for move in my_possible_moves:
            my_mobility += self.eval_matrix[move[0]][move[1]]

        enemy_mobility = 0
        for move in enemy_possible_moves:
            enemy_mobility += self.eval_matrix[move[0]][move[1]]
        mobility = round(1000*(my_mobility-enemy_mobility)/(my_mobility+enemy_mobility+2))
        # my_mobility-enemy_mobility 1:1
        # mobility 2:0
        return mobility
        

    def get_stable_tokens(self, board):
        pass

    def get_frontier_tokens(self, board, my_tokens, enemy_tokens, free_tokens):
        # Counts the number of frontier tokens
        my_frontier_tokens = []
        enemy_frontier_tokens = []

        for token in free_tokens:
            for move in self.moves:
                position = tuple(x + y for x, y in zip(token, move))

                if position in my_tokens and position not in my_frontier_tokens:
                    my_frontier_tokens.append(position)
                elif position in enemy_tokens and position not in enemy_frontier_tokens:
                    enemy_frontier_tokens.append(position)

        return len(enemy_frontier_tokens) - len(my_frontier_tokens)

    def get_sum_of_neighbors(self, board, my_tokens, enemy_tokens, free_tokens):
        # Counts the sum of the number of empty squares
        # adjacent to opponent's tokens
        my_empty_neighbors = 0
        enemy_empty_neighbors = 0

        for token in free_tokens:
            for move in self.moves:
                position = tuple(x + y for x, y in zip(token, move))

                if position in my_tokens:
                    my_empty_neighbors += 1
                elif position in enemy_tokens:
                    enemy_empty_neighbors += 1

        return enemy_empty_neighbors - my_empty_neighbors

    def get_amount_of_neighbors(self, board, my_tokens, enemy_tokens, free_tokens):
        # Counts the number of empty squares, which neighbor
        # an opponent's token
        my_empty_neighbors = 0
        enemy_empty_neighbors = 0

        for token in free_tokens:
            my_token_found = False
            enemy_token_found = False

            for move in self.moves:
                position = tuple(x + y for x, y in zip(token, move))

                if position in my_tokens and my_token_found == False:
                    my_empty_neighbors += 1
                    my_token_found = True
                elif position in enemy_tokens and enemy_token_found == False:
                    enemy_empty_neighbors += 1
                    enemy_token_found = True

        return enemy_empty_neighbors - my_empty_neighbors


    def minimax(self, board, own_color, opponent_color, depth, alpha, beta, maximize):
        if depth == 0:
            evaluation = self.evaluate(board, own_color)    
            return evaluation
        
        my_tokens, enemy_tokens, free_tokens = self.get_coords(board, own_color)
        my_possible_moves = self.get_possible_moves(my_tokens, enemy_tokens, free_tokens)

        max_token_flips = self.size**4
        if maximize:
            max_value = -max_token_flips

            for coords in my_possible_moves:
                new_board = self.swap_stones(board, coords, own_color, opponent_color)
                max_tokens = self.minimax(new_board, opponent_color, own_color, depth - 1, alpha, beta, False)
                max_value = max(max_value, max_tokens)
                alpha = max(alpha, max_tokens)

                if beta <= alpha:
                    break
            return max_value
        else:
            min_value = max_token_flips

            for coords in my_possible_moves:
                new_board = self.swap_stones(board, coords, own_color, opponent_color)
                min_tokens = self.minimax(new_board, opponent_color, own_color, depth - 1, alpha, beta, True)
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
