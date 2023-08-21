import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# loads window
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_experimental_option("detach", True)
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('WEBSITEWEBSITEWEBSITE')
search = driver.find_element(by=By.LINK_TEXT, value="LOGIN").click()
time.sleep(5)

# search.send_keys(Keys.RETURN)

# https://apps.schedule360.com/sart

# time.sleep(5)
# driver.close()
