# Gradual

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.arr = []
        self.mov = False
        self.counter = 1
        self.opponent_last_move = -1
        return

    def move(self):
        mov = False

        if self.arr:
            mov = True
            self.arr.pop()
        
        return mov # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):

        if opponent_last_move == True:
            self.arr = [opponent_last_move] * self.counter
            self.counter += 1
        elif opponent_last_move == self.opponent_last_move:
            self.arr = []
            self.counter = 1

        self.opponent_last_move = opponent_last_move
        return