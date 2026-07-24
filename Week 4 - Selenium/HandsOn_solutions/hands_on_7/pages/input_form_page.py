"""
Hands-On 7 / Task 2, Step 57 - InputFormPage

The live "Input Form Submit" page's fields differ from the generic
"name, email, phone, address" description in the task sheet - verified via
DevTools, the real form has no phone field, and requires 11 fields (Name,
Email, Password, Company, Website, Country, City, Address x2, State, Zip)
before it accepts the submission at all (confirmed by submitting a partial
form and observing it silently stays on the form instead of showing the
success message). fill_form() keeps the 4 test-relevant parameters from the
task sheet (name, email, password, address) and fills the remaining
required-but-not-under-test fields with fixed sane values internally, so the
test file itself only has to state what it actually cares about.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InputFormPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "inputEmail4")
    PASSWORD_INPUT = (By.ID, "inputPassword4")
    COMPANY_INPUT = (By.ID, "company")
    WEBSITE_INPUT = (By.ID, "websitename")
    COUNTRY_SELECT = (By.NAME, "country")
    CITY_INPUT = (By.ID, "inputCity")
    ADDRESS1_INPUT = (By.ID, "inputAddress1")
    ADDRESS2_INPUT = (By.ID, "inputAddress2")
    STATE_INPUT = (By.ID, "inputState")
    ZIP_INPUT = (By.ID, "inputZip")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".selenium_btn")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-msg")

    _DEFAULT_COMPANY = "Cognizant"
    _DEFAULT_WEBSITE = "https://example.com"
    _DEFAULT_COUNTRY = "India"
    _DEFAULT_CITY = "Chennai"
    _DEFAULT_STATE = "Tamil Nadu"
    _DEFAULT_ZIP = "600001"

    def fill_form(self, name: str, email: str, password: str, address: str) -> None:
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.COMPANY_INPUT).send_keys(self._DEFAULT_COMPANY)
        self.driver.find_element(*self.WEBSITE_INPUT).send_keys(self._DEFAULT_WEBSITE)
        Select(self.driver.find_element(*self.COUNTRY_SELECT)).select_by_visible_text(
            self._DEFAULT_COUNTRY
        )
        self.driver.find_element(*self.CITY_INPUT).send_keys(self._DEFAULT_CITY)
        self.driver.find_element(*self.ADDRESS1_INPUT).send_keys(address)
        self.driver.find_element(*self.ADDRESS2_INPUT).send_keys(address)
        self.driver.find_element(*self.STATE_INPUT).send_keys(self._DEFAULT_STATE)
        self.driver.find_element(*self.ZIP_INPUT).send_keys(self._DEFAULT_ZIP)

    def submit_form(self) -> None:
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_success_message(self) -> str:
        return self.wait_for_element(self.SUCCESS_MESSAGE).text
