from src.pages.main_page import MainPage
from selenium.webdriver.common.by import By
import allure




@allure.suite('Главная страница')
class TestMain:
    @allure.title('Тест открытия страницы')
    def test_open_page(self, browser):
        main = MainPage(browser)
        main.open_page()
        title = main.find((By.CSS_SELECTOR, '.site-title'))
        assert title.text == 'Pizzeria'

    @allure.title('Открытие карточки товара')
    def test_open_product(self,browser):
        desired_product = "Пицца «4 в 1»"
        main = MainPage(browser)
        main.open_page()
        main.find_click_button((By.XPATH, f'//h3[contains(text(), "{desired_product}")]'))
        prod_title = main.find((By.CSS_SELECTOR, '.product_title'))
        assert desired_product in prod_title.text

    @allure.title('Добавление товара в корзину') #пока что не работает
    def test_add_product_cart(self, browser):

        main = MainPage(browser)
        main.open_page()
        cart_value = main.find((By.CSS_SELECTOR, '.cart-contents')).text
        prod = main.find((By.XPATH, '(//li/div/a[@title="Пицца «Как у бабушки»"])[2]'))
        main.move_elem(prod)
        main.find_click_button((By.XPATH, '//*[@class="button product_type_simple add_to_cart_button ajax_add_to_cart" and @data-product_id="423"]'))
        print(cart_value)



