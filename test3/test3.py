import os
import re


def texts(name):
    f = open(name, 'r')
    text = f.read()
    x = re.findall('<w>.+</w>', text)
    f.close()
    return x


def resutls(s,filename):
    f = open(filename,"w+",encoding = "utf-8")
    f.write(s)
    f.close()

    
def words():
    s = ""
    for roots, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.xhtml'):
                s = s + file + "\t"+ str(len(texts(os.path.join(roots,file)))) + "\n"
    results(s,"result1.txt")


if __name__ == '__words__':
    words()
