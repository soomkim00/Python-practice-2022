N = int(input())
gw = 0
for _ in range(N):
    word = input()
    err = 0
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            n_word = word[i + 1:]
            if n_word.count(word[i]) > 0:
                err += 1
    if err == 0:
        gw += 1
print(gw)
