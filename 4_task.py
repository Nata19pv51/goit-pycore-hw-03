from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Get today date:
    today_date = datetime.today().date()
    # today_date = datetime(year=2025, month=10, day=14)
    
    # Determine what day of the year it is:
    today_number_day_of_year = today_date.timetuple().tm_yday

    upcoming_birthdays = []
    
    # Pass through users list and get every dictionary:
    for user in users:
        # Get birthday from every dictionary:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = birthday.replace(year=2025)
        # Determine what day of the year it is:
        birthday_number_day_of_year = birthday.timetuple().tm_yday
        
        congrat_dict = dict()
        
        # Determine if it is Monday today:
        if today_date.weekday() == 0:
            # Determine if the birthday was on Sunday (yesterday). It true -> congrate today:
            if birthday_number_day_of_year == (today_number_day_of_year - 1) or birthday_number_day_of_year == (today_number_day_of_year - 2):
                congrat_dict["name"] = user["name"]
                congrat_dict["congratulation_date"] = today_date.strftime("%Y-%m-%d")
                upcoming_birthdays.append(congrat_dict)
        
        # Determine who is birthday today or will celebrate the next 7 days. 
        # If there is so, it should be written to the upcoming_birthdays list:
        if (birthday_number_day_of_year >= today_number_day_of_year) and (birthday_number_day_of_year <= (today_number_day_of_year + 7)):
            if birthday.weekday() == 5:
                congrat_dict["name"] = user["name"]
                congrat_date = birthday + timedelta(days=2)
                congrat_dict["congratulation_date"] = congrat_date.strftime("%Y-%m-%d")
                upcoming_birthdays.append(congrat_dict)
            elif birthday.weekday() == 6:
                congrat_dict["name"] = user["name"]
                congrat_date = birthday + timedelta(days=1)
                congrat_dict["congratulation_date"] = congrat_date.strftime("%Y-%m-%d")
                upcoming_birthdays.append(congrat_dict)
            else:
                congrat_dict["name"] = user["name"]
                congrat_dict["congratulation_date"] = birthday.strftime("%Y-%m-%d") 
                upcoming_birthdays.append(congrat_dict)
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.12"},
    {"name": "Jane Smith", "birthday": "1990.10.15"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

if upcoming_birthdays:
    print("Список привітань на цьому тижні: ", upcoming_birthdays)
else:
    print("Список привітань на цьому тижні: відсутній")
