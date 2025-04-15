from playwright.sync_api import expect

def printTela(page, pathh):
    page.screenshot(path=pathh)

def navegarPara(page, link):
    page.goto(link)

def preencherCampo(page, campo, texto):
    page.fill(campo, texto)

def clicarBotaoPorTexto(page, texto):
    page.get_by_role("button",name=texto).click()

def esperaPorTexto(page, texto, timeout):
    expect(page.locator("text=" + texto)).to_be_visible(timeout=timeout)

def esperaPorTextoContido(page, texto_parcial, tempo):
    """Espera até que um elemento na página contenha o texto parcial especificado."""
    locator = page.locator(f'text={texto_parcial}')
    expect(locator).to_be_visible(timeout=tempo)
    
def fecharNavegador(browser):
    browser.close()
