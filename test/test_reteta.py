import json
import pytest
from bucatarie import Bucatarie,Reteta
def bucatarie():
    bucatarie = Bucatarie()
    bucatarie.inventar = {'oua': 6, 'lapte': 455}
    return bucatarie
def test_adaugare_produs(bucatarie):
    bucatarie.adauga_produs('oua', 4)
    assert bucatarie.inventar['oua'] == 10
    bucatarie.adauga_produs('faina', 600)
    assert bucatarie.inventar['faina'] == 600
def test_scadere_produs(bucatarie):
    bucatarie.scadere_produs('lapte', 400)
    assert bucatarie.inventar['lapte'] == 55
    bucatarie.scadere_produs('faina', 400)
    assert 'faina' not in bucatarie.inventar
@pytest.fixture
def reteta():
    reteta = Reteta('Clatite', [{'nume': 'oua', 'cantitate': 6}, {'nume': 'lapte', 'cantitate': 400}])
    return reteta
def test_pregatire_reteta(bucatarie, reteta):
    reteta.pregatire(bucatarie)
    assert bucatarie.inventar['oua'] == 0
    assert bucatarie.inventar['lapte'] == 55
    assert bucatarie.inventar['faina'] == 600  # Fails, since faina wasn't added yet
if __name__ == '__main__':
    pytest.main()