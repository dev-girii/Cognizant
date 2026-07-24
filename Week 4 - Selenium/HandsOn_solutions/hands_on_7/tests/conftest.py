"""
Hands-On 7 - Shared pytest fixtures for the POM-based Playground test suite.
"""

import sys
from pathlib import Path

import pytest

HANDS_ON_7_ROOT = Path(__file__).resolve().parents[1]
HANDS_ON_4_ROOT = HANDS_ON_7_ROOT.parent / "hands_on_4"
sys.path.insert(0, str(HANDS_ON_7_ROOT))  # for `pages` package imports
sys.path.insert(0, str(HANDS_ON_4_ROOT))  # for build_driver

from setup_test import build_driver  # noqa: E402


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver():
    drv = build_driver(headless=True)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Same screenshot-on-failure hook as Hands-On 6, carried over."""
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
