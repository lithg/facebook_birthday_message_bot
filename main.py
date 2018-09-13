from selenium import webdriver
import time


driver = webdriver.Chrome('chromedriver.exe')
driver.set_page_load_timeout(10)

email = input("Enter Username: ")
passwd = input("Enter password: ")

driver.get('https://www.facebook.com/login')
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('pass').send_keys(passwd)
driver.find_element_by_name('login').click()

time.sleep(5)

# entering on birthday page
driver.get('https://www.facebook.com/events/birthdays/')

text_area = driver.find_elements_by_tag_name('textarea')
for i in text_area:
    i.send_keys('Parabéns! \n Muitas felicidades.')

time.sleep(5)
driver.quit()
