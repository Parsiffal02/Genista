while True:                                                                       #Проверка на дурака
    try:
        a = float(input('Введите катет a: '))
        b = float(input('Введите катет b: '))
        break
    except ValueError:
         print('Вы должны числа! Попробуйте снова!')
c = (a**2+b**2)**0.5
p = a + b + c
p1=p/2
s=(p1*(p1-a)*(p1-b)*(p1-c))**0.5
print('Площадь равна:', s)
print('Периметр равен:', p)
