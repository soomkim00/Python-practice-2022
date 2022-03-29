Ex = int(input())
Won = int(input())

Eu = int(Won/Ex)

if Eu < 1000:
    Eu -= 1

print(Eu//100, Eu%100//50, Eu%100%50//10, Eu%10)