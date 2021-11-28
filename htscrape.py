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

waitagain = WebDriverWait(driver,5)

#content = driver.find_elements_by_css_selector('#ContentPlaceHolder1_GridView1 > tbody:nth-child(1) > tr')
#for i in content:
#    print(i.text)

all_tables = pd.read_html(driver.page_source,attrs={'id':'ContentPlaceHolder1_GridView1'})
df = all_tables[0]
print(df)





