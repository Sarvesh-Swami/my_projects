from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome(service=webdriver.chrome.service.Service("chromedriver.exe"))
driver.get("https://www.crazygames.com/game/stickman-ww2")

WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.CLASS_NAME, "css-g39b1"))
)
play = driver.find_element(By.CLASS_NAME, "css-g39b1")
play.click()
time.sleep(99)