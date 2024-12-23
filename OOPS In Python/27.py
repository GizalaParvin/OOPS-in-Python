class Father:
    def info(self):
        print("Father Method")
class Mother:
    def info(self):
        print("Mother Method")
class child1(Mother,Father):
    pass
class child2(Father,Mother):
    pass
c1 =child1()
c1.info()
c2 =child2()
c2.info()