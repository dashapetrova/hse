#задание 1
f=open("text1.txt","r",encoding = "utf-8")
for line in f:
    sym=line.split(" ")
    if sym[2]=="союз":
        print(line)
f.close()
