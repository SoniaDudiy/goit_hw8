from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.now()

    # Визначаємо день тижня, з якого починається тиждень (понеділок)
    start_of_week = current_date - timedelta(days=current_date.weekday())

    # Визначаємо дату наступного понеділка
    next_monday = start_of_week + timedelta(weeks=1)

    # Створюємо словник, де ключ - це день тижня, а значення - список користувачів з іменинами в цей день
    birthdays_per_week = {i: [] for i in range(7)}

    # Перебираємо користувачів і додаємо їх у відповідний день тижня
    for user in users:
        name = user['name']
        birthday = user['birthday']

        # Якщо день народження припадає на вихідний, то виводимо привітання в понеділок
        if birthday.weekday() > 4:  # 5 і 6 представляють суботу та неділю
            birthdays_per_week[0].append(name)  # 0 представляє понеділок
        else:
            birthdays_per_week[birthday.weekday()].append(name)

    # Виводимо результат
    for day, names in birthdays_per_week.items():
        if names:
            day_name = next_monday + timedelta(days=day)
            print(f"{day_name.strftime('%A')}: {', '.join(names)}")

# Приклад 
users = [
    {'name': 'Bill', 'birthday': datetime(2023, 7, 29)},            # Субота
    {'name': 'Jill', 'birthday': datetime(2023, 7, 31)},            # Понеділок 
    {'name': 'Kim', 'birthday': datetime(2023, 8, 2)},              # Серада
    {'name': 'Jan', 'birthday': datetime(2023, 8, 6)},              # Неділя 
]

get_birthdays_per_week(users)

