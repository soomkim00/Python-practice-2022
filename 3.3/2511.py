Ascore = 0
Bscore = 0
lastWin = "D"

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(10):
    if A[i] > B[i]:
        Ascore += 3
        lastWin = "A"
    elif A[i] < B[i]:
        Bscore += 3
        lastWin = "B"
    else:
        Ascore += 1
        Bscore += 1

print(Ascore, Bscore)
if Ascore > Bscore:
    print("A")
elif Bscore > Ascore:
    print("B")
else:
    print(lastWin)