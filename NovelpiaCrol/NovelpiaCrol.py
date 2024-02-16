from distutils import fancy_getopt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium

import time
import csv
import os


#크롬 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 브라우저 생성
browser = webdriver.Chrome(options=chrome_options)



#소설 클래스
class Novel:
    def __init__ (self,title,view,recommend,episode,writer,tag):
        self.title=title
        self.view=view
        self.recommend=recommend
        self.episode=episode
        self.writer=writer
        self.tag=tag

#크롤링
def Crawling():
    title=browser.find_elements(By.CLASS_NAME, "name_st")
    view=browser.find_element(By.CSS_SELECTOR,"body > div:nth-child(49) > div.epnew-wrapper.s_inv > div.epnew-novel-info > div.ep-info-line.info-count1 > div.counter-line-a > p:nth-child(1) > span:nth-child(2)").text
    recommend=browser.find_element(By.CSS_SELECTOR,"body > div:nth-child(49) > div.epnew-wrapper.s_inv > div.epnew-novel-info > div.ep-info-line.info-count1 > div.counter-line-a > p:nth-child(2) > span:nth-child(2)").text
    episode=browser.find_element(By.XPATH,"/html/body/div[8]/div[1]/div[2]/div[5]/div[2]/div[1]/p[3]/span[2]").text
    writer=browser.find_element(By.XPATH,"/html/body/div[8]/div[1]/div[2]/div[5]/div[2]/div[1]/p[3]/span[2]").text
    tag=browser.find_element(By.XPATH,"/html/body/div[8]/div[1]/div[2]/div[5]/div[2]/div[1]/p[3]/span[2]").text
    
    b=Novel(title,view,recommend,episode,writer,tag)
    return(b)



a=[]

for page in range(1,3,1):
    
    #웹페이지 접속
    url='https://novelpia.com/plus/all/date/'+str(page);
    browser.get(url)
    
    
    #소설정보 크롤링
    print(str(page)+"번페이지 시작")
    time.sleep(5)
    asd=browser.find_elements(By.CLASS_NAME, "name_st")
    for i in asd:
        print(i.text)
    
    #a.append(Crawling())
    
    
    
    

    