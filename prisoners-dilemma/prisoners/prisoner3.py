# Tit for tat

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.my_moves = []
        self.opponent_moves = []
        return

    def move(self):
        move = False
        opponent_moves = self.opponent_moves

        if len(opponent_moves) > 0:
            move = self.opponent_moves[-1]

        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.opponent_moves.append(opponent_last_move)
        return