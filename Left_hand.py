# Дано: последовательность строк.
#
# Задание: вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
# В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left",
# даже если это часть другого слова. Все строки даны в нижнем регистре.

right: str = "right"
left: str = "left"

def is_exist_left(value):
    try:
        value.index(left)
        return True
    except:
        return False

def is_exist_right(value):
    try:
        value.index(right)
        return True
    except:
        return False

value_list: list = ["left", "right", "left", "stop", "bright aright", "ok", "enough", "jokes"]

result: str = ''
for value in value_list:
    if(is_exist_right(value)):
        value = value.replace(right, left)
        result += value + ","
    elif(is_exist_left(value)):
        value = value.replace(left, right)
        result += value + ","
    else:
        result += value + ","

print("Результат: ", result[:-1])

