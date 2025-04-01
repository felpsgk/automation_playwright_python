from playwright.sync_api import sync_playwright
from contextlib import contextmanager

@contextmanager
def iniciar_browser():
    """Inicia o navegador, contexto e página e garante o fechamento adequado"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            yield page, browser
        finally:
            browser.close()