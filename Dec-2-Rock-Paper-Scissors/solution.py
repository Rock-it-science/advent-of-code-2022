lines = []
with open('Dec-2-Rock-Paper-Scissors/input.txt', 'r') as f:
    lines = f.readlines()

total_score = 0

for line in lines:
    moves = line.split(' ')

    opp_move = moves[0]
    # Put opp_move on the same scale as my_move (X,Y,Z)
    if opp_move == 'A': opp_move = 'X'
    elif opp_move == 'B': opp_move = 'Y'
    elif opp_move == 'C': opp_move = 'Z'
    my_move = moves[1].removesuffix('\n')

    # Shape Score
    if my_move == 'X': # Rock
        total_score += 1
    elif my_move == 'Y': # Paper
        total_score += 2
    elif my_move == 'Z': # Scissors
        total_score += 3
    
    # Tie
    if my_move == opp_move:
        total_score += 3

    # Win
    elif (my_move == 'X' and opp_move == 'Z') or (my_move == 'Y' and opp_move == 'X') or (my_move == 'Z' and opp_move == 'Y'):
        total_score += 6

print(f'Total score is {total_score}')
