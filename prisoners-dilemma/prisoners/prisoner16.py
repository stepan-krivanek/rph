# Generous tit for tat
import random

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.opponent_last_move = False

    def move(self):

        if self.opponent_last_move == True:
            if random.random() < 0.1:
                move = False
            else: move = True
        else:
            move = False

        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.opponent_last_move = opponent_last_move