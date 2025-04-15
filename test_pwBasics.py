from playwright.sync_api import sync_playwright, expect
from base.browser import iniciar_browser
from base.pageBase import navegarPara, preencherCampo, clicarBotaoPorTexto, esperaPorTexto, printTela
import pytest

@pytest.mark.parametrize("usuario,senha", [
    ("ua_automasuper", "Ab147258369@"),
    ("ua_automasuper", "Ab147258369@"),
    ("ua_automasuper", "Ab147258369@"),
])
def test_login(request, usuario, senha):
    with iniciar_browser() as (page, browser):
        try:
            navegarPara(page, "https://apphml.unimedbh.com.br/unimedagenda")
            printTela(page, "link.png", request)
            preencherCampo(page, "#username", usuario)
            printTela(page, "login.png", request)
            preencherCampo(page, "#password", senha)
            clicarBotaoPorTexto(page, "Entrar")
            printTela(page, "entrar.png", request)
            esperaPorTexto(page, "Parabéns, seus dados foram validados com sucesso", 7000)
            printTela(page, "sucesso.png", request)
        except Exception as e:
            printTela(page, "screenshot_error.png", request)
            raise e
