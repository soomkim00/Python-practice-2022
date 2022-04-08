def makeoct(n):
    return oct(int(n, 2))


a = input()
print(makeoct(a)[2:])
