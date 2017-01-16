#вариант 2
def text():
    f = open("2.txt","r",encoding="utf-8")
    a = f.read().split()
    m = []
    for n in a:
        b = n.lower().rstrip('.,<>/?""1234567890-=_+''[]{}()*&^%$#@!;:|\...')
        m.append(b)
    return m
def ness(m):
    mas = []
    s = ""
    for i in m:
        if i[-4:] == 'ness':
            if i not in s:
                mas.append(i)             
            s = s + i + " "
    return mas    
def numb():
    m = text()
    mas = ness(m)
    return len(mas)
def main():
    m = text()
    b = ness(m)
    mas2 = []
    fr = ""
    s = ""
    for i in m:
        if i[-4:] == 'ness':             
            s = s + i + " " 
    for n in b:
        mas2.append(s.count(n))
    maxi = mas2[0]
    for j in mas2:
        if j > maxi:
            maxi = j
    for n in b:
        if s.count(n) == maxi:
            fr=fr+" "+n
    return fr
print("Количество разных слов на -ness =",numb(),"\nСамое(ые) частотное(ые) -",main())
