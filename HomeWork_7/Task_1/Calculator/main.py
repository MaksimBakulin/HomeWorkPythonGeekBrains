import input_output as io
import calculation_logic_rational_numbers as calc
import calculation_logic_complex_numbers as calc_cplx


choice_functional = input("Для каких чисел выполнить вычисление? (1 - рациональные, 2 - комплексные): ")

if choice_functional == "1":
    a, b, c = 0, 0, 0

    a = int(io.Input(a, "первое значение"))
    b = int(io.Input(b, "второе значение"))
    c = io.Input(c, "действие (+ - * /)")

    if c == "+":
        calc.Sum(a, b)
    elif c == "-":
        calc.Subtraction(a, b)
    elif c == "*":
        calc.Multiplication(a, b)
    elif c == "/":
        calc.Division(a, b)
    else:
        print("Введено некорректное действие")

elif choice_functional == "2":
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

    print("Теперь введите необходимые значения переменных. Пример: для вычисления выражения (5+2х) + (3-6х)\n"
          "необходимо было бы задать следующие переменные:\n"
          "Числовое значение первой переменной - 5\n"
          "Числовое значение второй переменной - 2\n"
          "Числовое значение третьей переменной - 3\n"
          "Числовое значение четвертой переменной - 6\n"
          "Буквенное значение - х\n"
          "Выполняемое действие - +")

    a = int(io.Input(a, "числовое значение первой переменной"))
    b = int(io.Input(b, "числовое значение второй переменной"))
    c = int(io.Input(b, "числовое значение третьей переменной"))
    d = int(io.Input(b, "числовое значение четвертой переменной"))
    e = io.Input(e, "буквенное значение")
    f = io.Input(f, "выполняемое действие")

    if f == "+":
        calc_cplx.Sum(a, b, c, d, e)
    elif f == "-":
        calc_cplx.Subtraction(a, b, c, d, e)
    elif f == "*":
        calc_cplx.Multiplication(a, b, c, d, e)
    elif f == "/":
        calc_cplx.Division(a, b, c, d, e)
    else:
        print("Введено некорректное действие")

else:
    print("Необходимо было ввести 1 или 2!!!")