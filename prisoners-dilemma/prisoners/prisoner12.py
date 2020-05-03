# Tf2t

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.arr = [False, False]
        self.iteration = 0
        return

    def move(self):
        move = False

        if True in self.arr and self.iteration > 1:
            move = True
        
        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.arr.pop(0)
        self.arr.append(opponent_last_move)
        self.iteration += 1
        return