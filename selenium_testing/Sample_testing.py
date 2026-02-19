from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")

time.sleep(10)

driver.quit()


