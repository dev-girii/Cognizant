"""
Hands-On 7 / Task 1, Step 53 - CheckboxPage

Targets the "Click on check box" widget (checkboxes named option1..option4)
on the Checkbox Demo page - the page has a second, separate "Select Product"
checkbox group above it, which this page object intentionally does not touch.
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckboxPage(BasePage):
    # 1-indexed to match how the demo page itself labels them (Option 1-4).
    OPTIONS = {
        1: (By.NAME, "option1"),
        2: (By.NAME, "option2"),
        3: (By.NAME, "option3"),
        4: (By.NAME, "option4"),
    }

    def _checkbox(self, index: int):
        return self.driver.find_element(*self.OPTIONS[index])

    def check_option(self, index: int) -> None:
        checkbox = self._checkbox(index)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self, index: int) -> None:
        checkbox = self._checkbox(index)
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self, index: int) -> bool:
        return self._checkbox(index).is_selected()
