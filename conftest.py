import pytest
import os
import pytest_html

def pytest_configure(config):
    # Garante que a variável extra existe
    config._metadata = {}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Executa o restante do hook do pytest
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        extra = getattr(report, 'extra', [])
        report.extra = extra

        # Adiciona screenshot automaticamente se existir 'screenshot_auto' como atributo
        screenshot_path = getattr(item, 'screenshot_auto', None)
        if screenshot_path and os.path.exists(screenshot_path):
            rel_path = os.path.relpath(screenshot_path)
            extra.append(pytest_html.extras.image(rel_path))
        report.extra = extra

# Adiciona uma coluna no relatório para screenshots
def pytest_html_results_table_header(cells):
    cells.insert(1, pytest_html.html.th('Screenshot'))

def pytest_html_results_table_row(report, cells):
    extra = getattr(report, 'extra', [])
    for e in extra:
        if e['format'] == 'image':
            cells.insert(1, pytest_html.html.td(pytest_html.html.img(src=e['content'], height="100")))
            return
    cells.insert(1, pytest_html.html.td(''))
