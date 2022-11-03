# Task_2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо и справа-налево.
# Иначе – False.

text = (input('Введите слово: ')).lower()
print(text)
def palindrom(x):
    if x[:] == x[::-1]:
        return True
    else:
        return False
print(palindrom(text))