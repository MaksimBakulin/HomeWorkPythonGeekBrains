def multiplication_list(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_list = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_list)

lst = [2, 3, 4, 5, 6]
multiplication_list(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
multiplication_list(lst)