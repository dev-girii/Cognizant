"""
Hands-On 7 / Task 2 - Playground suite refactored onto Page Objects.

Golden rule of POM: this file contains assertions (what should happen) only.
All interactions (how to make it happen) live in pages/. There is zero
driver.find_element(...) here - verify with:
    grep -rn "find_element" automation_scripts/hands_on_7/tests/
(should return nothing).
"""

import pytest

from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage
from pages.simple_form_page import SimpleFormPage


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    page = SimpleFormPage(driver)
    page.navigate_to(base_url + "simple-form-demo/")
    page.enter_message(message)
    page.click_submit()
    assert page.get_displayed_message() == message


def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(base_url + "checkbox-demo/")

    page.check_option(1)
    assert page.is_option_checked(1) is True

    page.uncheck_option(1)
    assert page.is_option_checked(1) is False


def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(base_url + "select-dropdown-demo/")
    page.select_day("Wednesday")
    assert page.get_selected_day() == "Wednesday"


def test_input_form_submit(driver, base_url):
    page = InputFormPage(driver)
    page.navigate_to(base_url + "input-form-demo/")
    page.fill_form(
        name="Test User",
        email="test@example.com",
        password="TestPass123",
        address="123 Main St",
    )
    page.submit_form()
    assert "Thanks for contacting us" in page.get_success_message()


# Step 59: what breaks in a flat (non-POM) script if the Submit button's ID
# changes from 'submit' to 'btn-submit'?
#
# In a flat script, `driver.find_element(By.ID, 'submit').click()` is
# duplicated inline in every test function that needs to submit that form -
# test_simple_form_submission, test_input_form_submit, any future test
# reusing the same button. The ID rename breaks EVERY one of those call
# sites simultaneously, and fixing it means grep-and-replace across the
# whole test suite, with the risk of missing an occurrence or breaking a
# similarly-named locator elsewhere.
#
# With POM, the locator exists in exactly one place: e.g.
# SimpleFormPage.SHOW_INPUT_BUTTON = (By.ID, 'showInput'). Every test calls
# the readable `page.click_submit()` method instead of the raw locator, so
# fixing the rename means changing one class-level tuple in one file -
# every test that uses `.click_submit()` is automatically correct again
# with no changes to the test files themselves.
