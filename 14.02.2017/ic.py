import re
def opp():
    k = 0
    f = open("it.xml","r",encoding="utf-8")
    for line in f:
        k += 1
    f.close()
    return k


def record1():
    f = open('result1.txt','w',encoding='utf-8')
    f.write(str(opp()))
    f.close()
record1()


def dic():
    d = {}
    regex1 = 'lemma="'
    regex2 = 'type="[a-zþ0-9]+"'
    f = open("it.xml","r",encoding="utf-8")
    for line in f:
        if re.search(regex1,line) != None:
            res = re.search(regex2,line)
            if res != None:
                p1 = line.rfind('"')
                p2 = line.find('type=')
                s = line[p2+6:p1]
                if s in d.keys():
                    d[s] += 1
                else:
                    d[s] = 1
    return d


def record2():
    d = dic()
    f = open('result1.txt','a',encoding='utf-8')
    for i in d.keys():
        f.write('\n'+i)
    f.close()
record2()


def plur():
    d = {}
    regex1 = 'lemma="'
    regex2 = 'type="[a-zþ0-9]+"'
    f = open("it.xml","r",encoding="utf-8")
    for line in f:
        if re.search(regex1,line) != None:
            res = re.search(regex2,line)
            if res != None:
                p1 = line.rfind('"')
                p2 = line.find('type=')
                s = line[p2+6:p1]
                if s[0] == 'l' and s[2] == 'f':
                    if s in d.keys():
                        d[s] += 1
                    else:
                        d[s] = 1
    return d


def record3():
    d = plur()
    f = open('result2','w',encoding='utf-8')
    for i in d.keys():
        f.write(i+' - '+str(d[i])+'\n')
    f.close()
record3()
