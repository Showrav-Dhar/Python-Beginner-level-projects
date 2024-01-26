# in this project we will work with python datetime package
def age_calculator(year, month, date):
    import datetime  # importing the datetime module inside the method is a good practice
    today = datetime.date.today()  # returns a date object for todays date
    date_of_birth = datetime.date(year, month, date)  # created a date object of the birthdate
    age = int((today - date_of_birth).days / 365.25)
    return age


# The expression (today - date_of_birth).days subtracts the birthdate from
# the current date and returns the difference as a number of days.
# The code divides the number of days by 365.25 (the average number of days in a year, considering leap years)
# and converts the result to an integer using int().

print("Enter Your Date Of Birth")

year = int(input("Enter Your Birth Year - "))
month = int(input("Enter Your Birth month - "))
day = int(input("Enter Your Birth day - "))
print(f"Your age is = {age_calculator(year, month, day)}")
