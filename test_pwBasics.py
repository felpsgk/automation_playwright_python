from playwright.sync_api import sync_playwright, expect
from base.browser import iniciar_browser
from base.pageBase import navegarPara, preencherCampo, clicarBotaoPorTexto, esperaPorTexto, printTela

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
        try:
            navegarPara(page, "https://apphml.unimedbh.com.br/unimedagenda")
            printTela(page, "C:\ProgramData\Jenkins\slave\workspace\python\link.png")  # Captura um print inicial
            preencherCampo(page, "#username", "ua_automasuper")
            printTela(page, "C:\ProgramData\Jenkins\slave\workspace\python\login.png")  # Captura um print inicial
            preencherCampo(page, "#password", "Ab147258369@")
            clicarBotaoPorTexto(page, "Entrar")
            printTela(page, "C:\ProgramData\Jenkins\slave\workspace\python\entrar.png")  # Captura um print inicial
            esperaPorTexto(page, "Parabéns, seus dados foram validados com sucesso", 7000)
            printTela(page, "C:\ProgramData\Jenkins\slave\workspace\python\sucesso.png")  # Captura um print inicial
        except Exception as e:
            # Captura um print em caso de erro
            page.screenshot(path="C:\ProgramData\Jenkins\slave\workspace\python\screenshot_error.png")
            raise e  # Relança o erro após salvar o print
