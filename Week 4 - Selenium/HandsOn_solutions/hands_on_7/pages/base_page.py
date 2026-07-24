"""
Hands-On 7 / Task 1, Step 50 - BasePage

Common functionality every page object needs: navigation, title, and a
shared explicit-wait helper. Every other page class inherits from this one.
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url: str, timeout: int = 15) -> None:
        self.driver.get(url)
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def get_title(self) -> str:
        return self.driver.title

    def wait_for_element(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
