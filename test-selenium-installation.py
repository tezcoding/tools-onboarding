from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com") # navigates to the provided link
print(driver.title) # prints the title of active browser window
# driver.quit()