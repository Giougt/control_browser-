from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import pyautogui


a =input("info")
b =input("info")

chromedriver_path = "path of chromedriver"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

#ouverture + full_size 
driver.get("url of site")
driver.maximize_window()

sleep(2)

screenshot = pyautogui.screenshot()
screenshot.save("test1.png")

driver.find_element(By.ID,"id").click()
input= driver.find_element(By.ID,"id")
input.send_keys(a)

sleep(2)

driver.find_element(By.ID,"id").click()
input= driver.find_element(By.ID,"id")
input.send_keys(b)

sleep(2)

driver.find_element(By.ID,"id").click()

sleep(4)