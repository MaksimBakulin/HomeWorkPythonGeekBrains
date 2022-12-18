"""Задача - Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.

Старое решение
lst = [x for x in input().split(" ")]
new_list = []
i = 0

while i < len(lst):
    if lst.count(lst[i]) < 2:
        new_list.append(lst[i])
        i += 1
    else:
        i += 1

print(f"Список неповторяющихся элементов для списка {lst}: \n {new_list}")"""

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")