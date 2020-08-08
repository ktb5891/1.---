from FighterClass import Fighter
from BoomberClass import Boomber

def war_game(airforce):
    airforce.take_off()
    airforce.fly()
    airforce.attack()
    airforce.land()

if __name__ == "__main__":
    f15 = Fighter(15)
    war_game(f15)
    print("="*50)
    b29 = Boomber(2)
    war_game(b29)