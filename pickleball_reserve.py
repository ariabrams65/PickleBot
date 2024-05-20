from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import datetime

def get_3rd_date(driver):
    date_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.single-date-select-one-click:nth-child(3) > p:nth-child(2)"))
    )
    return date_element.text.split()[1]


def sleep_until_midnight():
    cur_time = datetime.datetime.now()    
    target_time = cur_time.replace(day=cur_time.day + 1, hour=0, minute=5, second=0, microsecond=0)
    time_difference = (target_time - cur_time).total_seconds()
    print(time_difference)
    time.sleep(time_difference)


driver = webdriver.Firefox()
driver.get("https://my.campusrec.uci.edu/booking")

booking = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnBookingIndexShowLoginBlock_e06954a1-5e89-4d78-abcd-995ddb8249fb > img:nth-child(1)"))
)
booking.click()

netid_signin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-external-login"))
)
time.sleep(1)
netid_signin.click()

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#j_username"))
)
username.send_keys("adabrams")

password = driver.find_element(By.CSS_SELECTOR, "#j_password")
password.send_keys("Ruff2069")

login = driver.find_element(By.CSS_SELECTOR, ".btn")
login.click()

#Since I manually have to accept duo we are wating a full minute
trust = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#trust-browser-button"))
)
trust.click()

booking = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#divBookingProducts-large > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)"))
)
booking.click()

initial_third_date = get_3rd_date(driver)  
while True:
    time.sleep(10)
    driver.refresh()
    if initial_third_date != get_3rd_date(driver):
        break


date = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,  "button.date-selector-btn-secondary:nth-child(3)"))
)
date.click()

book_8_9 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnOpenSlot_701dd166-071e-4a0a-bfeb-dc340efc661e"))
)
book_8_9.click()

book_9_10 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnOpenSlot_abb913b9-ebd2-4360-b556-54300e204ba7")) 
)
book_9_10.click()
#driver.close()