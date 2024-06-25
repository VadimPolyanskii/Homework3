
lst = []

x_el = int(input("Введите количество элементов: "))

for number in range(x_el):
    element = int(input(f"Введите элемент {number}: "))
    lst.append(element)
    lst.sort()

print(lst)