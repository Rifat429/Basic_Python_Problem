class ATM:
    def __init__(self):
        self.pin=0
        self.balance=0
        # print("Hello I am constructor")
        self.menu()
    
    def menu(self):
        user_input=int(input("""
      What you want to do?
      1. Enter 1 to Create PIN
      2. Enter 2 to Deposit
      3. Enter 3 to Withdraw
      4. Enter 4 to Check Balance
      5. Enter 5 to Exit
"""))
        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input==4:
            self.check_balance()
        else :
            print("Exit")

    def create_pin(self):
        self.pin=int(input("Enter your PIN: "))
        print("Your PIN is set successfully...")
        self.menu()
    
    def deposit(self):
        temp=int(input("Enter your pin: "))
        if temp==self.pin:
            amount=int(input("Enter the amount: "))
            self.balance=self.balance+ amount

            print("Your Deposit is successfull...")

        else:
            print("Invalid PIN...")
        
        self.menu()

    def withdraw(self):
        temp=int(input("Enter your PIN: "))
        if temp == self.pin:
            amount=int(input("Enter the amount: "))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Your withdrawal is successfull...")
            else:
                print("Your withdrawal is unsuccessfull...")

        else:
            print("Invalid PIN")
        
        self.menu()

    def check_balance(self):
        temp=int(input("Enter your PIN: "))
        if temp == self.pin:
            print("Your current balance is : ",self.balance)
        else :
            print("Invalid PIN")

        self.menu()




ebl= ATM()
