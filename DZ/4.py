while True:                                                                       #Проверка на дурака
    try:
        n = int(input("Пожалуйста, введите колличество экспонатов: ")) 
        t = int(input("Пожалуйста, введите колличество полных лет: ")) 
        break
    except ValueError:
        print('Вы должны числа! Попробуйте снова!')
m=n*5
ch=m//60
d=ch//8
g=d//365
print('колличество лет:',g,'колличество дней:',d,'колличестсво часов:',ch,'колличество минут:',m)