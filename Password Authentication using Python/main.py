# This system is used for the identification of a user.
# It is like a login screen that we see while logging in any website.
# It asks for  email or username and for password.
# after entering the correct password then it verifies you as the real user.

import getpass

# the following database is a dictionary which name is database
# here key is username and value is password
database = {"Sheldon_cooper": "Shelly@43#12",
            "Howard_Wolowitz": "GettingGirls@24/7",
            "just_penny": "cheeseCake@32",
            "Leonard_ner": "penny@love@23"}  # can add more

username = input("Enter Your UserName : ")
password = getpass.getpass("Enter your password : ")
# getpass.getpass() method shows dot display while entering the password in the terminal

for i in database.keys():
    if username == i:
        while password != database.get(i):  # dictionary_name.get(key) this return the value of the key
            print("Wrong Password")
            password = getpass.getpass("Try Again : ")
        break
print("Verified successfully")
