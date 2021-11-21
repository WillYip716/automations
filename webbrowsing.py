
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.techlistic.com/p/selenium-practice-form.html')

messageField = driver.find_element_by_xpath('//*[@id="post-body-3077692503353518311"]/div[1]/div/div[3]/input')
messageField.send_keys('HEllo word')
#showMessageButton =  driver.find_element_by_xpath('')
#showMessageButton.click()