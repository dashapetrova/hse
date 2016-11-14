#2-ой вариант
m=[]
s=input('введите слово: ')
while s!='':
    m.append(s)
    s=input('введите слово: ')
for word in m:
    if len(word)>5:
        print(word)
print('Чтобы завершить программу, нажмите ENTER')
ENTER=input('')
