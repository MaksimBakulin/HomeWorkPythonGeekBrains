dot_A_X = float(input("Введите значение по оси Х для точки А: "))
dot_A_Y = float(input("Введите значение по оси Y для точки А: "))
dot_B_X = float(input("Введите значение по оси Х для точки B: "))
dot_B_Y = float(input("Введите значение по оси Y для точки B: "))

result = (((dot_B_X - dot_A_X) ** 2) + ((dot_B_Y - dot_A_Y) ** 2)) ** 0.5
print(round(result, 2))