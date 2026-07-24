"""
Hands-On 7 / Task 1, Steps 51-52 - SimpleFormPage

Locators live as class-level tuples, never inline inside a method - if the
site's id changes, there is exactly one line to update.
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    MESSAGE_INPUT = (By.ID, "user-message")
    SHOW_INPUT_BUTTON = (By.ID, "showInput")
    MESSAGE_DISPLAY = (By.ID, "message")

    def enter_message(self, text: str) -> None:
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(text)

    def click_submit(self) -> None:
        self.driver.find_element(*self.SHOW_INPUT_BUTTON).click()

    def get_displayed_message(self) -> str:
        # No assert statements in page methods - actions and return values only.
        return self.wait_for_element(self.MESSAGE_DISPLAY).text
