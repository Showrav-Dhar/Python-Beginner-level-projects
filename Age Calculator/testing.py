def age_cal(year, month, date):
    import datetime
    today = datetime.date.today()
    dob = datetime.date(year, month, date)
    age = int((today - dob).days / 365.25)
    return age


print(f"Age = {age_cal(2000, 10, 24)}")
