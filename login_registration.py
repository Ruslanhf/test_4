import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(15)
wait = WebDriverWait(driver, 15)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

#  Регистрация аккаунта

driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("reg_email").send_keys("ironlolka1@mail.ru")
driver.find_element_by_id("reg_password").send_keys("Strangelove2281!@#")
time.sleep(1)
driver.find_element_by_id("reg_email").click()
driver.find_element_by_name("register").click()

# Логин в систему

driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("ironlolka1@mail.ru")
driver.find_element_by_id("password").send_keys("Strangelove2281!@#")
driver.find_element_by_name("login").click()
element_logout = driver.find_element_by_id("body")
element_logout_text = element_logout.text
assert "Logout" in element_logout_text
print("Logout not none.")

driver.quit()


