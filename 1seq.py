# Модуль 1


lst = []

x_el = int(input("Введите количество элементов: "))

for number in range(x_el):
    element = int(input(f"Введите элемент {(number + 1)}: "))
    lst.append(element)
    lst.sort()

print("Отсортированный список: ", lst)