# Дано: Дан кусок текста (str).
# Задание: Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.

text: str = input('Введите текст: ')

def capital_letters(text):
    result: str = ''
    for i in text:
        if i.isupper() == True:
            result += i
    print(result)

capital_letters(text)