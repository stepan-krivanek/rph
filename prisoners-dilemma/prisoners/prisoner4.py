# Grim, spiteful

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.spiteful = False
        return

    def move(self):
        move = self.spiteful
        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        if opponent_last_move == True:
            self.spiteful = True
        return