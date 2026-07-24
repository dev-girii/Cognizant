"""
Hands-On 7 / Task 1, Step 54 - DropdownPage
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class DropdownPage(BasePage):
    DAY_SELECT = (By.ID, "select-demo")

    def select_day(self, day_name: str) -> None:
        select = Select(self.driver.find_element(*self.DAY_SELECT))
        select.select_by_visible_text(day_name)

    def get_selected_day(self) -> str:
        select = Select(self.driver.find_element(*self.DAY_SELECT))
        return select.first_selected_option.text
