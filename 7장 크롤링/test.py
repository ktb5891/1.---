# from selenium import webdriver
# import time


# # 크롬 웹 드라이버의 경로를 설정합니다.

# driver = webdriver.Chrome('chromedriver.exe')



# # 크롬을 통해 네이버 로그인 화면에 접속합니다.

# driver.get('https://nid.naver.com/nidlogin.login')

# time.sleep(5)

# driver.find_element_by_name('id').send_keys('ktb5891')

# time.sleep(0.5)

# driver.find_element_by_name('pw').send_keys('xoqja489775')

# time.sleep(0.5)

# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


# import re
 
# def cleanText(readData):
 
#     #텍스트에 포함되어 있는 특수 문자 제거
 
#     text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
 
#     return text
 
# thisdata = 'soskdj1293[][][]aasdfAA?!<>()'
# thisdata1 = cleanText(thisdata)
# # print(thisdata1)

# from tkinter import filedialog

# def Load():
#     filename = filedialog.askopenfilename(initialdir="/", title="Select file",
#                                           filetypes=(("PPTX files", "*.pptx"),
#                                           ("all files", "*.*")))
#     print(filename)
# Lo
import datetime
import time

if __name__ == "__main__":
    print("Start")
    time.sleep(1)
    cur_time = datetime.datetime.now()
    print('현재 시각 : %s' % cur_time)
    time.sleep(1)
    print('End')