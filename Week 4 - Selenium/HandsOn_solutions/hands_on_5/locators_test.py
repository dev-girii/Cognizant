"""
Hands-On 5 / Task 1 - Locator Strategies, From Simple to Robust
==================================================================
Target: Simple Form Demo (message input) and Checkbox Demo (option labels).

Note on By.NAME: DevTools inspection of the current Simple Form Demo page
shows the message <input id="user-message"> carries no `name` attribute
(only class + id). Rather than fake a locator that doesn't exist on the real
page, By.NAME is demonstrated against the Checkbox Demo's
<input name="option1">, which genuinely has one. This is itself a realistic
locator lesson: sites change their markup over time, and a strategy that
worked in a tutorial can silently stop applying to a specific element -
always verify locators against the live DOM (F12), never assume.
"""

import sys
from pathlib import Path

from selenium.webdriver.common.by import By

# Reuse the driver factory built in Hands-On 4 rather than duplicating it.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hands_on_4"))
from setup_test import build_driver  # noqa: E402

SIMPLE_FORM_URL = "https://www.lambdatest.com/selenium-playground/simple-form-demo/"
CHECKBOX_URL = "https://www.lambdatest.com/selenium-playground/checkbox-demo/"

# Absolute XPath is captured here exactly as it exists on the live page today.
# It is intentionally the "worst" locator in the ranking below - any layout
# change (e.g. inserting one new <div>) breaks it.
ABSOLUTE_XPATH = (
    "/html/body/div[1]/div[1]/main[1]/div[1]/section[2]/div[1]/div[1]"
    "/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
)


def locate_simple_form_message_input() -> None:
    driver = build_driver(headless=True)
    try:
        driver.get(SIMPLE_FORM_URL)

        by_id = driver.find_element(By.ID, "user-message")
        assert by_id.tag_name == "input"
        print("By.ID: found")

        by_class = driver.find_element(By.CLASS_NAME, "border-gray-550")
        assert by_class.get_attribute("id") == "user-message"
        print("By.CLASS_NAME: found")

        # TAG_NAME matches every <input> on the page and returns the first
        # one in DOM order - which, on this live page, is actually a hidden
        # "Schedule Demo" widget field (id=inputFirstName), NOT the message
        # box. This is exactly why TAG_NAME alone is rarely a usable
        # production locator: it "works" only in the sense that it finds
        # *an* <input>, not necessarily the right one.
        by_tag = driver.find_element(By.TAG_NAME, "input")
        print(f"By.TAG_NAME: found (id={by_tag.get_attribute('id')!r} - not the target element)")

        by_xpath_abs = driver.find_element(By.XPATH, ABSOLUTE_XPATH)
        assert by_xpath_abs.get_attribute("id") == "user-message"
        print("By.XPATH (absolute): found")

        by_xpath_rel = driver.find_element(
            By.XPATH, "//input[@id='user-message' and @placeholder]"
        )
        assert by_xpath_rel.get_attribute("id") == "user-message"
        print("By.XPATH (relative, attribute-based): found")

        # --- Task 1, Step 33: three CSS selectors for the same element ---
        css_by_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
        css_by_attr = driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Please enter your Message']"
        )
        css_by_parent_child = driver.find_element(
            By.CSS_SELECTOR, "div.left-input > input"
        )
        for i, el in enumerate([css_by_id, css_by_attr, css_by_parent_child], start=1):
            assert el.get_attribute("id") == "user-message", f"CSS selector #{i} mismatch"
        print("3x By.CSS_SELECTOR (#id, [attr], parent > child): all found")

    finally:
        driver.quit()


def locate_checkbox_labels_and_name() -> None:
    driver = build_driver(headless=True)
    try:
        driver.get(CHECKBOX_URL)

        # By.NAME - demonstrated on the real element that has one.
        by_name = driver.find_element(By.NAME, "option1")
        assert by_name.get_attribute("type") == "checkbox"
        print("By.NAME: found (input[name='option1'])")

        # Task 1, Step 34: XPath text() and contains().
        exact = driver.find_element(By.XPATH, "//label[text()='Option 1']")
        print(f"XPath text()='Option 1': found -> {exact.text!r}")

        # The Checkbox Demo page actually contains two separate checkbox
        # widgets ("Select Product" and "Click on check box"), each with its
        # own Option 1-4 labels, so contains(text(),'Option') legitimately
        # matches 8 labels total, not 4 - verified against the live DOM.
        all_options = driver.find_elements(
            By.XPATH, "//label[contains(text(),'Option')]"
        )
        print(f"XPath contains(text(),'Option'): found {len(all_options)} labels")
        assert len(all_options) == 8

    finally:
        driver.quit()


# Task 1, Step 35: ranking, most to least preferred for maintainable automation.
#
# 1. ID              - unique by spec, fastest lookup, immune to text/layout
#                       changes. Most preferred whenever the app assigns one.
# 2. CSS Selector (by attribute, e.g. [placeholder='...'])
#                       - fast, readable, resilient to structural changes as
#                       long as the attribute itself is stable.
# 3. NAME             - as unique/fast as ID in practice on well-formed forms,
#                       ranked just below ID/CSS only because it's less
#                       universally present (many modern elements omit it).
# 4. XPath (relative, attribute-based, e.g. //input[@id='...'])
#                       - flexible (can express text/parent-axis conditions
#                       CSS can't), but slightly slower than CSS and easier
#                       to write in a brittle way if not careful.
# 5. CLASS_NAME / TAG_NAME
#                       - rarely unique on a real page (utility CSS frameworks
#                       reuse class names everywhere; tag names match dozens
#                       of elements), so these are last-resort or must be
#                       combined with other conditions to be reliable.
# 6. XPath (absolute, e.g. /html/body/div[1]/.../input[1])
#                       - least preferred: encodes the entire DOM structure
#                       above the element, so it breaks the instant *any*
#                       ancestor element is added, removed, or reordered,
#                       even if the target element itself never changed.
if __name__ == "__main__":
    locate_simple_form_message_input()
    locate_checkbox_labels_and_name()
