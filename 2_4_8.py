from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button1 = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
browser.execute_script("arguments[0].scrollIntoView(true);", button1)
button1.click()

x_value = browser.find_element_by_id("input_value")
x = calc(x_value.text)
browser.find_element_by_id("answer").send_keys(x)

browser.find_element_by_id('solve').click()
