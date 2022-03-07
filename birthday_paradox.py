import datetime
import random


def get_birthdays(num_of_birthdays):
    birthdays = []

    for i in num_of_birthdays:
        start_year = datetime.date(2000,1,1)

        random_day = datetime.timedelta(random.randint(0,365))
        birthday = start_year + random_day
        birthdays.append(birthday)

    return birthdays




if __name__ == "__main__":
    pass