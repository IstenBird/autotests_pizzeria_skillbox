from src.pages.basic_page import BasePage
import allure


link = 'https://pizzeria.skillbox.cc/'


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    with allure.step(f'Открываем страницу {link}'):
        def open_page(self):
            self.browser.get(link)
