from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "There is no text indicating that the " \
                                                                         "basket is empty"

