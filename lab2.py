# Написать программу, которая читая файл, распознает, преобразует и выводит на экран числа по определенному правилу.
# Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь.
# Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
# Распознование делать через регулярные выражения. В вариантах, где есть параметр К, К заменяется на любое число.
# Вариант 11
# Натуральные числа. Выводит на экран четные числа, начинающиеся с цифры, введенной с клавиатуры.
# Каждое пятое число выводится прописью.
import re
dic = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
seq = open('txt1.txt','r').read()
print("Введите цифру 0-9, с которой начинаются числа в файле, которые нужно найти ")
k = input()
while not k.isdigit():
    print("Некорректное значение")
    k = input()
while int(k) > 9:
    print("Введено число, пожалуйста введите цифру 0-9")
    k = input()
counter = 1
nums = re.findall(r'[-+]?\d+', seq)
for i in nums:
    if i[0] == k:
        if int(i) % 2 == 0:
            if counter == 5:
                for j in i:
                    print(dic.get(int(j)), end=' ')
                counter = 1
                print(end='\n')
            else:
                print(i)
                counter += 1
