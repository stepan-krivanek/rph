# Slow tft

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.arr = [False, False]
        self.iteration = 0
        self.mov = False
        return

    def move(self):

        if self.arr.count(True) == 2:
            self.mov = True
        if self.arr.count(False) == 2:
            self.mov = False
        
        return self.mov # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.arr.pop(0)
        self.arr.append(opponent_last_move)
        return