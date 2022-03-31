sen = input()
key = input()
len_key = len(key)

for i in range(len(sen)):
    if sen[i] == ' ':
        print(' ', end='')
    else:
        if ord(sen[i]) - ord(key[i%len_key]) <= 0:
            print(chr(ord(sen[i]) - ord(key[i%len_key]) + 26 + 96), end='')
        else :
            print(chr(ord(sen[i]) - ord(key[i%len_key]) + 96), end='')