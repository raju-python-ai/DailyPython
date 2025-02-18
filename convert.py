def convert_days(days):
    years = days // 365
    remaining_days = days % 365
    weeks = remaining_days // 7
    days = remaining_days % 7
    
    print(f"{years} years, {weeks} weeks, and {days} days")

num_days = int(input("Enter the number of days: "))
convert_days(num_days)
