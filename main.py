import datetime

users = [
    {'name': 'Ivan', 'birthday': datetime.datetime(2023, 5, 29)},
    {'name': 'Dima', 'birthday': datetime.datetime(2023, 5, 30)},
    {'name': 'Pasha', 'birthday': datetime.datetime(2023, 5, 31)},
    {'name': 'Nikita', 'birthday': datetime.datetime(2023, 6, 1)},
    {'name': 'Oleg', 'birthday': datetime.datetime(2023, 6, 2)},
    {'name': 'Egor', 'birthday': datetime.datetime(2023, 6, 3)},
    {'name': 'Vsya', 'birthday': datetime.datetime(2023, 6, 4)},
    {'name': 'Petya', 'birthday': datetime.datetime(2023, 6, 5)},
    {'name': 'Sanya', 'birthday': datetime.datetime(2023, 6, 6)},
    {'name': 'lexa', 'birthday': datetime.datetime(2023, 6, 7)},
    {'name': 'Natasha', 'birthday': datetime.datetime(2023, 5, 20)}
]


def get_birthdays_per_week(users):
    
    today = datetime.date.today()

    
    start_of_week = today - datetime.timedelta(days=today.weekday())

    
    birthdays_per_week = {}

    
    for user in users:
        name = user['name']
         
        birthday = user['birthday'].date()


