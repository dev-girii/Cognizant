"""
Hands-On 6 - pytest-based Playground test suite (flat driver calls).

This is the pre-POM version required by Hands-On 6: tests call driver /
find_element directly. Hands-On 7 refactors this same coverage onto Page
Objects (see automation_scripts/hands_on_7/).
"""

import sys
from pathlib import Path

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hands_on_4"))
from setup_test import open_page  # noqa: E402

MESSAGE_INPUT = (By.ID, "user-message")
SHOW_INPUT_BUTTON = (By.ID, "showInput")
MESSAGE_DISPLAY = (By.ID, "message")

FIRST_CHECKBOX = (By.NAME, "option1")

DAY_SELECT = (By.ID, "select-demo")


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    """Step 42 + Step 45: enter a message, submit, assert it's echoed back -
    parameterised across 3 different input values (3 separate test runs)."""
    open_page(driver, base_url + "simple-form-demo/")

    driver.find_element(*MESSAGE_INPUT).send_keys(message)
    driver.find_element(*SHOW_INPUT_BUTTON).click()

    displayed = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MESSAGE_DISPLAY)
    )
    assert displayed.text == message


def test_checkbox_demo(driver, base_url):
    """Step 43: check the first checkbox, verify state, uncheck, verify again."""
    open_page(driver, base_url + "checkbox-demo/")

    checkbox = driver.find_element(*FIRST_CHECKBOX)
    checkbox.click()
    assert checkbox.is_selected() is True

    checkbox.click()
    assert checkbox.is_selected() is False


def test_dropdown_selection(driver, base_url):
    """Step 49: select 'Wednesday' from the Select Dropdown List demo."""
    open_page(driver, base_url + "select-dropdown-demo/")

    dropdown = Select(driver.find_element(*DAY_SELECT))
    dropdown.select_by_visible_text("Wednesday")

    assert dropdown.first_selected_option.text == "Wednesday"
