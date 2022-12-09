lst = [x for x in input().split(" ")]
new_list = []
i = 0

while i < len(lst):
    if lst.count(lst[i]) < 2:
        new_list.append(lst[i])
        i += 1
    else:
        i += 1

print(f"Список неповторяющихся элементов для списка {lst}: \n {new_list}")