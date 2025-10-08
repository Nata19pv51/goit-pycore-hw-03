from datetime import datetime

def get_days_from_today(date):
    # Get today date
    date_today = datetime.today()
    
    # Convert string into datetime according to the format %Y-%m-%d:
    date = datetime.strptime(date, "%Y-%m-%d")
    
    total_seconds_in_day = 24 * 60 * 60
   
    # Transform seconds to days 
    delta = int((date_today - date).total_seconds() / total_seconds_in_day)
    
    return abs(delta)

# Ask the user to enter the date:
data = input("Enter date in format YYYY-MM-DD: ")
print(get_days_from_today(data))