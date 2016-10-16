a=int(input('input a number1: '))
b=int(input('input a number2: '))
c=int(input('input a number3: '))

print('\na=',a,'\nb=',b,'\nc=',c)

if a*b==c:
    print('\nПроизведение чисел a и b равно числу c')
else:
    print('\nПроизведение чисел a и b не равно c')

if a*c+b==0:
    print('Число c является решением линейного уравнения a*x+b=0')
else:
    print('Число c не является решением линейного уравнения a*x+b=0')

print('\nЧтобы завершить программу, нажмите Enter')
ENTER=input('')
