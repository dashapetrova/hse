import os
def main():
    num = 0
    for root, dirs, files in os.walk('.'):
        for d in dirs:
            k = 0
            for i in d:
                if i not in "йцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ":
                    k += 1
            if k == 0:
                num += 1
    return num
if __name__ == '__main__':
    print(main())    
