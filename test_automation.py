
import pytest


# @pytest.fixture(scope="module") roda uma vez para cada módulo
@pytest.fixture(scope="function") # roda uma vez para cada função
def preWork():
    print("Pre Workaaaaaaaaaaaaaaaaaa")

def test_increment(preWork):
    print("Initial Check")
    
def test_deincrement(preWork):
    print("Initial ddddd Check")
