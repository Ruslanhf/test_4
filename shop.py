import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(15)
wait = WebDriverWait(driver, 15)
driver.maximize_window()

# Отображение страницы товара

# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("ironlolka1@mail.ru")
# driver.find_element_by_id("password").send_keys("Strangelove2281!@#")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 600);")
# driver.find_element_by_class_name("post-181").click()
# heading = driver.find_element_by_class_name("product_title")
# heading_text = heading.text
# assert heading_text == "HTML5 Forms"
# print("Heading book - ", heading_text)

# Количество товаров в категории

# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("ironlolka1@mail.ru")
# driver.find_element_by_id("password").send_keys("Strangelove2281!@#")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector("aside>div>ul>li.cat-item-19>a").click()
# html_count = driver.find_elements_by_css_selector("ul> .product")
# number_html_count = len(html_count)
# print("Количество товаров на странице -", number_html_count)

# Сортировка товаров

# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("ironlolka1@mail.ru")
# driver.find_element_by_id("password").send_keys("Strangelove2281!@#")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# sort_default = driver.find_element_by_css_selector("[value='menu_order']")
# sort_default_att = sort_default.get_attribute("selected")
# sort_default_text = sort_default.text
# assert "Default sorting" in sort_default_text
# print("Выбрана сортировка по умолчанию -", sort_default_att)
# sort_by = driver.find_element_by_class_name("orderby")
# select = Select(sort_by)
# select.select_by_value("price-desc")
# sort_h = driver.find_element_by_css_selector("[value='price-desc']")
# sort_h_att = sort_h.get_attribute("selected")
# sort_ha_text = sort_h.text
# assert "Sort by price: high to low" in sort_ha_text
# print("Выбрана сортировка от большей к меньшей -", sort_h_att)

# Отображение, скидка товара

# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("ironlolka1@mail.ru")
# driver.find_element_by_id("password").send_keys("Strangelove2281!@#")
# driver.find_element_by_name("login").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 600);")
# driver.find_element_by_class_name("post-169").click()
# old_price = driver.find_element_by_css_selector(".price>del>span")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price>ins>span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# print("Старая цена -", old_price_text)
# print("Новая цена -", new_price_text)
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images"))).click()
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()

# Првоерка цены в корзине

# driver.get("http://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector(".post-182 > .button").click()
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cartcontents"), "1 Item"))
# item = driver.find_element_by_css_selector(".cartcontents")
# item_text = item.text
# assert item_text == "1 Item"
# print("Количество товаров в корзине -", item_text)
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".amount"), "₹180.00"))
# price = driver.find_element_by_css_selector(".amount")
# price_text = price.text
# assert price_text == "₹180.00"
# print("Стоимость товаров -", price_text)
# driver.find_element_by_css_selector(".wpmenucart-contents").click()
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal")))
# subtotal = driver.find_element_by_css_selector(".cart-subtotal")
# subtotal_text = subtotal.text
# assert subtotal_text is not None
# print("Стоимость отобразилась -", subtotal_text)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-total")))
# total = driver.find_element_by_css_selector(".order-total")
# total_text = total.text
# assert total_text is not None
# print("Стоимость отобразилась -", total_text)


# Работа в корзине

driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
driver.find_element_by_css_selector(".post-182 > .button").click()
time.sleep(3)
driver.find_element_by_css_selector(".post-180 > .button").click()
driver.find_element_by_css_selector(".wpmenucart-contents").click()
time.sleep(3)
driver.find_element_by_css_selector(".cart_item:nth-child(1)>.product-remove .remove").click()
driver.find_element_by_link_text("Undo?").click()
driver.find_element_by_css_selector(".quantity>input").clear()
driver.find_element_by_css_selector(".quantity>input").send_keys("3")
driver.find_element_by_name("update_cart").click()
att_value = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".quantity>input"))).get_attribute("value")
assert att_value == "3"
print("Значение value =", att_value)
time.sleep(1)
driver.find_element_by_css_selector(".coupon .button").click()
wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
coupton = driver.find_element_by_css_selector(".woocommerce-error>li")
time.sleep(1)
coupton_text = coupton.text
assert coupton_text == "Please enter a coupon code."
print("Сообщение об ошибке появилось -", coupton_text)

# Покупка товара

driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector(".post-182 > .button").click()
time.sleep(1)
driver.find_element_by_css_selector(".wpmenucart-contents").click()
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name"))).send_keys("Ruslan")
driver.find_element_by_id("billing_last_name").send_keys("Blidchenko")
driver.find_element_by_id("billing_email").send_keys("ironlolka1@mail.ru")
driver.find_element_by_id("billing_phone").send_keys("89835569654")
driver.find_element_by_id("billing_address_1").send_keys("Gagarina")
driver.find_element_by_id("billing_city").send_keys("Saint-Petersburg")
driver.find_element_by_id("billing_state").send_keys("Russian Federation")
driver.find_element_by_id("billing_postcode").send_keys("333333")
driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
wait.until(EC.visibility_of_element_located((By.ID, "payment_method_cheque"))).click()
driver.find_element_by_id("place_order").click()
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
                                            "Thank you. Your order has been received."))
thanks = driver.find_element_by_css_selector(".woocommerce-thankyou-order-received")
thanks_text = thanks.text
assert "Thank you. Your order has been received." in thanks_text
print("Отображается надпись: ", thanks_text)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3)"),
                                            "Check Payments"))
check = driver.find_element_by_css_selector("tr:nth-child(3)")
check_text = check.text
assert "Check Payments" in check_text
print(check_text)
driver.quit()
