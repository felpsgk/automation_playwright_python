from playwright.sync_api import sync_playwright, expect
from base.browser import iniciar_browser
from base.pageBase import navegarPara, preencherCampo, clicarBotaoPorTexto, esperaPorTextoContido, printTela
import pytest

@pytest.mark.parametrize("usuario,senha", [
    ("ua_automasuper", "Ab147258369@"),
    ("ua_automasuper", "Ab147258369@"),
    ("ua_automasuper", "Ab147258369@"),
])
def test_login(usuario, senha):
    with iniciar_browser() as (page, browser):
        try:
            navegarPara(page, "https://apphml.unimedbh.com.br/unimedagenda")
            printTela(page, "link.png")
            preencherCampo(page, "#username", usuario)
            printTela(page, "login.png")
            preencherCampo(page, "#password", senha)
            clicarBotaoPorTexto(page, "Entrar")
            printTela(page, "entrar.png")
            esperaPorTextoContido(page, "dados foram validados com sucesso", 4000)
            printTela(page, "sucesso.png")
        except Exception as e:
            printTela(page, "screenshot_error.png")
            raise e
