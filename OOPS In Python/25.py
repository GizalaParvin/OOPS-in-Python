# Inheritence Single Class 

class Vehicle:
    def start(self):
        print("Starting Engine " )
    def stop(self):
        print("Stoping Engine")
class TwoWheelers(Vehicle):
    def say(self):
        super().start()
        print("I have two wheelers")
        super().stop()
Enfield =TwoWheelers()
Enfield.say()

#Overriding Method
class A:
    def sayhi(self):
        print("I Am In A")
class B(A):
    def sayhi(self):
        print("I am In B")
bobj = B()
bobj.sayhi()