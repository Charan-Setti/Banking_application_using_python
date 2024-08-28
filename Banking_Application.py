import mysql.connector

# Establishing connection to MySQL database
mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='bank_application')
cursor = mydb.cursor()

class Reg:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.username = ""
        self.email = ""
        self.phone_number = ""
        self.password = ""

    def registration(self):
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.username = input("Enter a user name: ")
        self.email = input('Enter your Email id: ')
        self.phone_number = input('Enter your phone number: ')
        self.password = input('Enter your password: ')

        # Email and username validations
        if not self.email or '@' not in self.email or '.' not in self.email:
            print('Invalid email format')
            return
#         if '@' in self.username:
#             print('Username cannot contain "@"')
#             return
        
        # Password validation
        if not (6 <= len(self.password) <= 15):
            print('Password length should be between 6 and 15 characters')
            return
        if not any(char.isdigit() for char in self.password):
            print('Password should contain at least one digit')
            return
        if not any(char.isupper() for char in self.password):
            print('Password should contain at least one uppercase letter')
            return
        if not any(char.islower() for char in self.password):
            print('Password should contain at least one lowercase letter')
            return

        # Inserting data into database
        insert_query = 'INSERT INTO users (first_name, last_name, username, email, phone_number, password) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (self.first_name, self.last_name, self.username, self.email, self.phone_number, self.password)
        cursor.execute(insert_query, values)
        mydb.commit()

        print("Registration is Successful. Please proceed to Login")

    def login(self):
        self.username = input("Enter your login user name: ")
        self.password = input("Enter your Password: ")

        login_query = 'SELECT * FROM users WHERE username = %s AND password = %s'
        cursor.execute(login_query, (self.username, self.password))
        result = cursor.fetchone()

        if result:
            print(f"Login is Successful, Welcome {self.username} !")
        else:
            print("Username or password is incorrect")

    def fpass(self):
        self.username = input("Enter your Username : ")

        user_check_query = 'SELECT username FROM users WHERE username = %s'
        cursor.execute(user_check_query, (self.username,))
        res = cursor.fetchone()

        if res:
            self.update_pass = input("Enter your new password : ")
            self.confirm_update_pass = input("Confirm your new password : ")

            if self.update_pass == self.confirm_update_pass:
                update_pass_query = 'UPDATE users SET password = %s WHERE username = %s'
                cursor.execute(update_pass_query, (self.update_pass, self.username))
                mydb.commit()
                print("Password is Updated Successfully, please try to login once again")
            else:
                print("Passwords do not match")
        else:
            print("No such Username exists")

# Creating instance of Reg class
r1 = Reg()

# User interaction
while True:
    cases = int(input("Choose Your action: \n 1) Register \n 2) Login \n 3) Forgot Password \n 4) Exit \n"))

    if cases == 1:
        r1.registration()
    elif cases == 2:
        r1.login()
    elif cases == 3:
        r1.fpass()
    elif cases == 4:
        break
    else:
        print("Invalid choice")

# Closing cursor and database connection
cursor.close()
mydb.close()
