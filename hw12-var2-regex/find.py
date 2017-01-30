import re
def text():
    f = open("portrait.txt","r",encoding="utf-8")
    a = f.read().split()
    m = []
    for n in a:
        b = n.lower().rstrip('.,<>/?""1234567890-=_+''[]{}()*&^%$#@!;:|\...')
        m.append(b)
    return m
def main():
    m = text()
    regex = 'на(й|ш(е|ё)?)(т|д|л)(ш|енн?)?(а?я?|(и|о|ы|(е|ё)|ую?)?(т|шь)?(ся)?(м(у|и)?|го|е|й|х)?)?'
    s = ''
    for i in m:
        res = re.search(regex,i)
        if res != None:
            k = 0
            for j in i:
                if j not in regex:
                    k += 1
            if k == 0:
                if i not in s:
                    s = s + i + ' '
    return s
print(main())
