"""
Hands-On 6 - Shared pytest fixtures for the Playground test suite.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hands_on_4"))
from setup_test import build_driver, open_page  # noqa: E402


@pytest.fixture(scope="session")
def base_url() -> str:
    """Step 48: session-scoped constant, used instead of hardcoding the URL
    in every test."""
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver():
    """Step 41: function-scoped driver fixture.

    scope='function' spins up a brand-new Chrome instance for every single
    test (setup before yield), and tears it down after (driver.quit() after
    yield) - equivalent to setUp/tearDown in unittest. This guarantees full
    test isolation: no test can leak cookies, local storage, or open tabs
    into the next one. scope='session' would reuse one browser across all
    tests, which is faster but risks tests interfering with each other.
    """
    drv = build_driver(headless=True)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Step 46: capture a screenshot when a test fails.

    request.node (== `item` here) exposes the outcome of each of the three
    phases pytest runs per test (setup/call/teardown) via this hook. We only
    care about the 'call' phase (the actual test body) failing.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            screenshots_dir = Path(__file__).parent / "screenshots"
            screenshots_dir.mkdir(exist_ok=True)
            safe_name = item.name.replace("/", "_").replace("::", "_")
            path = screenshots_dir / f"{safe_name}_failure.png"
            driver.save_screenshot(str(path))
            print(f"\nFailure screenshot saved: {path}")


# Re-export so test files can `from conftest import open_page` if desired
# instead of duplicating the sys.path dance.
__all__ = ["open_page"]
