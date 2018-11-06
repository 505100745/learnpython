class SweetPotato: ###定义一个地瓜类
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condinments = [] #为了能够存储多个数据，往往在开中让一个属性是列表

    def __str__(self):
        return "地瓜状态：%s 烘烤次数：%d,添加的佐料有：%s"%(self.cookedString,self.cookedLevel,str(self.condinments))
    def cook(self,cooked_time):
        #因为这个方法被调用了多次，为了再一次调用这个方法的时候，能够获取到上一次调用这个方法时的cooked_time
        #所以需要在此把cooker_time保存到这个对象的属性中，因为属性不会随着方法的调用而结束
        #一个方法被调用的时候是可以用局部变量来保存数据的，但是当这个方法定义结束只有这个方法中的所有数据就没有了

        self.cookedLevel += cooked_time
        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = "生的"
        elif self.cookedLevel > 3 and self.cookedLevel < 5:
            self.cookedLevel = "半生不熟"
        elif self.cookedLevel >= 5  and self.cookedLevel < 8:
            self.cookedString = "熟了"
        elif self.cookedLevel > 8:
            self.cookedString = "烤糊了"

    def addCondiments(self,item):
        #因为item这个变量指向了一个佐料，所以接下来需要将item放到append里面
        self.condinments.append(item)

di_gua = SweetPotato()



di_gua.cook(1)
print(di_gua)

di_gua.cook(1)
print(di_gua)

di_gua.addCondiments("大蒜")
di_gua.cook(1)

print(di_gua)