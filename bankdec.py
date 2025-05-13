
user_admin_detail = {}
user_id =[]
admin_id = []
user_balance ={}

#========================LOGIN FUCTION=====================================


def read_admin():
    global user_admin_detail
    global admin_id
    with open('admin_details.txt','r') as file:
        lines = file.readlines()

    for line in lines:
        admin =line.strip('\n').split(',')
        user_admin_detail[admin[0]] = admin[1]
        admin_id.append(admin[0])

def read_user():
    global user_admin_detail
    global user_id
    with open('users_details.txt','r') as file:
        lines = file.readlines()

    for line in lines:
        user =line.strip('\n').split(',')
        user_admin_detail[user[0]] = user[1]
        user_id.append(user[0])




def login():
    with open('admin_details.txt','a') as file:
                file.write('admin,1234,\n')

    with open('users_details.txt','a') as file:
        file.write('00000000,00000,00000000,000000,\n')
    global  user_admin_detail
    global  user_id 
    global admin_id
    global user_balance
    while True:
        login_id = input('Enter the ID : ')
        password = input('Enter password : ')
        login_id = login_id.strip().lower()
        password = password.strip().lower()
        user_balance['user'] = 1234
        if login_id =='admin' and password == '1234':
            with open('user_balance.txt','a') as file:
                file.write(f'00000,1234')
                return 1,3,login_id,password

        else:
            read_admin()
            if login_id in admin_id:
                admin_password =user_admin_detail.get(login_id)
                if admin_password == password:
                    user_id.clear()
                    user_admin_detail.clear()
                    admin_id.clear()    
                    return 1,login_id,password
                else:
                    print('Incorrct Password ')

            else:
                read_user()            
                if login_id in user_id:
                    user_password = user_admin_detail.get(login_id)
                    if user_password == password:
                        user_id.clear()
                        user_admin_detail.clear()
                        admin_id.clear()
                        return 2,login_id,password
                    else:
                        print('Incorrct Password ')
                else:
                    print('Incorrct ID')


#===================================================================

#========================GENERATE_DATE_TIME=========================

def date_time():
    import datetime 
    x = datetime.datetime.now()
    time = x.strftime("%Y-%m-%d %H:%M:%S")
    return time

#=====================GENERATE_USER_ID_PASSWORD=====================


def get_account_id():
    import random
    import math
    num_01 = random.random()
    num_02 = num_01*1000000
    num_03 = math.floor(num_02)
    use = 'user' + str(num_03)
    return use


def get_password():
    import random
    import math
    num_01 = random.random()
    num_02 = num_01*1000
    num_03 = math.floor(num_02)
    if num_03 <1000:
        num_03 = num_03 + 1000
    return num_03

#===================================================================

#====================CHECK_NIC_NUMBER==============================

def check_new_NIC_number(): 
        while True:
                try:
                    NIC_number = (input("Enter your NIC number : "))
                    check_nic = open('users_details.txt','r')
                    read = check_nic.readlines()
                    check_nic.close()
                    for nic in read:
                        split_word =nic.split(',')
                        if split_word[2] == (NIC_number.strip()):
                            print(" Invaild NIC Number Try again.")
                            break
                    else:
                        return NIC_number
                except ValueError:
                        print("NIC must be in Numbers. ") 

#==================================================================

#==============================CREATE_USER===================================

user_balance ={}
def collect_user_details():
    global user_balance
    name = input("Enter the Username : ")
    nic_num = check_new_NIC_number()
    userid = get_account_id()
    userpassword = get_password()
    balance = deposit_amount_check()
    print(balance)
    print(userid)
    print(userpassword)
    with open('users_details.txt','a') as add_user_details: 
        add_user_details.write(f'{userid},{userpassword},{nic_num.strip()},{name.strip()},\n')
    user_balance[userid] = balance
    transaction_withdraw_deposite(userid,balance)
    write_user_balance()
    write_user_balance_dec()

#===============================================================================

#========================CHECK_AMOUNT==============================


