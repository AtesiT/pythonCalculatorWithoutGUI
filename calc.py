def calc():
    while True:
        the_sign = input('Что вы хотите сделать? Сложение, Вычитание, Умножение, Деление, Выход. ')
        first_number = int(input('Введите первое целое число: '))
        second_number = int(input('Введите второе целое число: '))

        if the_sign == 'сложение':
            return_number = 'Выполнена операция сложения: ', first_number + second_number
        elif the_sign == 'вычитание':
            return_number = 'Выполнена операция вычитания: ', first_number - second_number
        elif the_sign == 'умножение':
            return_number = 'Выполнена операция умножения: ', first_number * second_number
        elif the_sign == 'деление':
            return_number = 'Выполнена операция деления: ', first_number / second_number
        elif the_sign == 'выход':
            print('Вы вышли из калькулятора')
            quit()
        else:
            print('Вы ошиблись в написании')
            continue
        print(return_number)
    


calc()