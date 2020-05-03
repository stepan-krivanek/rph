# Per ccd

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.movement = [False, False, True]
        self.x = 0
        return

    def move(self):
        move = self.movement[self.x]

        if self.x == 2:
            self.x = 0
        else:
            self.x += 1
        
        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        return