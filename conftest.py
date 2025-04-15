import pytest

def pytest_configure(config):
    # Garante que a variável extra existe
    config._metadata = {}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Executa o restante do hook do pytest
    outcome = yield
    report = outcome.get_result()

    # Se for uma falha ou sucesso e o objeto tiver extras, injeta no relatório
    if report.when == 'call':
        extra = getattr(report, 'extra', [])
        report.extra = extra
