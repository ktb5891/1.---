
def CountsChars(inStr):
    numCnt, lowerCnt, upperCnt, hanCnt, etcCnt = [0] * 5
    ch = ""
    for ch in inStr :
        if ( ord(ch) >= ord("A") and ord(ch) <= ord("Z")) :
            upperCnt += 1
        elif ( ord(ch) >= ord("a") and ord(ch) <= ord("z")) :
            lowerCnt += 1
        elif ( ord(ch) >= ord("0") and ord(ch) <= ord("9")) :
            numCnt += 1
        elif ( ord(ch) >= ord("가") and ord(ch) <= ord("힣")) :
            hanCnt += 1
        else :
            etcCnt += 1
    
    CountDict = {'upper':upperCnt, 'lower':lowerCnt, 'han':hanCnt, 'num':numCnt, 'etc':etcCnt}
    return CountDict

if __name__ == "__main__":
    testStr = '22__가A나Bab12'
    testDict = CountsChars(testStr)
    print(testStr)
    print("han: "+ str(testDict['han']))
    print("num: "+ str(testDict['num']))