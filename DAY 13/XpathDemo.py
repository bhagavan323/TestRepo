from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Drivers/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

# Absolute xpath
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()

# Relative xpath
# driver.find_element(By.XPATH,"//*[@id='search_query_top']").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[@name='submit_search']").click()
#

# Example Contains() starts-with()

# driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()

# test()
# driver.find_element(By.XPATH,"//a[text()='Women']").click()
