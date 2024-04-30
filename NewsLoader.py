from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)

driver.get("https://www.google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("youtube" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "YouTube: Home"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "YouTube: Home")
link.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)

search_element = driver.find_element(By.NAME, "search_query")
search_element.click()
time.sleep(1)
search_element.clear()
search_element.send_keys("Live News " + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Live"))
)

first_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Live")
first_link.click()

time.sleep(20)

driver.quit()