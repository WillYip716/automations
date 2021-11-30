from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

url = 'https://hashtagbasketball.com/fantasy-basketball-projections'
driver = webdriver.Chrome()
driver.get(url)

topfield = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_DDSHOW"]')
topfield.click()

wait = WebDriverWait(driver,5)

all = driver.find_element_by_xpath('/html/body/form/section/div/div[2]/div/div[1]/table/tbody/tr[2]/td[1]/select/option[6]')
all.click()

waitagain = WebDriverWait(driver,15)


driver.execute_script("window.scrollTo(0,15500)")

content = driver.find_element_by_xpath('/html/body/form/section/div/div[2]/div/div[4]/div')
inner = content.get_attribute('innerHTML')

#for i in content:
#    print(i.text)

with open('test.html',"w") as f:
    f.write(inner)

print('done')



