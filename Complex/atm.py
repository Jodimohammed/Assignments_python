
 #python program for simple ATM machine performing deposit,withdraw,transactions functions .
balance = 0

transactions = []

def deposit():
    global balance
    
    dep_amt = int(input("please enter amount to deposit: "))
    balance += dep_amt
    withdrew = f"Credited: ${balance}" 
    transactions.append(withdrew)
    
def withdraw():
    global balance
    
    withdraw_amt = int(input("Please enter amount to withdraw: "))
    if withdraw_amt > balance :
        print("Sorry Insufficient funds.") 
        
    else:
        balance -= withdraw_amt
        print("done\n"f"you have ${balance} remaining.") 
        withdrew = f"Debited: ${balance}"
        transactions.append(withdrew)
        
def transactions_rec():
        for item in transactions:
            print(item)
            print("------------------")
        
    
while True:
    choice =  input("please enter your choice of transaction type 1 to deposit and type, 2 to withdraw  type, 3 to see transactions  or type 4 quit ")
    if choice == '1' :
        deposit()
        
    elif choice == '2' :
        withdraw()
        
    elif choice == '3' :
        transactions_rec()
    
    elif choice == '3' :
        break
    
    else : 
        print("invalid option.")

        

        


        
