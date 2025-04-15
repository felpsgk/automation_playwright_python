from playwright.sync_api import expect
import os
import pytest_html

def printTela(page, path, request=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    page.screenshot(path=path)
    if request:
        rel_path = os.path.relpath(path)
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
