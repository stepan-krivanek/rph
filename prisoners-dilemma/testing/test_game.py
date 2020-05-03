# This script creates two (identical) players, 
# lets them play for some number of iterations and 
# then displays their scores. 
#
# For running this script, you need to put the 'game.py'
# as well as your 'player.py' to the python path, e.g. 
# to the the working directory. 
#
# A very simple testing script, feel free to modify it
# according to your needs
#
# example code for students of B4B33RPH course
# Author: Tomas Svoboda, and the RPH team

# Modification for multi prisoner score testing by Stepan Krivanek

from game import Game 
import random

# assuming your player is in player.py as required
# https://cw.fel.cvut.cz/wiki/courses/b4b33rph/cviceni/veznovo_dilema/specifikace
import prisoner1 # defector
import prisoner2 # cooperator
import prisoner3
import prisoner4
import prisoner5
import prisoner6
import prisoner7
import prisoner8
import prisoner9
import prisoner10
import prisoner11
import prisoner12
import prisoner13
import prisoner14
import prisoner15
import prisoner16
import prisoner17
import prisoner0
import player


# define the payoff matrix; see game.py for detailed explanation of this matrix
#payoff_matrix =(((4,4),(1,6)),
#              ((6,1),(2,2)))

            #  (((4,4),(1,6)),
            #   ((6,1),(2,2)))

# define the number of iterations
number_of_iterations = 100

# create the players
def play(payoff_matrix):
    p1 = prisoner1.MyPlayer(payoff_matrix, number_of_iterations)
    p2 = prisoner2.MyPlayer(payoff_matrix, number_of_iterations)
    p3 = prisoner3.MyPlayer(payoff_matrix, number_of_iterations)
    p4 = prisoner4.MyPlayer(payoff_matrix, number_of_iterations)
    p5 = prisoner5.MyPlayer(payoff_matrix, number_of_iterations)
    p6 = prisoner6.MyPlayer(payoff_matrix, number_of_iterations)
    p7 = prisoner7.MyPlayer(payoff_matrix, number_of_iterations)
    p8 = prisoner8.MyPlayer(payoff_matrix, number_of_iterations)
    p9 = prisoner9.MyPlayer(payoff_matrix, number_of_iterations)
    p10 = prisoner10.MyPlayer(payoff_matrix, number_of_iterations)
    p11 = prisoner11.MyPlayer(payoff_matrix, number_of_iterations)
    p12 = prisoner12.MyPlayer(payoff_matrix, number_of_iterations)
    p13 = prisoner13.MyPlayer(payoff_matrix, number_of_iterations)
    p14 = prisoner14.MyPlayer(payoff_matrix, number_of_iterations)
    p15 = prisoner15.MyPlayer(payoff_matrix, number_of_iterations)
    p16 = prisoner16.MyPlayer(payoff_matrix, number_of_iterations)
    p17 = prisoner17.MyPlayer(payoff_matrix, number_of_iterations)
    p0 = prisoner0.MyPlayer(payoff_matrix, number_of_iterations)
    pl = player.MyPlayer(payoff_matrix,number_of_iterations)

    list_of_players = [pl, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17]

    for i in range(50):
        list_of_players.append(prisoner1.MyPlayer(payoff_matrix, number_of_iterations))

    for i in range(102):
        list_of_players.append(prisoner3.MyPlayer(payoff_matrix, number_of_iterations))

    for i in range(30):
        list_of_players.append(prisoner12.MyPlayer(payoff_matrix, number_of_iterations))

    results = [0 for x in list_of_players]

    for x in list_of_players:
        indexX = list_of_players.index(x)

        for y in list_of_players:
            indexY = list_of_players.index(y)

            x.__init__(payoff_matrix, number_of_iterations)
            y.__init__(payoff_matrix, number_of_iterations)

            game = Game(x, y, payoff_matrix, number_of_iterations)
            game.run()

            result_A, result_B = game.get_players_payoffs()
            results[indexX] += result_A
            results[indexY] += result_B

    ret = 1
    for i in range(18):
        if results[i] > results[0]:
            ret += 1
    
    #print(results)
    print(results.index(max(results))+1)
    return ret

payoff_matrix = (((4, 4), (3, 10)), ((10, 3), (2, 2)))
print(play(payoff_matrix))

'''
def gen_num():
    return random.randrange(1, 100)

def create_matrix():
    a = gen_num()
    b = gen_num()
    c = gen_num()
    d = gen_num()
    return (((a,a),(c,d)),((d,c),(b,b)))


dictionary = {}
i = 0
attempt = 1
while i != 64:
    key = [2,0,0,0,0,0,0]
    s = str(format(i, '#08b'))
    wantedKey = int("2" + s[2:8])
    m = create_matrix()

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

    newKey = int("".join(map(str, key)))

    if attempt > 10000:
        print("still running")
        dictionary[wantedKey] = None
        attempt = 1
        i += 1
    if newKey != wantedKey:
        attempt += 1
        continue

    dictionary[newKey] = play(m)
    i += 1

print(dictionary)
'''

#for i in range(0, 18, 3):
#    print(str(results[i]) + ", " + str(results[i+1]) + ", " + str(results[i+2]) + ", ")
#print(results)
#print(results.index(max(results))+1)

# create the game instance
#game1 = Game(p1, p2, payoff_matrix, number_of_iterations)
# run game
#game1.run()

# get scores 
#scores = game1.get_players_payoffs()

# display scores
#print('playerA got:',scores[0], '\nplayerB got:', scores[1])
