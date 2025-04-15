from playwright.sync_api import sync_playwright
from contextlib import contextmanager

@contextmanager
def iniciar_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            yield page, browser
        finally:
            browser.close()