from playwright.sync_api import sync_playwright, expect
from base.browser import iniciar_browser
from base.pageBase import navegarPara, preencherCampo, clicarBotaoPorTexto, esperaPorTexto, printTela

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

def test_login2():
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

def test_login3():
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
