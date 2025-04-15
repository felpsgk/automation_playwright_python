from playwright.sync_api import sync_playwright, expect
from base.browser import iniciar_browser
from base.pageBase import navegarPara, preencherCampo, clicarBotaoPorTexto, esperaPorTexto, fecharNavegador

# def test_V1pwBasics():
#     with sync_playwright() as playwright:  # Usando o contexto manual para evitar a fixture
#         browser = playwright.chromium.launch(headless=False)  # Abrir o navegador
#         context = browser.new_context()  # Criar um contexto de navegação (incógnito)
#         page = context.new_page()  # Abrir uma nova aba
#         page.goto("https://apphml.unimedbh.com.br/unimedagenda")

#         page.fill("#username", "ua_automasuper")
#         page.fill("#password", "Ab147258369@")

#         page.locator('button:text("Entrar")').click()

#         expect(page.locator("text=Parabéns, seus dados foram validados com sucesso")).to_be_visible(timeout=3000)

#         browser.close()  # Fechar o navegador

def test_login():

    with iniciar_browser() as (page, browser):
        navegarPara(page, "https://apphml.unimedbh.com.br/unimedagenda")
        preencherCampo(page, "#username", "ua_automasuper")
        preencherCampo(page, "#password", "Ab147258369@")
        clicarBotaoPorTexto(page, "Entrar")
        esperaPorTexto(page, "Parabéns, seus dados foram validados com sucesso", 7000)