a = ""
number = int(input("Введите число: "))
while number != 0:
    a = str(number % 2) + a
    number //=2
print(a)