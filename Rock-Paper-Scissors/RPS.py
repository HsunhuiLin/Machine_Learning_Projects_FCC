# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):

    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    # first guess
    guess = "R"
    prev_n = ""
    prev_n += prev_play

    n = 3

    if len(opponent_history) > n:
        prev_n = ''.join(opponent_history[-n:])
    
    if ''.join(opponent_history[-(n+1):]) in play_order.keys():
        play_order[''.join(opponent_history[-(n+1):])] += 1
    else:
        play_order[''.join(opponent_history[-(n+1):])] = 1

    
    possible = [
        prev_n+'R',
        prev_n+'P',
        prev_n+'S'
    ]
    
    # Setting possible combination as keys if not already in the dict
    for i in possible:
        if i not in play_order.keys():
            play_order[i] = 0 

    # highest possible combination in the next round
    pred = max(possible, key = lambda x: play_order[x])[-1]
    
    response = {'P': 'S', 'S': 'R', 'R': 'P'}
    guess = response[pred]

    return guess
