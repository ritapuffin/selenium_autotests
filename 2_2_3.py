from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x1 = browser.find_element_by_id("num1").text
x2 = browser.find_element_by_id("num2").text
x = str(int(x1) + int(x2))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(x)

button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()