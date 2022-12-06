lst = list(map(float, input("Введите последовательность чисел:\n").split()))
new_list = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(new_list) - min(new_list))