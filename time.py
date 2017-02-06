import re
def text():
    a=[]
    f = open("Санкт-Петербург.html","r",encoding="utf-8")
    for line in f:
        a.append(line)
    return a
def main():
    a=text()
    s=''
    p1 = int; p2 = int
    regex = '"[A-Z][A-Z][A-Z](\+|-)?[0-9][0-9]?:?[0-90-9]?"'
    for line in a:
        b=line.split()
        for i in b:
            res = re.search(regex,i)
            if res != None:
                p1 = i.find('>')
                p2 = i.find('<')
                s=i[p1+1:p2]
    return s
def record():
    s=main()
    f = open("result.txt","w")
    f.write("Часовой пояс - "+s)
    f.close()
record()
