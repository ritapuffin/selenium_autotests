from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

y = calc(browser.find_element_by_id("input_value").text)
browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_id("robotCheckbox").click()

button = browser.find_element_by_xpath('//button[text()="Отправить"]')
browser.execute_script("arguments[0].scrollIntoView(true);", button)

browser.find_element_by_css_selector("[value='robots']").click()

button.click()