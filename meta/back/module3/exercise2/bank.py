# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):

    def basicinfo():
        print("This is a generic bank")
        return "Generic bank:0"

    @abstractmethod 
    def withdraw(self, amount):
        pass

# Class Swiss
class Swiss(Bank):
  
    def __init__(self):
        self.balance = 1000

    def basicinfo(self):
        print("This is a swiss bank")
        return "Swiss Bank: " + str(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn amount: " + str(amount))
            print("New balance: " + str(self.balance))
        else:
            print("Insufficient funds")
        return self.balance
  
# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()