class ATM:
    # static variable...
    counter=1
    def __init__(self):
        self.__pin=0
        self.__balance=0
        self.id=ATM.counter #whenever we wnat to use the static variable we use the class name
        ATM.counter=ATM.counter+1
        # print("Hello I am constructor")
        self.menu()
    def get_pin(self):
        return self.__pin
        ## getter and setter method
    def set_pin(self,new_pin):
        if type(new_pin)== int :
            self.__pin=new_pin
        else :
            print("Please set only integer type pass")
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
        self.__pin=int(input("Enter your PIN: "))
        print("Your PIN is set successfully...")
        self.menu()
    
    def deposit(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            self.__balance=self.__balance+ amount

            print("Your Deposit is successfull...")

        else:
            print("Invalid PIN...")
        
        self.menu()

    def withdraw(self):
        temp=int(input("Enter your PIN: "))
        if temp == self.__pin:
            amount=int(input("Enter the amount: "))
            if amount<self.__balance:
                self.balance=self.__balance-amount
                print("Your withdrawal is successfull...")
            else:
                print("Your withdrawal is unsuccessfull...")

        else:
            print("Invalid PIN")
        
        self.menu()

    def check_balance(self):
        temp=int(input("Enter your PIN: "))
        if temp == self.__pin:
            print("Your current balance is : ",self.__balance)
        else :
            print("Invalid PIN")

        self.menu()




ebl= ATM()
