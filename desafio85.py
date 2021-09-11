tudo = [[], []]


for n in range(0,7):
    v =  int(input(f'Digite  o {n+1}* número'))
    if v%2 ==0:
        tudo[0].append(v)
    else:
        tudo[1].append(v)

tudo[0].sort()
tudo[1].sort()
print(tudo)