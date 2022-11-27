dot_X = int(input("Введите значение для точки X, не равное 0: "))
dot_Y = int(input("Введите значение для точки Y, не равное 0: "))

if dot_X > 0 and dot_Y > 0:
    print("Точка находится в плоскости I")
elif dot_X < 0 and dot_Y > 0:
    print("Точка находится в плоскости II")
elif dot_X < 0 and dot_Y < 0:
    print("Точка находится в плоскости III")
elif dot_X > 0 and dot_Y < 0:
    print("Точка находится в плоскости IV")
else:
    print("Ноль вводить нельзя!!!")