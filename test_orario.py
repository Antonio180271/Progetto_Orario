import pytest

from orario import Orario


@pytest.fixture
def orario():
    return Orario(10,30,50)


def test_creazione_orario(orario):
    assert orario.ore == 10
    assert orario.minuti == 30
    assert orario.secondi == 50

def test_creazione_orario_ore__non_validi():
    with pytest.raises(ValueError):
        o = Orario(27,30,40)

def test_creazione_orario_minuti__non_validi():
    with pytest.raises(ValueError):
        o = Orario(21,79,40)

def test_creazione_orario_secondi__non_validi():
    with pytest.raises(ValueError):
        o = Orario(21,30,103)

def test_str(orario):
    assert str(orario) == "10:30:50"

def test_str2():
    o = Orario(8,10,50)
    assert str(o) == "08:10:50"

def test_str3():
    o = Orario(15,1,6)
    assert str(o) == "15:01:06"

def test_aggiungi_ore(orario):
    orario.aggiungi_ore(10)
    assert str(orario) == "20:30:50"

def test_aggiunta_ore_eccesso(orario):
    orario.aggiungi_ore(16)
    assert str(orario) == "02:30:50"

def test_aggiunta_ore_eccesso2(orario):
    orario.aggiungi_ore(42)
    assert str(orario) == "04:30:50"

def test_aggiunta_secondi(orario):
    orario.aggiungi_secondi(1000)
    assert str(orario) == "10:47:30"

def test_aggiunta_secondi2(orario):
    orario.aggiungi_secondi(100000)
    assert str(orario) == "14:17:30"


# def test_deposito_valido(conto):
#     conto.deposita(50)
#
#     assert conto.saldo_attuale() == 150
#
#
# def test_deposito_negativo(conto):
#     with pytest.raises(ValueError):
#         conto.deposita(-20)
#
#
# def test_prelievo_valido(conto):
#     conto.preleva(30)
#
#     assert conto.saldo_attuale() == 70
#
#
# def test_prelievo_eccessivo(conto):
#     with pytest.raises(ValueError):
#         conto.preleva(200)
#
#
# def test_cambia_intestatario_con_spazio(conto):
#     conto.cambia_nome("Geppetto")
#
#     assert conto.intestatario == "Geppetto "
#
#
# def test_str(conto):
#     assert str(conto) == "Conto di Mario Rossi - Saldo: €100.00"