from datetime import datetime, date, timedelta

def days_between(start_date, end_date):
    return (end_date - start_date).days

date1 = date(2023, 5, 1)
date2 = date(2023, 5, 15)

print("Date Demonstration:")
print(f"Date1: {date1}")
print(f"Date2: {date2}")
print(f"Difference in days: {days_between(date1, date2)} days")

datetime1 = datetime(2023, 5, 1, 14, 30)
datetime2 = datetime(2023, 5, 15, 9, 0)

print("\nDatetime Demonstration:")
print(f"Datetime1: {datetime1}")
print(f"Datetime2: {datetime2}")
print(f"Difference in days (ignoring time): {days_between(datetime1.date(), datetime2.date())} days")

print("\nAdditional Date-Time Operations:")

now = datetime.now()
print(f"Current Date and Time: {now}")

formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date and Time: {formatted_datetime}")

future_date = date1 + timedelta(days=10)
print(f"Future Date (10 days later): {future_date}")

past_date = date2 - timedelta(days=5)
print(f"Past Date (5 days before): {past_date}")

specific_time = datetime(2023, 5, 1, 14, 0)
print("\nComparing times:")
if now > specific_time:
    print("Current time is after the specific time.")
else:
    print("Current time is before the specific time.")