def Input():
    global a
    global b
    global c
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = input("Выберите действие (+ - / *): ")
    print(f"Будет вычислен результат выражения {a} {c} {b}")

def Output(a):
    print(f"Результат вычисления = {a}")