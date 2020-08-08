from AirForceClass import AirForce

class Fighter(AirForce):
    def __init__(self, missile_num):
        self.missile_num = missile_num
    def take_off(self):
        print("전투기 발진") 
    def fly(self):
        print("전투기 목적지 출격")
    def attack(self):
        for _ in range(self.missile_num):
            print("미사일 투하")
            self.bomb_num = 0
    def land(self):
        print("전투기 착륙")
    