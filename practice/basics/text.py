def read_all(filename):
    """Вернуть содержимое текстового файла filename как строку."""
    filename = open(filename, 'r')
    a = filename.read()
    return a

def sum_two(filename):
    """Прочитать первые два числа из текстового файла и вернуть их сумму."""
    f = open(filename, 'r')
    a = f.read()
    s = a.split()
    return int(s[0]) + int(s[1])



def longest_line(filename):
    """Вернуть номер самой длинной строки текстового файла. Нумерация начинается с единицы."""
    s = []
    with open(filename, 'r') as f:
        for s_line in f:
            i = len(s_line)
            s.append(i)
    if s == []:
        return 1
    max_line = max(s)
    for i in range(0,len(s)):
        if s[i] == max_line:
            return i + 1



def random_access(filename, n):
    """Вернуть n-ый символ текстового файла. Нумерация с единицы"""
    f = open(filename, 'r')
    a = f.read()
    if n <= 0 or n > len(a):
        return ''
    else:
        return a[n - 1]


def alphabet(filename, n):
    """Вывести n первых заглавных букв латинского алфавита в текстовый файл."""
    f = open(filename, 'w+')
    a = f.read()
    for i in range(65, 65 + n):
        a = f.write(str(chr(i)))
    return a


