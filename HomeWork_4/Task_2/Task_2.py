a = int(input("Введите число, которое необходимо разложить на простые множители: "))

i = 2
lst = []
start_number = a

while i <= a:
    if a % i == 0:
        lst.append(i)
        a /= i
        i = 2
    else:
        i += 1

if len(lst) < 2:
    print(f"Число {start_number} не имеет простых множителей, кроме самого себя и единицы")
else:
    print(f"Число {start_number} можно разложить на множители {lst}")