import schedule
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

def schedule_check():
	try:
		driver.get('securelogintowebsite')
		time.sleep(2)
		driver.get('website')
		driver.find_element(By.XPATH, '//*[@name="srch"]/option[1]').click()
		driver.find_element(By.XPATH, '//*[@name="sub"]').click()
		time.sleep(2)
		driver.find_element(By.XPATH, "//*[contains(@href, 'website')]")
	except:
		driver.refresh()
		time.sleep(30)
		schedule_check()
	else:
		pass

schedule_check()

def all_days():
		try:
		driver.get('website')
		driver.find_element(By.XPATH, '//*[@name="srch"]/option[1]').click()
		driver.find_element(By.XPATH, '//*[@name="sub"]').click()
		time.sleep(2)
		driver.find_element(By.XPATH, "//*[contains(@href, '1111')]")
		driver.find_element(By.XPATH, "//*[contains(@href, 'website')]").click()
		time.sleep(2)
		press_schedule_now_button = driver.find_element(By.XPATH, '//*[@name="dropdown"]').click()
	except:
		pass

		try:
		driver.get('website')
		driver.find_element(By.XPATH, '//*[@name="srch"]/option[1]').click()
		driver.find_element(By.XPATH, '//*[@name="sub"]').click()
		time.sleep(2)
		driver.find_element(By.XPATH, "//*[contains(@href, '1111')]")
		driver.find_element(By.XPATH, "//*[contains(@href, 'website')]").click()
		time.sleep(2)
		press_schedule_now_button = driver.find_element(By.XPATH, '//*[@name="dropdown"]').click()
	except:
		pass

def job():
	schedule_check()
	all_days()

schedule.every().day.at("06:55").do(job)


while True:
	schedule.run_pending()
	time.sleep(1)
