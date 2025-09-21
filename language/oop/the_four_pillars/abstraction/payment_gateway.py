from abc import ABC, abstractmethod

class Payment(ABC):
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by Credit Card"
    
class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by UPI"
    
class CryptoPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by Crypto"
    
def pay_using_any_method(payment_method : Payment, amount):
    return payment_method.pay(amount)


payment1 = CreditCardPayment()
payment2 = UPIPayment()
payment3 = CryptoPayment()

print(pay_using_any_method(payment1, 1000))
print(pay_using_any_method(payment2, 2000))
print(pay_using_any_method(payment3, 3000))