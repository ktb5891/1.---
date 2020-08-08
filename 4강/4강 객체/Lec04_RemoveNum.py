def remove_num_from_str(inStr):
    outStr = ''
    for i in range(0, len(inStr)) :
        if inStr[i].isdigit() ==  False  :
            outStr = outStr + inStr[i]
    return outStr

if __name__ == "__main__":
    testStr = input('문자열 입력: ')
    print(remove_num_from_str(testStr))

