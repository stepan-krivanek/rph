# Soft majo

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.num_of_defects = 0
        self.num_of_coops = 0
        return

    def move(self):
        move = False

        if self.num_of_coops < self.num_of_defects:
            move = True

        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        if opponent_last_move == True:
            self.num_of_defects += 1
        else:
            self.num_of_coops += 1
        return