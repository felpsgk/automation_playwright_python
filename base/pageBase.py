from playwright.sync_api import expect
import os
import pytest

def printTela(page, caminho_arquivo, request=None):
    page.screenshot(path=caminho_arquivo)
    
    if request:
        if hasattr(request.config, "_html") and request.node:
            extra = getattr(request.node, "extra", [])
            rel_path = os.path.relpath(caminho_arquivo)
            extra.append(pytest_html.extras.image(rel_path))
            request.node.extra = extra



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
