plane_number = int(input("Введите номер четверти плоскости (от 1 до 4) "))

if plane_number == 1:
    print("Возможные координаты точек: (X > 0; Y > 0)")
elif plane_number == 2:
    print("Возможные координаты точек: (X < 0; Y > 0)")
elif plane_number == 3:
    print("Возможные координаты точек: (X < 0; Y < 0)")
elif plane_number == 2:
    print("Возможные координаты точек: (X > 0; Y < 0)")
else:
    print("Вы ввели число вне указанного диапазона!!!")