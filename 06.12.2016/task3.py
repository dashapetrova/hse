#задание 3
f=open("text1.txt","r",encoding = "utf-8")
s = input("Введите слово: ")
m = []
while s!='':
    m.append(s)
    s=input("Введите слово: ")
for i in m:
    for line in f:
        sym = line.split(" ")
        if i == sym[0]:
            print(i,sym[1:])
        else:
            print(i+" - в словаре нет такого слова")
            break
f.close()
