def Palindrom():
    word = input('Введите слово: ')
    if word == word[::-1]:
        print('Это палиндром')
    else:
        print('Это не палиндром')
Palindrom()