alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
use = [0] * 26
word = input().upper()

for i in range(26):
    use[i] = word.count(alp[i])

m = max(use)
if use.count(m) >= 2:
    print("?")
else:
    print(alp[use.index(m)])
