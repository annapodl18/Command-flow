# Дано: Число x.
# Задание: нужно написать программу, которая дает оценку заданному значению, используя следующие правила.
# если x нечетное, то это "Плохо"
# если x = [2, 5] и четное, то это "Неплохо"
# если x = [6, 20] и четное, то это "Так себе"
# если x > 20 и четное, то это "Отлично"

isInt: bool = False
value: int

while isInt == False:
    try:
        value = int(input('Введите целое число: '))
        isInt = True
    except:
        print('Вы ввели не целочисленное значение...')


if value % 2 != 0:
    print('Плохо')
elif value % 2 == 0:
    if value in range(2, 6):
        print('Неплохо')
    elif value in range(6, 21):
        print('Так себе')
    elif value > 20:
        print('Отлично')


