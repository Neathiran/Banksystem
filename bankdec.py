def date_time():
    import datetime
    x = datetime.datetime.now()
    return x
    

transaction = {}
admin ={}
user_details ={}
def get_account_id():
    import random
    import math
    num_01 = random.random()
    num_02 = num_01 * 1000000
    num_03 = math.floor(num_02)
    use = 'user' + str(num_03)
    return use


def get_password():
    import random
    import math
    num_01 = random.random()
    num_02 = num_01 * 10000
    num_03 = math.floor(num_02)
    if num_03 <1000:
        num_03 = num_03 + 1000
    return num_03

def amount_check():
    while True:
        try:
            amount = int(input('Enter Deposite Amount : '))
            if amount < 0:
                print('Amount will be > 0.')

            else:
                return amount
        except ValueError:
            print("Amount will be on Numbers")


def id_check():
     while True:
        try:
            user_id = input("Enter your user ID :")
            user_password =int(input("Enter the Password : "))
            key_list = []
            for key in user_details:
                key_list.append(key)
                print(key_list)
            if user_id in key_list:
                id_user = user_details.get(user_id)
                user = id_user
                if user[1] == user_password:
                    print(f"Welcom",user[0])
                    return user_id
                else:
                    print("Incorrect Password")
            else:
                print("Incorrect ID")        
        except ValueError:
            print("user ") 


       
def deposite_money_and_add_transaction():
    user_01 = id_check()
    check = amount_check() 
    change_01 = user_details.get(user_01)
    print(change_01)   
    balance = change_01[2]
    balance += check
    del change_01[2]
    change_01.insert(2,balance)
    user_details.pop(user_01)
    user_details[user_01] = change_01
    date_time_01 = date_time()
    transaction[user_01] = [date_time_01,check,balance]
    print(transaction)
    

# def add_transaction():
#     user_01 = id_check()
#     check = amount_check() 
#     money = deposite_money()
#     date_time_01 = date_time()
#     transaction[user_01] = [date_time_01,check,money]
#     print(transaction)

def add_to_file():
    for key,value in user_details.items():
        file = open('user_details.txt','a')
        file.write(f'{key},')
        for i in value:
            file.write(f'{i},')
        file.write('\n')
        file.close()
#====================LOGIN===============================

admin_id = "Admin"
admin_password = 1234
login = input("Enter Your User ID :")
password =int(input("Enter the Password : "))

if admin_id == login and admin_password == password:
    print("Admin Login")
    admin[login] = password
    while True:
        print("1. Create Account.")
        print("2. Deposite Money.")
        print("3. withdraw Money.")
        print("4. Transaction History.")
        print("5. Exit.")
        try:
            choice = int(input("Enter Your choise :"))
       
            if choice == 1:
                name = input("Enter the Username :")
                userid = get_account_id()
                userpassword = get_password()
                balance = amount_check()
                print(balance)
                print(userid)
                print(userpassword)
                details_01 = [name,userpassword,balance]
                user_details[userid] = details_01
                print(user_details)

            elif choice ==2:
                deposite_money_and_add_transaction()
                        
            elif choice ==3:
                print(user_details) 
            elif choice == 5:
                add_to_file()
        except ValueError:
            print("Choise must be on Numbers.")
            