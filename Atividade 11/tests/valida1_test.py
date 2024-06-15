from regex_cs.main import valida_1

def test_valida1_tamanho_inferior_a_5():
    assert not valida_1('#1As')

def test_valida1_tamanho_igual_a_5():
    assert valida_1(r'#1Asd')

def test_valida1_tamanho_igual_a_30():
    assert valida_1(r'#1ASDFghjklçqwertyuiopzxcvbnma')

def test_valida1_tamanho_superior_a_30():
    assert not valida_1(r'#1ASDFghjklçqwertyuiopzxcvbnmaa')

def test_valida1_sem_simbolos():
    assert not valida_1(r'11ASDFghjklçqwertyuiopzcvbnma')

def test_valida1_simbolo_inicio():
    assert valida_1(r'#1ASDFghjklçqwertyuiopzxcvbnma')

def test_valida1_simbolo_meio():
    assert valida_1(r'1ASDFghjklçqwerty%uiopzxcvbnma')

def test_valida1_simbolo_fim():
    assert valida_1(r'1ASDFghjklçqwertyuiopzxcvbnma¬')

def test_valida1_sem_letras():
    assert not valida_1(r'123456789¬')

def test_valida1_letra_inicio():
    assert valida_1(r'a123456789¬')

def test_valida1_letra_meio():
    assert valida_1(r'123456b789¬')

def test_valida1_letra_final():
    assert valida_1(r'123456789¬z')

def test_valida1_sem_numero():
    assert not valida_1(r'ASDFghjklçqwertyuiopzxcvbnma¬')

def test_valida1_numero_inicio():
    assert valida_1(r'1ASDFghjcvbnma¬')

def test_valida1_numero_meio():
    assert valida_1(r'ASDFghj2cvbnma¬')

def test_valida1_numero_final():
    assert valida_1(r'ASDFghjcvbnma¬9')