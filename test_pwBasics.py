from playwright.sync_api import sync_playwright, expect
from base.browser import iniciar_browser
from base.pageBase import navegarPara, preencherCampo, clicarBotaoPorTexto, esperaPorTexto, printTela

def test_login(request):
    with iniciar_browser() as (page, browser):
        try:
            navegarPara(page, "https://apphml.unimedbh.com.br/unimedagenda")
            printTela(page, "prints/link.png", request)  # Captura um print inicial
            preencherCampo(page, "#username", "ua_automasuper")
            printTela(page, "prints/login.png", request)  # Captura um print inicial
            preencherCampo(page, "#password", "Ab147258369@")
            clicarBotaoPorTexto(page, "Entrar")
            printTela(page, "prints/entrar.png", request)  # Captura um print inicial
            esperaPorTexto(page, "Parabéns, seus dados foram validados com sucesso", 7000)
            printTela(page, "prints/sucesso.png", request)  # Captura um print inicial
        except Exception as e:
            # Captura um print em caso de erro
            printTela(page, "prints/screenshot_error.png", request)
            raise e  # Relança o erro após salvar o print

def test_login2(request):
    with iniciar_browser() as (page, browser):
        try:
            navegarPara(page, "https://apphml.unimedbh.com.br/unimedagenda")
            printTela(page, "prints/link.png", request)  # Captura um print inicial
            preencherCampo(page, "#username", "ua_automasuper")
            printTela(page, "prints/login.png", request)  # Captura um print inicial
            preencherCampo(page, "#password", "Ab147258369@")
            clicarBotaoPorTexto(page, "Entrar")
            printTela(page, "prints/entrar.png", request)  # Captura um print inicial
            esperaPorTexto(page, "Parabéns, seus dados foram validados com sucesso", 7000)
            printTela(page, "prints/sucesso.png", request)  # Captura um print inicial
        except Exception as e:
            # Captura um print em caso de erro
            printTela(page, "prints/screenshot_error.png", request)
            raise e  # Relança o erro após salvar o print

def test_login3(request):
    with iniciar_browser() as (page, browser):
        try:
            navegarPara(page, "https://apphml.unimedbh.com.br/unimedagenda")
            printTela(page, "prints/link.png", request)  # Captura um print inicial
            preencherCampo(page, "#username", "ua_automasuper")
            printTela(page, "prints/login.png", request)  # Captura um print inicial
            preencherCampo(page, "#password", "Ab147258369@")
            clicarBotaoPorTexto(page, "Entrar")
            printTela(page, "prints/entrar.png", request)  # Captura um print inicial
            esperaPorTexto(page, "Parabéns, seus dados foram validados com sucesso", 7000)
            printTela(page, "prints/sucesso.png", request)  # Captura um print inicial
        except Exception as e:
            # Captura um print em caso de erro
            printTela(page, "prints/screenshot_error.png", request)
            raise e  # Relança o erro após salvar o print
