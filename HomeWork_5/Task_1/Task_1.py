txt = input("Введите текст: ")
incorrect_word = "абв"
new_text = [i for i in txt.split() if incorrect_word not in i]
print(f"Новый текст, без сочетаний '{incorrect_word}'")
print(*new_text)
