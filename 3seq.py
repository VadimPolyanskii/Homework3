# Модуль 3

user_num1 = input("Введите элементы 1-го списка через запятую': ")
user_num2 = input("Введите элементы 2-го списка через запятую': ")

# Удаление из строк запятых и пробелов
numbers_str1 = user_num1.replace(",", " ").split()
numbers_str2 = user_num2.replace(",", " ").split()

# Преобразование каждого числа строк в целое число и помещение их в списки 1 и 2
lst1 = [int(num) for num in numbers_str1]
lst2 = [int(num) for num in numbers_str2]

print("Список 1: ", lst1)
print("Список 2: ", lst2)
print("-----------------------")

# Помещение эелементов 1-го списка, которых нет во 2-м, в новый список и вывод результата
res_lst = [i for i in lst1 if i not in lst2]
print("Результат: ", res_lst )



