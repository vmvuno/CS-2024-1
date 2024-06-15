from regex_cs.main import valida_2

def test_valida2_tamanho_inferior_a_8():
    assert not valida_2('#1Asdfg')

def test_valida2_tamanho_igual_a_8():
    assert valida_2(r'#1Asdfgh')

def test_valida2_tamanho_igual_a_12():
    assert valida_2(r'#1ASDFghjklç')

def test_valida2_tamanho_superior_a_12():
    assert not valida_2(r'#1ASDFghjklçq')

def test_valida2_sem_simbolos():
    assert not valida_2(r'11ASDFghjkl')

def test_valida2_simbolo_inicio():
    assert valida_2(r'#1ASDFghjkl')

def test_valida2_simbolo_meio():
    assert valida_2(r'1ASDF¨ghjkl')

def test_valida2_simbolo_fim():
    assert valida_2(r'1ASDFghjkl@')

def test_valida2_sem_letras():
    assert not valida_2(r'123456789¬')

def test_valida2_letra_inicio():
    assert valida_2(r'A123456789¬')

def test_valida2_letra_meio():
    assert valida_2(r'123456C789¬')

def test_valida2_letra_final():
    assert valida_2(r'123456789¬F')

def test_valida2_sem_numero():
    assert not valida_2(r'ASDFghjk¬')

def test_valida2_numero_inicio():
    assert valida_2(r'1ASDFghma¬')

def test_valida2_numero_meio():
    assert valida_2(r'ASDFg5hma¬')

def test_valida2_numero_final():
    assert valida_2(r'ASDFghma¬9')

def test_valida2_apenas_minusculas():
    assert not valida_2(r'asdfghma¬9')