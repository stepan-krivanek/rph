# Mem2

class MyPlayer:
    def __init__(self, payoff_matrix, number_of_iterations):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.iteration = 0
        self.first_round = []
        self.second_round = []
        self.strategy = 0
        self.opponent_last_move = -1
        return

    def move(self):
        if self.iteration == 0: move = False
        if self.iteration == 1: move = self.opponent_last_move

        if self.strategy == 1:
            move = self.opponent_last_move
        elif self.strategy == 2:
            if self.first_round[1] == True or self.second_round[1] == True:
                move = True
            else:
                move = False
        else:
            move = True
        
        return move # True(defect) or False(coop)
    
    def record_last_moves(self, my_last_move, opponent_last_move):
        if self.strategy != 4:
            if self.iteration % 2 == 0:
                self.first_round = [my_last_move, opponent_last_move]

            if self.iteration % 2 == 1:
                self.second_round = [my_last_move, opponent_last_move]
                self.change_strategy
            
            self.opponent_last_move = opponent_last_move
            self.iteration += 1
        return

    def change_strategy(self):
        if self.first_round == [False, False] and self.second_round == [False, False]:
            self.strategy = 1 # tft
        elif self.second_round == [False, True] or self.second_round == [True, False]:
            self.strategy = 2 # tf2t
        elif self.strategy == 3:
            self.strategy = 4  # infinite all_d
        else :
            self.strategy = 3  # all_d