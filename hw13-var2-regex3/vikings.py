import re
def main():
    s = ''
    f = open("Викинги.html","r",encoding="utf-8")
    for line in f:
        line = re.sub("в(и|и́)кинг(а(ми?|х)?|о(в|м)|у|е|и)?[^\w]","бурундук\\2",line)
        line = re.sub("В(и|и́)кинг(а(ми?|х)?|о(в|м)|у|е|и)?[^\w]","Бурундук\\2",line)
        s = s+line
    f.close()
    return s


def record():
    s = main()
    f = open("results.txt","w",encoding='utf-8')
    f.write(s)
    f.close()
record()
