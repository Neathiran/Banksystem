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


       
# def deposite_money():
#     global cheak 
#     global user_01
#     balance =user_01[2] 
#     newbalance = balance + cheak 
#     user_01.remove(balance)
#     user_01.insert(2,newbalance)
#     return user_01


    

#==Login==

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
                user_details[userid] = name,userpassword,balance
                print(user_details)

            elif choice ==2:
                user_01 = id_check()
                check = amount_check()   
                amount_01 = check
                user_02 = user_01
                def deposite_money(num,new):
                    balance =add[2] 
                    newbalance = balance +  num 
                    del add[2]
                    add.insert(2,newbalance)
                    print(add)
                    return add
                money = deposite_money(amount_01,user_02)
            elif choice ==3:
                print(user_details)    

        except ValueError:
            print("Choise must be on Numbers.")