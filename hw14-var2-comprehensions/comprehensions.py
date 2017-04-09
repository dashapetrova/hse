import re
def lines():
    f = open('bk2.txt','r',encoding='utf-8')
    a = f.read()
    c = re.split(r'[.?!]',a)
    lines = [' '.join([word.strip('.,<>/?""-=_+''""[]{}()*&^%$#@!;:|\«»\n') for word in line.split()]).strip() for line in c]
    return lines    
def main():
    sents = lines()
    results=[]
    for line in sents:
        k=0
        words=line.split()
        k=['+' for w in words]
        if len(k)>10:
            for w in words:
                if w.istitle()==True:
                    results.append(w)
    return results
if __name__ == '__main__':
    print(main())
