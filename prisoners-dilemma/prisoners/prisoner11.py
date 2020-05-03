# Pavlov

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.my_last_move = False
        self.opponent_last_move = False
        return

    def move(self):
        move = False

        if self.my_last_move != self.opponent_last_move:
            move = True
        
        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.my_last_move = my_last_move
        self.opponent_last_move = opponent_last_move
        return