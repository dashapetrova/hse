import random
def words():
    f = open("1.csv","r",encoding="utf-8")
    a = f.read().split(',')
    m = []
    for n in a:
        b = n.rstrip('.,<>/?""1234567890-=_+''[]{}()*&^%$#@!;:|\...')
        m.append(b)
    return m
def d():
    m = words()
    d = {}
    for i in m:
        a = i.split()
        d[a[0]] = a[1]
    return d
def rand():
    m = words()
    di = d()
    mas = []
    for n in di.keys():
        mas.append(n)
    v = random.choice(mas)
    return v    
def attempt():
    di = d()
    v = rand()
    j = 0
    for i in di[v]:
        j += 1
    print(v,'.'*j)
    s = input()
    if s == di[v]:
        result = "you win"
    else:
        result = "you lose"
    return result
print(attempt()) 