def deposit_amount_check():
    while True:
        try:
            amount = float(input('Enter Deposite Amount : '))
            if amount < 0:
                print('Amount will be > 0.')

            else:
                return amount
        except ValueError:
            print("Amount will be on Numbers")

def withdraw_amount_check(user_id):
    global user_balance
    while True:
        try:
            amount = float(input('Enter Withdraw Amount : '))
            if amount < 0:
                print('Amount will be > 0.')
               
            else:
                balance = float(user_balance.get(user_id[0]))
                if balance < amount:
                    print(f'Your Account Balance : {balance} ')
                else :
                    return amount                  
        except ValueError:
            print("Amount will be on Numbers")

#==================================================================

#=======================ADD_ADMIN==========================

def add_admin_id():
    new_admin = input('Enter Admin ID : ')
    new_password = input('Enter Password : ')
    with open('admin_details.txt','a') as file:
        file.write(f'{new_admin.lower().strip()},{new_password.strip()},\n')

#==========================================================

#===================CHECK_ID_PASSWORD======================
def check_id():
        while True:
                user_id = (input("Enter your user ID : "))
                check_id = open('users_details.txt','r')
                read = check_id.readlines()
                check_id.close()
                for id in read:
                    split_word =id.strip('\n').split(',')
                    if split_word[0] == user_id:
                         return split_word    
                else:
                    print("Incorrct User ID")
    

def check_id_password():
    detail = check_id()
    while True:
        password = input("Enter the Password : ")
        if detail[1] == password:
            print(f"Hello {detail[3]}")
            return detail
        else:
             print("Incorrct Password. Try again ")

#===========================================================

 #=====================WRITE_DECTONERY_FILE ================           
def write_user_balance():
    global user_balance
    with open('user_balance.txt','w') as file:
        for key,value in user_balance.items():
                file.write(f'{key},{value},\n')


def write_user_balance_dec():
    global user_balance
    with open('user_balance.txt','r') as file:
        lines = file.readlines()

    for i in lines:
        split_key_value = i.strip('\n').split(',')
        user_balance[split_key_value[0]] = float(split_key_value[1])        
#=================================================================

#=======================DEPOSIE_ WITHDRAY==========================              
def deposit_money(amount,user_id):
    global user_balance
    balance = float(user_balance.get(user_id[0]))
    balance += amount
    user_balance.pop(user_id[0])
    user_balance[user_id[0]] = balance
    print("Deposit Successful.")
    print(f"Your Account Balance : {balance}")
    return user_id[0]

def money_withdraw(amount,user_id):
    global user_balance
    balance = float(user_balance.get(user_id[0]))
    balance = balance - amount
    print(f'Your Account Balance : {balance}')
    user_balance.pop(user_id[0])
    user_balance[user_id[0]] = balance
    print(f"Withdraw Successful.")
    print(f"Your Account Balance : {balance}")
    return user_id[0]

def transaction_withdraw_deposite(user_ID,add_money):
    global choice
    global user_balance
    date = date_time()
    new_balance = user_balance.get(user_ID)
    with open('user_transaction.txt', 'a') as file:
        if choice == 2:
            file.write(f'Deposite , {user_ID},{date},{add_money},{new_balance},\n')
        elif choice ==3:
            file.write(f'Withdraw , {user_ID},{date},{add_money},{new_balance},\n')
        elif choice ==1:
             file.write(f'Deposite , {user_ID},{date},{add_money},\n')
#=============================================================================

#=======================TRANSACTION_HISTORY===================================
def transaction_history():
    global New_login
    global user_login_id
    with open('user_transaction.txt','r') as file:
            lines = file.readlines()
            if New_login[0] == 2:
                user_login = user_login_id
                print('===============================================================================================')
                print('|      DATE & TIME     |         USER_ID       |   TYPE OF TRANSACTION  |       AMOUNT      |    ')
                print('===============================================================================================')
                for line in lines:
                    user = [field.strip() for field in line.strip().split(',')]
                    if user[1] == user_login[0]:
                        print(f'| {user[2]}  |      {user[1]}       |         {user[0]}       |       {float(user[3])}    ') 

            elif New_login[0] ==1:
                user_login = check_id_password()
                print('===============================================================================================')
                print('|      DATE & TIME     |         USER_ID       |   TYPE OF TRANSACTION  |       AMOUNT      |    ')
                print('===============================================================================================')
                for line in lines:
                    user = [field.strip() for field in line.strip().split(',')]
                    if user[1] == user_login[0]:
                        print(f'| {user[2]}  |      {user[1]}       |         {user[0]}       |       {float(user[3])}    ')
            else:
                print("Data not Found")


