#Abstraction oops concept 
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False 
    def start(self):
        self.clutch = True #unnecessary things which are get hide 
        self.acc= True  ##unnecessary things which are get hide 
        print("Car started")

car1 = Car()
car1.start()