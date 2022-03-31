N = int(input())

for i in range(N):
    score = 0
    Sum = 1
    result = input()
    result_l = list(result)
    for j in result_l:
        if j == 'O':
            score += Sum
            Sum += 1
        else:
            Sum = 1
    print(score)