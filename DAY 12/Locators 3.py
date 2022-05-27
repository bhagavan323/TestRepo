from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Drivers/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://narayanagroup.org/")
driver.maximize_window()
driver.find_element(By.NAME,"txtScode").send_keys("nes")
driver.find_element(By.NAME,"btnLogin").click()


# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# tag  & ID  tagname#valueofId    inout#email

#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# tag & Class   tagname.valueClass    input.inputtext
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# tag & attribute  tagname[attribute=value]
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc@gmail.com")

# tag Class & attribute  tagname.valueofClass[attribute=value]


#driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc@gmail.com")




