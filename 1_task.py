from datetime import datetime

def get_days_from_today(date):
    date_today = datetime.today()
    
    date = datetime.strptime(date, "%Y-%m-%d")
    
    total_seconds_in_day = 24 * 60 * 60
    
    delta = int((date_today - date).total_seconds() / total_seconds_in_day)
    
    return delta
    
data = input("Enter data in format YYYY-MM-DD: ")
print(get_days_from_today(data))