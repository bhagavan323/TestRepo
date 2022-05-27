# Test case
# ----------------
# 1. open web browser(chrome/firefox/IE)
# 2. open URL https://opensource-demo.orangehrmlive.com/index.php/auth/login
# 3. Enter username :Admin
# 4. provide password :admin123
# 5. click on login
# 6. capture title of the dashboard page (Actual title)
# 7. verify title of the page: OrangeHRM (Expected)
# 8. close browser

# Selenium 3

# from selenium import webdriver
# driver=webdriver.Chrome()
# #driver=webdriver.Chrome(executable_path="C:/Drivers/chromedriver.exe")
#
# driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login/")
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_name("Submit").click()
#
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("login test passed")
# else:
#     print("login test failed")
#
# driver.close()

# Selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:/Drivers/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login/")


driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.NAME,"Submit").click()
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("login test passed")
else:
    print("login test failed")
driver.close()
