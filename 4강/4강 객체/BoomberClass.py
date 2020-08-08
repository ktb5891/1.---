from AirForceClass import AirForce
class Boomber(AirForce):
    def __init__(self, bomb_num):
        self.bomb_num = bomb_num
    def take_off(self):
        print("폭격기 발진") 
    def fly(self):
        print("폭격기 목적지 출격")
    def attack(self):
        for _ in range(self.bomb_num):
            print("폭탄 투하")
            self.bomb_num = 0
    def land(self):
        print("폭격기 착륙")
    def bomb(self):
        print("추가 추가")