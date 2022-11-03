# Дано: Строка со словами (str).
# Задание: напишите программу, которая проверяет есть ли в исходной строке три слова подряд.
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

def is_int(value):
    try:
        int(value)
        return True
    except:
        return False

def remove_special_symbols(value):
    special_symbols_list: list = "! @ # $ % ^ & * ( ) [ ] { } ; : , . / < > ? \ | ` ~ - = _ +".split(' ')
    result_value = str(value)

    for item in value:
        try:
            special_symbols_list.index(item)
            result_value = result_value.replace(item, "")
        except:
            pass

    return result_value

value: str = input('Введите сообщение: ')
value_without_special_symbols: str = remove_special_symbols(value)
value_list: list = value_without_special_symbols.split(' ')

condition_count: int = 0
for item in value_list:

    if item == '':
        continue

    item_is_int: bool = is_int(item)

    if(not item_is_int and condition_count != 3):
        condition_count += 1
        continue

    if(condition_count != 3):
        condition_count = 0

if(condition_count == 3):
    print("Результат: ", True)
else:
    print("Результат: ", False)
