class atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def check_balance(self):
        print("Your balance is 50,000")
    def withdraw(self,amount):
        new_amount=50000-amount
        print("You have withdrawn "+str(amount)+". Your remaining balance is"+str(new_amount)+".")

def main():
    card_number=input("Card Number: ")
    pin=input("Pin: ")
    new_user=atm(card_number,pin)
    print("Choose your activity: 1. Balance Inquiry 2. Withdrawal")
    activity=int(input("Enter 1 or 2."))
    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount=int(input("Enter the amount to withdraw:"))
        new_user.withdraw(amount)
    else:
        print("Input a valid number.")
if __name__=="_main_":
    main()
    
