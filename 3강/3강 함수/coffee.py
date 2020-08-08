def coffee_machine(coffee):
    print()
    print("#1. 뜨거운 물을 준비한다.")
    print("#2. 종이컵을 준비한다.")

    if coffee == 1:
        print("#3. 보통커피를 준비한다.")
    elif coffee == 2:
        print("#3. 설탕커피를 준비한다.")
    elif coffee == 3:
        print("#3. 블랙커피를 준비한다.")
    else:
        print("#3. 아무거나 준비한다.")

    print("#4. 물을 붓는다.")
    print()
    print("#5. 커피 나옵니다.")

if __name__ == "__main__":
    coffee = int(input("어떤 커피를 드릴까요?(1:보통,2:설탕,3:블랙 ) : "))
    coffee_machine(coffee)