import random

# 10 клаассиков русской литературы и даты их рождения

lst_peoples = [['Достоевский Ф.М.', '11.11.1821', 'одинадцатого ноября 1821 года'], ['Пушкин А.С.', '06.06.1799', 'шестого июня 1799 года'],
               ['Лермонтов М.Ю.', '15.10.1814', 'пятнадцатого октября 1814 года'], ['Гоголь Н.В.', '01.04.1809', 'первого апреля 1808 года'],
               ['Толстой Л.Н.', '09.09.1828', 'девятого сентября 1828 года'], ['Чехов А.П.', '29.01.1860', 'двадцатьдевятого января 1860 года'],
               ['Тургенев И.С.', '09.11.1818', 'девятого ноября 1818 года'], ['Толстой А.Н.', '10.01.1883', 'десятого января 1883 года'],
               ['Некрасов Н.А.', '10.12.1821', 'десятого декабря 1821 года'], ['Грибоедов А.С.', '15.01.1795', 'пятнадцатого января 1795']]


def quiz(peoples):

    pers_choice = random.sample(peoples, 5)            # выбираем 5 случайных людей из списка
    l_names = [val[0] for val in pers_choice]           # берём только имена и заносим в список
    l_dates = [val[1] for val in pers_choice]           # берем даты и заносим в список
    str_dates = [val[2] for val in pers_choice]         # берем даты прописью и заносим в список

    correct_answer = 0               # счётчик верных ответов
    incorrect_answer = 0               # счётчик неверных ответов

    print(f"Введите дату рождения классиков {l_names} в формате 'дд.мм.гггг'.")

    for i in range(len(l_names)):
        user_response = input(f"{l_names[i]}, дата рождения: ")

        if user_response == l_dates[i]:
            print("Верно!")
            correct_answer += 1
        if user_response != l_dates[i]:
            print(f"Неверно! Правильный ответ: {str_dates[i]}")
            incorrect_answer += 1

    print("Процент правильных ответов:", correct_answer * 100 / 5)
    print("Процент неправильных ответов:", incorrect_answer * 100 / 5)
    print(input("Желаете сыграть ещё раз?"))


quiz(lst_peoples)




