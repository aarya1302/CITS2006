import getpass
import bcrypt


database = {"user1": "123456", "user2": "654321"}

new_database = {}

user = input("Enter username : ")
password = getpass.getpass("Enter password : ")

for user,password in database.items(): 
    new_database[user] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

found_user = False
# checking user and password entered 
for user_db,password_db in new_database.items():

    if (user == user_db):
        if (bcrypt.checkpw(password.encode("utf-8"), password_db)):
            found_user = True
            print("Authenticated")
            break
        while(not bcrypt.checkpw(password.encode("utf-8"), password_db)):
            password = getpass.getpass("Invalid Password, re-enter : ")
    
if (not found_user): 

    print("Cannot find user in database")
    

    
