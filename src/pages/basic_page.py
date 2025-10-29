from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    with allure.step('Ищем элемент..'):
        def find(self, locator):
            wait = WebDriverWait(self.browser, 10)
            return wait.until(EC.presence_of_element_located(locator))

    with allure.step('Ищем кнопку и нажимаем кнопку'):
        def find_click_button(self, locator):
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.element_to_be_clickable(locator)).click()

    with allure.step('Наводим курсор на элемент'):
        def move_elem(self, elem):
            actions = ActionChains(self.browser)
            return actions.move_to_element(elem).perform()

    with allure.step('Проверяем значение корзины'):
        def check_cart_value(self, cart_value_start):
            self.find(())
            if cart_value != cart_value_start:
                return True
            else:
                return False

