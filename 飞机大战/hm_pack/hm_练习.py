class Cat:
    def eat(self):
        print("%s is eating"%self.name)
    def drink(self):
        print("it is drinking")

tom = Cat()
tom.name="TOM"

tom.eat()
print(tom)
addr=id(tom)
print("十进制is %d\n" %addr)
lazy_cat=Cat()
lazy_cat.name="大懒猫"
lazy_cat.eat()
