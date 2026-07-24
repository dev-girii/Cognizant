"""
Hands-On 4 / Task 2 - WebDriver Navigation and Window Commands
================================================================
Navigates the Playground, verifies URL after following a link, exercises
multi-tab handling, and captures a screenshot.
"""

from pathlib import Path

from selenium.webdriver.common.by import By

from setup_test import build_driver

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"
SCREENSHOT_PATH = Path(__file__).parent / "playground_screenshot.png"


def run() -> None:
    driver = build_driver(headless=True)
    try:
        # Step 28: open the playground, click the Simple Form Demo link,
        # assert the URL, then navigate back.
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
        assert "simple-form-demo" in driver.current_url, (
            f"Expected 'simple-form-demo' in URL, got {driver.current_url}"
        )
        print(f"Navigated to: {driver.current_url}")
        driver.back()
        print(f"After back(): {driver.current_url}")

        # Step 29: open a new tab, list handles, switch to it.
        driver.execute_script('window.open("https://www.google.com");')
        assert len(driver.window_handles) == 2, "Expected 2 open tabs"
        driver.switch_to.window(driver.window_handles[1])
        print(f"Second tab title: {driver.title}")

        # Step 30: switch back to the original tab and screenshot it.
        driver.switch_to.window(driver.window_handles[0])
        driver.save_screenshot(str(SCREENSHOT_PATH))
        assert SCREENSHOT_PATH.exists(), "Screenshot file was not created"
        print(f"Screenshot saved to: {SCREENSHOT_PATH}")

        # Step 31: window size.
        # Consistent window size matters for responsive UI automation because
        # many modern layouts change structure (menus collapse into hamburger
        # icons, columns stack, elements become hidden/overlapped) at
        # different viewport widths. A locator or click coordinate that works
        # at 1280x800 (desktop layout) can silently fail or hit the wrong
        # element at 375x812 (mobile layout) if the window size isn't fixed
        # and asserted at the start of every test run.
        original_size = driver.get_window_size()
        print(f"Original window size: {original_size}")
        driver.set_window_size(1280, 800)
        new_size = driver.get_window_size()
        print(f"New window size: {new_size}")
        assert new_size["width"] == 1280 and new_size["height"] == 800

    finally:
        driver.quit()


if __name__ == "__main__":
    run()
