class Acount:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount ,"was debited")
        print("Total balance = ",self.get_balance())


    def credited(self,amount):
        self.balance += amount
        print("Rs.",amount ,"was Credited")
        print("Total balance = ",self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Acount(10000,25000)
acc1.debit(1000)
acc1.credited(500)
acc1.credited(40000)