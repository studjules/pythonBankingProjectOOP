#Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details(self):
        print("Personal Details")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("gender: ", self.gender)

#Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance= 0
    def deposit (self,amount):
        self.amount = amount
        self.balance =+ self.amount
        print("balance has been updated:", self.balance)
    def withdraw(self, amount):
        self.amount=amount
        if self.amount > self.balance:
            print ("insufficient funds")
        else:
            self.balance = self.balance -self.amount
            print("account balance updated")
            print(self.balance)
    def view_balance(self):
        self.show_details()
        print("account balance updated")
        print(self.balance)

johann = Bank ("Johann", 25, "male")

johann.deposit(20)

johann.withdraw(5)

johann.view_balance()

