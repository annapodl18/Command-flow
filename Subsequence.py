# Дано: Число N = [1-9].
# Задание: нужно написать программу, которая выведет последовательность 123..N

isInt: bool = False
value: int

while isInt == False:
    try:
        value = int(input('Введите целое число: '))

        if not value in range(1, 10):
            print('Введите значение от 1 до 9')
            raise ValueError()

        isInt = True

    except:
        print('Вы ввели не целочисленное значение...')

result = ''

for i in range(1, value + 1):
    result += str(i)

print('Результат:', result)