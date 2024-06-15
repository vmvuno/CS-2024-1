import re
import sys

def valida_1(senha: str) -> bool:
    """Primeira função de validação

    Testa se a senha passada como argumento atende aos critérios:
        - Possuir tamanho T, onde 5 <= T <= 30;
        - Possuir letras, números e caracteres especiais.
    """ 

    return bool(re.search(r'^(?=.*[A-Za-z]+)(?=.*\d+)(?=.*[!@#$%¨&*£¢=+¬\-]+).{5,30}$', senha))

def valida_2(senha: str) -> bool:
    """Segunda função de validação

    Testa se a senha passada como argumento atende aos critérios:
        Possuir tamanho T, onde 8 <= T <= 12;
        Possuir letras, números e caracteres especiais.
        Possuir pelo menos uma letra maiúscula, um número e uma caracter especial.
    """ 
    return bool(re.search(r'^(?=.*[A-Z]+)(?=.*[a-z]*)(?=.*\d+)(?=.*[!@#$%¨&*£¢=+¬\-]+).{8,12}$', senha))

if __name__== '__main__':
    senha = sys.argv[1]

    print(f'Resultado da função de validação 1: {valida_1(senha)}')
    print(f'Resultado da função de validação 2: {valida_2(senha)}')