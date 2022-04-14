def cal_score(shooting_result):
    sr = list(shooting_result)
    score = 0
    hit = 0
    for i in range(len(sr)):
        if sr[i] == 'h':
            hit += 1
            score += hit
        else:
            score -= 1
            hit = 0
    return score


result = input()
print(cal_score(result))
