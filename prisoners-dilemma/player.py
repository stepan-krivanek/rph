class MyPlayer:
    '''
    This player has a dictionary of 6 different main strategies.
    '''

    def __init__(self, payoff_matrix, number_of_iterations = None):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.iteration = 1
        self.strategy = "defector"

        # Initiates translator for strategies created by a secret formula
        # 1 and 0 represent whether a condition was fulfilled or not
        self.dictionary = {
            2000000: "repeater",
            2000001: "repeater", 
            2000011: "repeater",
            2000100: "defector",
            2000110: "defector",
            2000111: "defector",
            2001011: "cooperator",
            2001111: "defector",
            2010100: "defector",
            2010110: "defector",
            2011110: "defector",
            2011111: "defector",
            2100000: "hardTft",
            2100001: "cooperator",
            2101001: "cooperator",
            2101011: "cooperator",
            2110000: "cooperator",
            2110100: "mimicker",
            2111000: "cooperator",
            2111001: "cooperator",
            2111011: "cooperator",
            2111100: "slowTft",
            2111110: "slowTft",
            2111111: "slowTft"
            }
            
        # Memory inicialization, at most two enemy moves are important for any strategy
        self.my_last_move = True
        self.opponent_last_moves = [False, False]
        self.slowTft_move = False

        # Adapts the strategy according to the number of iterations
        if number_of_iterations == None or number_of_iterations > 7:
            self.choose_strategy()

    def move(self):
        # Performs the right move according to the strategy chosen
        # (Since there is no switch and the functions can't be executed from the dictionary, it might look quiet ugly)
        if self.strategy == "mimicker": next_move = self.opponent_last_moves[-1]
        elif self.strategy == "defector": next_move = True
        elif self.strategy == "cooperator": next_move = False
        elif self.strategy == "repeater": next_move = self.repeat()
        elif self.strategy == "hardTft": next_move = self.hardTft()
        elif self.strategy == "slowTft": next_move = self.slowTft()
        else: next_move = self.opponent_last_moves[-1]

        # Saves the correct own move (because of the noise)
        self.my_last_move = next_move

        # True(defect) or False(coop)
        return next_move

    def record_last_moves(self, my_last_move, opponent_last_move):
        # Saves opponent's last move, compares the own one and counts rounds
        self.opponent_last_moves.pop(0)

        if self.my_last_move != my_last_move:
            if opponent_last_move == True:
                opponent_last_move = False
            else:
                opponent_last_move = True

        self.opponent_last_moves.append(opponent_last_move)
        self.iteration += 1

    def choose_strategy(self):
        # Chooses the most appropriate strategy from the dictionary
        # according to six conditions comparing values in a symetric matrix
        key = [2,0,0,0,0,0,0]
        m = self.payoff_matrix

        cc = m[0][0][0]
        dd = m[1][1][1]
        cd = m[0][1][0]
        dc = m[0][1][1]  

        if cc > dd: key[1] = 1
        if cc > cd: key[2] = 1
        if cc > dc: key[3] = 1
        if dd > cd: key[4] = 1
        if dd > dc: key[5] = 1
        if cd > dc: key[6] = 1

        self.strategy = self.dictionary[int("".join(map(str, key)))]

    def repeat(self):
        # Periodically playing cooperator and defector
        if self.my_last_move == True:
            ret = False
        else:
            ret = True
        return ret

    def hardTft(self):
        # Cooperates the first two moves,
        # then defects if the opponent has defected exactly once of the two previous moves
        if self.iteration > 2 and self.opponent_last_moves.count(True) == 1:
            ret = True
        else:
            ret = False
        return ret

    def slowTft(self):
        # Cooperates the first two moves,
        # then begins to defect after two consecutive defections of the enemy
        # and begins to cooperate again after two consecutive cooperations of the enemy
        if self.iteration > 2:
            if self.opponent_last_moves.count(True) == 2:
                self.slowTft_move = True
            if self.opponent_last_moves.count(False) == 2:
                self.slowTft_move = False

        return self.slowTft_move

if __name__ == "__main__":
    print("I don't know what to do!")