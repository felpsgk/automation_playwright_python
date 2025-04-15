from playwright.sync_api import expect

def print(page, pathh):
    page.screenshot(path=pathh)


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
