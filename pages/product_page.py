from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_ad_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_ad_to_basket.click()

    def should_be_book_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUST_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_name == added_product_name, "The title of the book doesn't match"
        assert product_price == basket_price, "The price of the book doesn't match"
