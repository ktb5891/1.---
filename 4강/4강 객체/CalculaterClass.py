class Calculator:    
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num 
        #self.result = self.result + num 
        return self.result

#cal1 = Calculator.__init__()
cal1 = Calculator()
cal1.add(30)
print(cal1.result)
cal1.add(20)
print(cal1.result)
print(id(cal1))
