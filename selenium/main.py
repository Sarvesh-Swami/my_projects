from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

prodcut_price_prefix = "productPrice"
product_prefix = "product"


driver = webdriver.Chrome(service=webdriver.chrome.service.Service("chromedriver.exe"))
driver.get("https://orteil.dashnet.org/cookieclicker/")
WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.ID, "langSelect-EN"))
)
language = driver.find_element(By.ID, "langSelect-EN")
language.click()
WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.ID, "bigCookie"))
)
cookie_id = driver.find_element(By.ID, "bigCookie")

while True:
    cookie_id.click()
    cookie_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookie_count = int(cookie_count)

    for i in range(4):
        upgrade_item = (prodcut_price_prefix + str(i))
        upgrade_item = driver.find_element(By.ID, upgrade_item).text.replace(",","")
        if not upgrade_item.isdigit():
            continue
        upgrade_item = int(upgrade_item)
        if cookie_count > upgrade_item:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break



