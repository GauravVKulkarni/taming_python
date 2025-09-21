class Account:

    bank_name = "De na Bank"

    def __init__(self, ac_type: {"Savings", "Current"}, ac_number : int, pin : int, initial_balance : int):
        self.account_type = ac_type
        self.account_number = ac_number
        self.pin = pin
        self.balance = initial_balance
        if ac_type == "Savings":
            self.daily_limit = 100000
        else:
            self.daily_limit = 500000

    def withdraw(self, amount):
        if amount > self.balance:
            return {"error" : "insufficient balance"}
        elif amount > self.daily_limit:
            return {"error" : "amount over daily withdrawal limit"}
        else:
            self.balance -= amount
            return {"success" : f"Rs. {amount} withdrawn"}
    
    def deposit(self, amount):
        if amount > self.daily_limit:
            return {"error" : "amount over daily deposit limit"}
        else:
            self.balance += amount
            return {"success" : f"Rs. {amount} deposited"}
        
    def balance_enquiry(self):
        return {"message" : f"Balance : Rs. {self.balance}"}
    

account1 = Account("Savings", 1, 1234, 500)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.balance_enquiry())