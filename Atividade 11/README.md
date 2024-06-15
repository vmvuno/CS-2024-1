# Construção de Software - 2024/1
## Prática em Expressões Regulares (RegEx)

1. Considere o material disponibilizado acima a respeito do tema Expressões Regulares.



1. Solicita-se o estudo deste material e fazer o seguinte exercício:
    1. Definir uma expressão regular para validar um login que possua as seguintes restrições:
       1. Possuir tamanho T, onde 5 <= T <= 30;
       1. Possuir letras, números e caracteres especiais.

    1. Definir uma expressão regular para validar uma senha que possua as seguintes restrições:
        1. Possuir tamanho T, onde 8 <= T <= 12;
        1. Possuir letras, números e caracteres especiais.
        1. Possuir pelo menos uma letra maiúscula, um número e uma caracter especial.

1. Implementar a validação destas expressões regulares na liguagem de programação de preferência do aluno.

---

O trabalho foi implementado na linguagem de programação python; abaixo, seguem as instruções para utilização.

Para utilização, é necessário ter o [interpretador python3](https://www.python.org/downloads/) instalado na máquina.

1. Abra o terminal no diretório Atividade 11
2. Crie um ambiente virtual
```sh
python -m venv venv
```

3. Ative o ambiente virtual  
   
Windows
```sh
venv/scripts/activate
```

Linux
```sh
source venv/bin/activate
```

4. Instale as dependências
```sh
pip install -r requirements.txt
```

5. Execute o script diretamente do terminal para receber o resultado das duas funções de validação de senha
```sh
python regex_cs/main.py <senha_a_ser_testada>
```

6. Ou importe as funções de validação para utilizá-las em outros scripts python
```py
from regex_cs.main import valida_1, valida_2
```

7. Para executar os testes das funções de validação, execute, no terminal (caso os testes falhem, certifique-se de que o terminal esteja aberto na pasta raiz do projeto: Atividade 11)
```sh
pytest -v
```
