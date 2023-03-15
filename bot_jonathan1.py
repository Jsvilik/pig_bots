def choice(round_score, my_score, opponent_score):
    if my_score + round_score + 10 < opponent_score:
        if round_score > 20:
            return True
    if my_score + round_score + 15 < opponent_score:
        if round_score > 25:
            return true
    if my_score + round_score + 30 > opponent_score:
        return False
    if round_score + my_score > opponent_score:
        if round_score > 19:
            return False
