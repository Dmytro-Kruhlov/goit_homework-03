import datetime
users = [
    {'name': 'Ivan', 'birthday': datetime.datetime(2023, 5, 29)},
    {'name': 'Dima', 'birthday': datetime.datetime(2023, 5, 30)},
    {'name': 'Pasha', 'birthday': datetime.datetime(2023, 5, 31)},
    {'name': 'Nikita', 'birthday': datetime.datetime(2023, 6, 1)},
    {'name': 'Oleg', 'birthday': datetime.datetime(2023, 6, 2)},
    {'name': 'Egor', 'birthday': datetime.datetime(2023, 6, 3)},
    {'name': 'ASd', 'birthday': datetime.datetime(2023, 6, 3)},
    {'name': 'Ysa', 'birthday': datetime.datetime(2023, 6, 3)},
    {'name': 'Vsya', 'birthday': datetime.datetime(2023, 6, 4)},
    {'name': 'Petya', 'birthday': datetime.datetime(2023, 6, 5)},
    {'name': 'Sanya', 'birthday': datetime.datetime(2023, 6, 6)},
    {'name': 'lexa', 'birthday': datetime.datetime(2023, 6, 7)},
    {'name': 'Natasha', 'birthday': datetime.datetime(2023, 6, 8)},
    {'name': 'Natasha', 'birthday': datetime.datetime(2023, 6, 9)},
    {'name': 'Natasha', 'birthday': datetime.datetime(2023, 6, 9)},
    {'name': 'Natasha', 'birthday': datetime.datetime(2023, 6, 12)},
    {'name': 'Natasha', 'birthday': datetime.datetime(2023, 6, 11)},
    {'name': 'Natasha', 'birthday': datetime.datetime(2023, 6, 10)},
]
today = datetime.datetime.today().date()
print(today)

nearest_saturday = today + datetime.timedelta(5 - today.weekday())
print(nearest_saturday)
friday_after_saturday = nearest_saturday + datetime.timedelta(days=6)
print(friday_after_saturday)

birthdays_this_week = {}

for user in users:
    name = user["name"]
    birthday = user["birthday"].date()
    
    if nearest_saturday <= birthday <= friday_after_saturday:
        if birthday.weekday() == 5:
            birthday += datetime.timedelta(days=2)
        if birthday.weekday() == 6:
            birthday += datetime.timedelta(days=1)
         
        if birthday not in birthdays_this_week:
         
            birthdays_this_week[birthday] = []
        birthdays_this_week[birthday].append(name)

for birthday, names in birthdays_this_week.items():
    weekday = birthday.strftime("%A")
    names_str = ", ".join(names)
    print(f"{weekday}: {names_str}")
