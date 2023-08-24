import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://USERNAME:PASSWORD@WEBSITE.COM')
time.sleep(3)

driver.get('CERTAINWEBPAGEWITHINWEBSITE')
select_dropdown_option = driver.find_element(By.XPATH, '//*[@name="srch"]/option[4]').click()
press_go_button = driver.find_element(By.XPATH, '//*[@name="sub"]').click()
time.sleep(2)
accept_button = driver.find_element(By.XPATH, "//*[contains(@href, 'WEBSITELINK')]").click()
time.sleep(2)
press_schedule_now_button = driver.find_element(By.XPATH, '//*[@name="NAMEOFBUTTON"]').click()
