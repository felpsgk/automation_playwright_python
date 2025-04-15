from playwright.sync_api import expect
import os
import pytest_html
from datetime import datetime

def printTela(page, path_base, request=None):
    os.makedirs("prints", exist_ok=True)
    test_name = request.node.name if request else "screenshot"
    timestamp = datetime.now().strftime("%H%M%S%f")
    filename = f"prints/{test_name}_{timestamp}_{os.path.basename(path_base)}"
    page.screenshot(path=filename)
    if request:
        rel_path = os.path.relpath(filename)
        request.node.extra = getattr(request.node, "extra", [])
        request.node.extra.append(pytest_html.extras.image(rel_path))

def navegarPara(page, link):
    page.goto(link)

def preencherCampo(page, campo, texto):
    page.fill(campo, texto)

def clicarBotaoPorTexto(page, texto):
    page.get_by_role("button",name=texto).click()

def esperaPorTexto(page, texto, timeout):
    expect(page.locator("text=" + texto)).to_be_visible(timeout=timeout)

def fecharNavegador(browser):
    browser.close()
