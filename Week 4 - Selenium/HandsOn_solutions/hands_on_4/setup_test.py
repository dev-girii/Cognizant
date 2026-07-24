"""
Hands-On 4 / Task 1 - Selenium Architecture and Environment Setup
==================================================================

Selenium component architecture:

1. WebDriver
   The core API this script talks to. WebDriver is a set of language bindings
   (here, the `selenium` Python package) plus a browser-specific driver binary
   (chromedriver) that translates WebDriver commands into the browser's native
   automation protocol (Chrome DevTools Protocol / W3C WebDriver protocol).
   Python code -> chromedriver (a small HTTP server) -> real Chrome instance.
   Each `driver.find_element(...)`, `.click()`, `.get(url)` call is an HTTP
   request/response round trip between the Python process and chromedriver.

2. Selenium Grid
   Solves the "I need to run these tests on many browsers/OSes/machines at
   once" problem. A Grid Hub distributes test sessions across registered
   Nodes (each running a different browser/version/OS combination), enabling
   parallel and cross-browser execution instead of running every test
   sequentially on one local machine.

3. Selenium IDE
   A browser extension for record-and-playback test creation. You click
   through the app in the browser, and it records each action as a Selenium
   command, then can export that recording as runnable code (e.g., a Python
   WebDriver script). Useful for quickly bootstrapping a script or for
   non-programmers to capture a flow, but not a substitute for a maintained
   POM-based suite (Hands-On 7).
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def build_driver(headless: bool = False) -> webdriver.Chrome:
    options = Options()
    if headless:
        # Modern headless mode - renders exactly like a normal window,
        # just without displaying it on screen.
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,800")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Task 1, Step 26: implicit wait.
    # driver.implicitly_wait(10) tells the driver to poll the DOM for up to
    # 10 seconds *every single time* find_element/find_elements is called and
    # the element isn't immediately present. This is bad practice as a global
    # default because:
    #   1. It applies uniformly to every locator call in the whole script,
    #      even ones that should fail fast (e.g., checking an element is
    #      ABSENT) - those now always take the full 10s to time out.
    #   2. It can silently mask real timing bugs: a page that should load in
    #      200ms but takes 9s due to a backend regression still "passes"
    #      within the implicit wait window, hiding a performance regression.
    #   3. Mixing implicit waits with explicit WebDriverWait calls (Hands-On 5)
    #      causes unpredictable, compounding wait times, because the implicit
    #      wait still fires inside every find_element the explicit wait uses
    #      internally.
    # Explicit waits (WebDriverWait + expected_conditions) are preferred
    # because they target one condition at a time, with an intent that's
    # visible in the test code itself.
    driver.implicitly_wait(10)
    return driver


def open_page(driver: webdriver.Chrome, url: str, timeout: int = 15) -> None:
    """Navigate and wait for the page to finish loading (readyState complete).

    driver.get() returns once the initial HTML document load fires, but on
    a JS-heavy site (this Playground is a Next.js app) the interactive
    widgets' click handlers attach asynchronously after that. Clicking a
    button immediately after driver.get() can hit the DOM before its
    listener is wired up, so the click "succeeds" but nothing visibly
    happens - a real flaky-test cause (see Hands-On 3, Task 1, Step 20).
    Waiting for document.readyState == 'complete' closes that race.
    """
    driver.get(url)
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def run() -> None:
    driver = build_driver(headless=False)
    try:
        driver.get(PLAYGROUND_URL)
        print(f"Page title: {driver.title}")
    finally:
        driver.quit()


def run_headless() -> None:
    """Task 1, Step 27: same script, but headless - title should still print
    correctly with no visible browser window."""
    driver = build_driver(headless=True)
    try:
        driver.get(PLAYGROUND_URL)
        print(f"[headless] Page title: {driver.title}")
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
    run_headless()
