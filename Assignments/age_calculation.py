from datetime import date

month_dict = {
    1: True, 2: False, 3: True, 4: False, 5: True, 6: False, 7: True, 8: True, 9: False, 10: True, 11: False, 12: True
}

def calculate_age(dob):
    days_in_year = 365.2425
    age = int((date.today() - dob).days / days_in_year)
    return age

while True:
    year = int(input("Enter your year of birth"))
    if 1922 <= year < 2022:
        break
    print("enter carefully")

while True:
    month = int(input("Enter your month of birth"))
    if 1 <= month <= 12:
        break
    print("enter carefully")

while True:
    dates = int(input("Enter your date of birth"))
    if month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            if 0 < dates <= 29:
                break
        else:
            if 0 < dates <= 28:
                break
        print("enter carefully")


    else:
        if month_dict[month] == True and 0 < dates <= 31:
            break
        if month_dict[month] != True and 0 < dates <= 30:
            break
        print("enter carefully")

print(calculate_age(date(year, month, dates)), " years old")
