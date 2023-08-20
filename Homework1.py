# Задание 1.
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе
# и False в противном случае. Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.

import subprocess

def checkout(cmd, text):
    result = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

print(checkout('cat /home/user/tests/debian-binary', '2.0' ), )

# Задание 2. (повышенной сложности)
# Доработать функцию из предыдущего задания таким образом,
# чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.

import string

def checkout(cmd, text, flag):
    result = subprocess.run([cmd], shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if flag == '-sm':
        transTable = str.maketrans('','',string.punctuation)
        transTable1 = str.maketrans('','','—«»')
        resultText = result.stdout.translate(transTable).translate(transTable1).replace('  ',' ').strip().split(' ')
    else:
        resultText = result.stdout
    if text in resultText and result.returncode == 0:
        return True
    else:
        return False

print(checkout('cat /home/user/tests/mytext.txt', 'Шерер', '-sm'), )