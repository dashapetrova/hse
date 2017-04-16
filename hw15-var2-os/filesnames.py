def names():
    import os
    m = os.listdir('.')
    return m
def main():
    m = names()
    newm = []
    num = 0
    for i in m:
        k = 0
        for j in i:
            if j in '1234567890':
                k += 1
        if k == 0:
            num += 1
            if '.' in i:
                i = i[:i.index('.')]
            if i not in newm:
                newm.append(i)
    print('num = {}'.format(num))
    print(newm)          
if __name__ == '__main__':
    main()
