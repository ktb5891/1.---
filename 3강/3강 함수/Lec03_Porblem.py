numlist = input('숫자를 입력하세요 ')
index = 0
ch = numlist[0]
while True :
    star =""
    for i in range(int(ch)*2) :
        star = star + '\u2605'
        i = i +1        
    print(star)
    index = index +1
    if (index >len(numlist)-1):
        break
    ch = numlist[index]