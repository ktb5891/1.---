import json
import re
from tkinter import filedialog
import time
# from hanspell import spell_checker

def Load():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("json files", "*.json"),
                                          ("all files", "*.*")))
    return filename
select_file = Load()
with open(select_file,'r',encoding='utf-8') as f:
    json_data = json.load(f)
w = open('전사파일.txt','w')

length = len(json_data["utterance"])
for i in range(0,length):
    text = json_data["utterance"][i]["form"]
    parse = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '',text)
    if parse in '데요' or '죠' or '니다' or '든요' or '세요' or '예요' or '에요' or '되요' or '돼요' or '고요' or '거야' or '어요' or '게요' or '까요' or '아요':
        parse = parse.replace('데요','데요.')
        parse = parse.replace('죠','죠.')
        parse = parse.replace('니다','니다.')
        parse = parse.replace('든요','든요.')
        parse = parse.replace('세요','세요.')
        parse = parse.replace('예요','예요.')
        parse = parse.replace('에요','에요.')
        parse = parse.replace('되요','되요.')
        parse = parse.replace('돼요','돼요.')
        parse = parse.replace('고요','고요.')
        parse = parse.replace('거야','거야.')
        parse = parse.replace('어요','어요.')
        parse = parse.replace('게요','게요.')
        parse = parse.replace('까요','까요?')
        parse = parse.replace('아요','아요.')

    #p = re.compile('[A-Z]')
    #if p.match(parse) != None:
    if parse in 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
        parse = parse.replace('A','(A)/(에이)')
        parse = parse.replace('B','(B)/(비)')
        parse = parse.replace('C','(C)/(씨)')
        parse = parse.replace('D','(D)/(디)')
        parse = parse.replace('E','(E)/(이)')
        parse = parse.replace('F','(F)/(에프)')
        parse = parse.replace('G','(G)/(쥐)')
        parse = parse.replace('H','(H)/(에이치)')
        parse = parse.replace('I','(I)/(아이)')
        parse = parse.replace('J','(J)/(제이)')
        parse = parse.replace('K','(K)/(케이)')
        parse = parse.replace('L','(L)/(엘)')
        parse = parse.replace('M','(M)/(엠)')
        parse = parse.replace('N','(N)/(엔)')
        parse = parse.replace('O','(O)/(오)')
        parse = parse.replace('P','(P)/(피)')
        parse = parse.replace('Q','(Q)/(큐)')
        parse = parse.replace('R','(R)/(알)')
        parse = parse.replace('S','(S)/(에스)')
        parse = parse.replace('T','(T)/(티)')
        parse = parse.replace('U','(U)/(유)')
        parse = parse.replace('V','(V)/(브이)')
        parse = parse.replace('W','(W)/(더블유)')
        parse = parse.replace('X','(X)/(엑스)')
        parse = parse.replace('Y','(Y)/(와이)')
        parse = parse.replace('Z','(Z)/(지)')

    if parse in ' 이 ' or ' 그 ' or ' 저 ' or ' 어 ' or ' 저기 ' or ' 에 ' or ' 응 ' or ' 아 ' or ' 음 ' or ' 으 ': 
        parse = parse.replace('이','이/')
        parse = parse.replace('그','그/')
        parse = parse.replace('저','저/')
        parse = parse.replace('어','어/')
        parse = parse.replace('저기','저기/')
        parse = parse.replace('에','에/')
        parse = parse.replace('응','응/')
        parse = parse.replace('아','아/')
        parse = parse.replace('음','음/')
        parse = parse.replace('으','으/')
        
    parse = parse+'\n'
    w.write(parse)
w.close()
time.sleep(5)
end = 'tmax'
while end != 'y':
    end = input('If you finished work press "y" : ')

