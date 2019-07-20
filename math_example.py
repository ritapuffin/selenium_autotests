from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.find_element_by_tag_name('button').click()
browser.switch_to.window(browser.window_handles[1])
#time.sleep(1)

# вторая страница
x = calc(browser.find_element_by_id("input_value").text)
browser.find_element_by_id("answer").send_keys(x)

browser.find_element_by_tag_name('button').click()