#==================================================================================

#=====================CHECK_BALANCE===================

def check_balance():
    global user_balance
    global New_login
    if New_login[0] == 1:
        user_id = check_id_password()
        balance_01 = user_balance.get(user_id[0])
        print(f"Account Balance : {balance_01}")

    elif New_login[0] == 2:
        balance_02 = user_balance.get(New_login[1])
        print(f"Account Balance : {balance_02}")

    else:
        user_id = check_id_password()
        balance_01 = user_balance.get(user_id[0])
        print(f"Account Balance : {balance_01}")

#=====================================================================

#===============================ADMIN_MENU========================================
New_login = login()
if New_login[0] ==1:
    print('       Admin Login       ')
    write_user_balance_dec()
    while True:
        print("====Admin Menu======")
        print("1. Create Account.")
        print("2. Deposite Money.")
        print("3. withdraw Money.")
        print("4. Transaction History.")
        print("5. Add Admin ID")
        print("6. Check Balance")
        print("7. Exit.")
        try:
            choice = int(input("Enter Your choise :"))
    
            if choice == 1:
                collect_user_details()
    
            elif choice ==2:
                if len(user_balance) > 2:
                    user_login_id = check_id_password()
                    amount_01 = deposit_amount_check()
                    deposite =  deposit_money(amount_01,user_login_id)
                    transaction_withdraw_deposite(deposite,amount_01)
                else:
                    print("Data Not Found")

            elif choice ==3:
                if len(user_balance) >2:
                    user_id_02 = check_id_password()
                    amount_02 = withdraw_amount_check(user_id_02)
                    withdraw = money_withdraw(amount_02,user_id_02)
                    transaction_withdraw_deposite(withdraw,amount_02)
                else:
                    print("Data Not Found")
                    
            elif choice == 4:
                if len(user_balance) >2:
                    transaction_history()

                else:
                    print("Data Not Found")

            elif choice ==5:
                add_admin_id()

            elif choice == 6:
                if len(user_balance) >2:
                    check_balance()

                else:
                    print("Data Not Found")

            elif choice == 7:
                write_user_balance()
                print("Thank You")
                exit()

            else:
                print('Enter Number Between 1 to 7. ')
        except ValueError:
            print("Choise Must be on Numbers.")
#=================================================================================

#===============================CUSTOMER_MENU=======================================         
elif New_login[0] ==2: 
    print('     Customer Login       ')
    write_user_balance_dec()
    user_login_id = [New_login[1]]
    user_login_id.append("hello")
    while True:
        print("=====Customer Menu======")
        print("1. Check balance")
        print("2. Deposite Money.")
        print("3. withdraw Money.")
        print("4. Transaction History.")
        print("5. Exit.")

        try:
            choice = int(input("Enter Your choise :"))
    
            if choice == 1:
                check_balance()
    
            elif choice ==2:
                amount_01 = deposit_amount_check()
                deposite =  deposit_money(amount_01, user_login_id)
                transaction_withdraw_deposite(deposite,amount_01)

            elif choice ==3:
                amount_02 = withdraw_amount_check(user_login_id)
                withdraw = money_withdraw(amount_02,user_login_id)
                transaction_withdraw_deposite(withdraw,amount_02)
                
            elif choice == 4:
                transaction_history()


            elif choice == 5:
                write_user_balance()
                print("Thank You")
                exit()

            else:
                print('Enter Number Between 1 to 5. ')

        except ValueError:
            print("Choise must be on Numbers.")

