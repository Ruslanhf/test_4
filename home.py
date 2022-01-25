from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(15)
wait = WebDriverWait(driver, 15)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 .attachment-shop_catalog").click()
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_class_name("reviews_tab").click()
driver.find_element_by_class_name("star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Ruslan")
driver.find_element_by_id("email").send_keys("ironlolka1@mail.ru")
driver.find_element_by_id("submit").click()
index = wait.until(EC.url_to_be("http://practice.automationtesting.in/wp-comments-post.php"))
print("Комментарий уже добавлен - ",index)
driver.quit()