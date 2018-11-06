class person():
    def __init__(self,name,weight):
        self.name = name 
        self.weight = weight

    def decrease(self):
        self.weight -= 0.5
        print("每次跑步会减重0.5公斤")

    def incrase(self):
        self.weight += 1.0
        print("每次吃东西会增重1.0公斤")

    def __str__(self):
        return "我的名字叫%s，我的体重是%.2f" %(self.name,self.weight)


jay = person('jay',70)
jay.decrease()
jay.incrase()

print(jay)

lily = person('lily',45)
lily.decrease()

print(lily)
