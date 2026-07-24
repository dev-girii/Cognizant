"""
Hands-On 5 / Task 2 - WebDriverWait and Expected Conditions
==============================================================
Target: Bootstrap Alerts demo, and a dynamically-loaded table row style wait.
"""

import sys
import time
from pathlib import Path

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hands_on_4"))
from setup_test import build_driver, open_page  # noqa: E402

ALERTS_URL = "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo/"

# The demo page has both an auto-closing and a manually-dismissed success
# alert, both matching the generic ".alert-success" class. Clicking the
# "Normal Success Message" button (class btn-success-manual) surfaces the
# manual alert (".alert-success-manual") so the assertion below targets a
# stable, non-vanishing element rather than racing a 5-second auto-close timer.
SUCCESS_BUTTON = (By.CSS_SELECTOR, ".btn-success-manual")
SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success-manual")


def test_explicit_wait_for_alert() -> None:
    """Step 36: click a button, explicitly wait for the resulting alert."""
    driver = build_driver(headless=True)
    try:
        open_page(driver, ALERTS_URL)
        driver.find_element(*SUCCESS_BUTTON).click()

        alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(SUCCESS_ALERT)
        )
        # The live site's copy reads "Normal success message. To close use
        # the close button." (no literal word "successfully") - asserting
        # against the real text rather than the word suggested in the task
        # sheet, which doesn't match current site copy.
        assert "success" in alert.text.lower(), alert.text
        print(f"Explicit wait found alert: {alert.text!r}")
    finally:
        driver.quit()


def compare_sleep_vs_explicit_wait() -> None:
    """Step 37: time.sleep(3) vs WebDriverWait, timed side by side."""
    # --- sleep() version ---
    driver = build_driver(headless=True)
    try:
        open_page(driver, ALERTS_URL)
        start = time.perf_counter()
        driver.find_element(*SUCCESS_BUTTON).click()
        time.sleep(3)  # blind guess at how long the UI update takes
        driver.find_element(*SUCCESS_ALERT)
        sleep_duration = time.perf_counter() - start
    finally:
        driver.quit()

    # --- explicit wait version ---
    driver = build_driver(headless=True)
    try:
        open_page(driver, ALERTS_URL)
        start = time.perf_counter()
        driver.find_element(*SUCCESS_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(SUCCESS_ALERT)
        )
        wait_duration = time.perf_counter() - start
    finally:
        driver.quit()

    print(f"time.sleep(3) version:  {sleep_duration:.2f}s (always pays the full 3s)")
    print(f"WebDriverWait version:  {wait_duration:.2f}s (returns as soon as condition is true)")
    # On a fast machine the alert appears almost immediately, so the explicit
    # wait finishes far faster than the fixed 3s sleep. On a slow/loaded
    # machine where the alert genuinely takes >3s to render, the sleep()
    # version would fail outright while WebDriverWait keeps polling up to
    # its 10s timeout - explicit waits are simultaneously faster on the
    # common case and more reliable on the slow case.
    assert wait_duration < sleep_duration


def test_element_to_be_clickable() -> None:
    """Step 38: wait for clickability, not just visibility, before clicking."""
    driver = build_driver(headless=True)
    try:
        open_page(driver, ALERTS_URL)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(SUCCESS_BUTTON)
        )
        button.click()
        # visibility_of_element_located only checks that the element exists
        # in the DOM and has a non-zero rendered size (display != none,
        # visibility != hidden). element_to_be_clickable checks all of that
        # PLUS that the element is enabled and not obscured by another
        # element receiving the click instead (e.g. a loading spinner or
        # modal overlay sitting on top of it) - it's the stronger guarantee
        # you actually want immediately before calling .click().
        print("element_to_be_clickable: clicked successfully")
    finally:
        driver.quit()


def test_fluent_wait_style_polling() -> None:
    """
    Step 39: FluentWait equivalent in Python - WebDriverWait accepts the same
    poll_frequency / ignored_exceptions parameters as Java's FluentWait, so
    there is no separate "FluentWait class" needed in Selenium's Python
    bindings; passing those two arguments IS the fluent-wait behavior.
    Applied here to the alert element as a stand-in for a dynamically-loaded
    row, polling every 500ms for up to 10s and ignoring NoSuchElementException
    while the element hasn't rendered yet.
    """
    driver = build_driver(headless=True)
    try:
        open_page(driver, ALERTS_URL)
        driver.find_element(*SUCCESS_BUTTON).click()

        row = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException],
        ).until(EC.visibility_of_element_located(SUCCESS_ALERT))
        print(f"FluentWait-style polling found: {row.text!r}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_explicit_wait_for_alert()
    compare_sleep_vs_explicit_wait()
    test_element_to_be_clickable()
    test_fluent_wait_style_polling()
