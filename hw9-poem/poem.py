#стихотворение на русском языке из четырёх строк без рифмы: трехстопный дактиль
import random

def phrase():
    f0 = open("plus1.txt","r",encoding="utf-8")
    pr1 = f0.read().split()
    p1 = random.choice(pr1)
    f1 = open("plus2.txt","r",encoding="utf-8")
    pr2 = f1.read().split()
    p2 = random.choice(pr2)
    return p1 + ' ' + p2

def adjective():
    f2 = open("adj.txt","r",encoding="utf-8")
    adj = f2.read().split()
    return random.choice(adj)

def verb():
    f3 = open("verb.txt","r",encoding="utf-8")
    v = f3.read().split()
    return random.choice(v)

def noun(num):
    f4 = open("sg.txt","r",encoding="utf-8")
    nounsg = f4.read().split()
    f5 = open("pl.txt","r",encoding="utf-8")
    nounpl = f5.read().split()
    f6 = open("ind.txt","r",encoding="utf-8")
    nounind = f6.read().split()
    if num == 'pl':
        return random.choice(nounpl)
    if num == 'ind':
        return random.choice(nounind)
    return random.choice(nounsg)

def punctuation():
    puncts = [".", "?", "!", "...",";"]
    return random.choice(puncts)

def verse1():
    return phrase() + ' ' + noun("sg") + ' ' + noun("pl") + punctuation()

def verse2():
    return verb() + ', ' + verb() + ' ' + noun("ind") + punctuation()

def verse3():
    return noun("sg") + ' ' + adjective() + ' ' + noun("pl") + punctuation()

def doit():
    verse = random.choice([1,2,3])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    else:
        return verse3()

for n in range(4):
    print(doit())
