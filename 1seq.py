# 1. Наиболее частые методы списка: append(x), sort(x), count(x), remove(x), insert(i, x).
# 2. Наиболее частые методы словаря: items(), popitem(), update(), keys(), values()
# 3. Наиболее частые методы множеств: add(x), remove(x), intersection(x), copy(x), pop(x)
# 4. Наиболее частые методы строк: format(*args, **kwargs) (либо f-строка), find(str, [start],[end]), lstrip([chars]), rstrip([chars]), strip([chars])



# Модуль 1


lst = []

x_el = int(input("Введите количество элементов: "))

for number in range(x_el):
    element = int(input(f"Введите элемент {(number + 1)}: "))
    lst.append(element)
    lst.sort()

print("Отсортированный список: ", lst)