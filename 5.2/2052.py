def getsq(n):
    s = f'{2 ** (-n):.250f}'
    index = 0
    for i in reversed(range(len(s))):
        if s[i] != '0':
            index = i
            break
    result = s[:index + 1]
    return result


N = int(input())
print(getsq(N))
