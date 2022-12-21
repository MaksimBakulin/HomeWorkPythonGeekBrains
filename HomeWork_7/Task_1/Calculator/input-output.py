def Input():
    global a
    global b
    global c
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = input("Выберите действие (+ - / *): ")

def Output(a):
    print(f"Результат вычисления = {a}")