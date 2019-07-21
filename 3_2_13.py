import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
        
class Test(unittest.TestCase):
    def test_old_page_success(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link1)
        input1 = browser.find_element_by_css_selector('div.first_block .form-control.first')
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector('div.first_block .form-control.second')
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector('div.first_block .form-control.third')
        input3.send_keys("test@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Should be greetings message")
        browser.quit()
        
    def test_new_page_success(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link2)
        input1 = browser.find_element_by_css_selector('div.first_block .form-control.first')
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector('div.first_block .form-control.second')
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector('div.first_block .form-control.third')
        input3.send_keys("test@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Should be greetings message")
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()
    