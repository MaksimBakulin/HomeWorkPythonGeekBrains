day = int(input("Введите номер дня недели: "))

if day > 0 and day < 6:
    print("Будний день")
elif day == 6 or day == 7:
    print("Выходной день")
else:
    print("Дня недели с таким номером не существует!!!")