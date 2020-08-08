class FourCal:  
    def __init__(self, first, second):
        self.first = first
        self.second = second  
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        if self.second == 0:
            return 0
        return self.first / self.second

class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second



if __name__ == "__main__":
    fcal1 = FourCal(10,20)
    fcal2 = FourCal(20,30)
    fcal1.setData(10,20)
    fcal2.setData(3,20)
    print(fcal1.first, fcal1.second)
    print(id(fcal1.first), id(fcal2.first))
    print(fcal1.add(), fcal2.add())

    fcal3 = MoreFourCal(4,2)
    fcal3.add()
    fcal3.div()
    fcal3.mul()
    fcal3.sub()
    fcal3.pow()
    