#задание 2
f=open("text1.txt","r",encoding = "utf-8")
s=0
for line in f:
    sym=line.split(" ")
    if sym[4]=="ед" and sym[5]=="жен":
        print(sym[0]+",")
        s=s+float(sym[-1])
print(s)
f.close()
