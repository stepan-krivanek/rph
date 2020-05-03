# Random
import random

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.my_moves = []
        self.opponent_moves = []
        return

    def move(self):
        move = True
        opponent_moves = self.opponent_moves

        if len(opponent_moves) > 0:
            true = self.get_latest_coop()

            if opponent_moves[-1] == False:
                if true < 2: move = False

        move = random.choice([True, False])
        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.my_moves.append(my_last_move)
        self.opponent_moves.append(opponent_last_move)
        return

    def get_latest_coop(self):
        true = 0

        for bit in self.opponent_moves[-5:]:
            if bit == True: true += 1

        return true