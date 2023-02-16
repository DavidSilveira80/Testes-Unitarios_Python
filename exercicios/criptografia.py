"""
                          beecrowd | 1024
                            Criptografia
Solicitaram para que você construisse um programa
simples de criptografia.
Este programa deve possibilitar enviar mensagens
codificadas sem que alguém consiga lê-las.
O processo é muito simples.
São feitas três passadas no texto inteiro.

Na primeira passada, somente caracteres que
sejam letras minúsculas e maiúsculas devem ser
deslocadas 3 posições para a direita,
segundo a tabela ASCII:

letra 'a' deve virar letra 'd',
letra 'y' deve virar caractere '|'

e assim sucessivamente.
Na segunda passada,

a linha deverá ser invertida.

Na terceira e última passada, todo e qualquer caractere a partir
da metade em diante (truncada) devem ser deslocados uma posição
para a esquerda na tabela ASCII.
Neste caso,

'b' vira 'a' e
'a' vira '`'.

Por exemplo, se a entrada for

“Texto #3”

o primeiro processamento sobre esta entrada
deverá produzir

“Wh{wr #3”.

O resultado do segundo processamento inverte os
caracteres e produz

“3# rw{hW”

Por último, com
o deslocamento dos caracteres da metade em diante,
o resultado final deve ser

“3# rvzgV”

4
Texto #3                 3# rvzgV
abcABC1                  1FECedc
vxpdylY .ph              ks. \n{frzx
vv.xwfxo.fd              gi.r{hyz-xx
"""


def criptografa_char(char: str, flag: str, step: int) -> str:
    if flag == 'r':
        cod_ascii = ord(char)
        char_criptografado = chr(cod_ascii + step)
    elif flag == 'l':
        cod_ascii = ord(char)
        char_criptografado = chr(cod_ascii - step)

    return char_criptografado


def criptografa_minusculas_maiusculas(texto_entrada: str, flag: str, step: int) -> str:
    primeira_pasada_minusculas_maiusculas = ''
    for letra in texto_entrada:
        if letra.isalpha():
            primeira_pasada_minusculas_maiusculas += criptografa_char(letra, flag, step)
        else:
            primeira_pasada_minusculas_maiusculas += letra

    return primeira_pasada_minusculas_maiusculas


def inverte_texto(texto: str) -> str:
    texto_invertido = ''
    for index in range(len(texto)):
        texto_invertido += texto[-(index + 1)]

    return texto_invertido


def divide_string(texto: str) -> int:
    metade_da_string = len(texto) // 2
    return metade_da_string


def particiona_texto(texto: str, flag_metade: int) -> str:
    if flag_metade == 1:
        metade_texto = texto[:divide_string(texto)]
    elif flag_metade == 2:
        metade_texto = texto[divide_string(texto):]
    return metade_texto


def tres_requisitos(texto):
    # Primeiro e segundo requisito satisfeito
    primeira_passada = criptografa_minusculas_maiusculas(texto, 'r', 3)
    segunda_passada = inverte_texto(primeira_passada)

    # Processamento e conclusão do 3 e ultimo requisito
    primeira_metade_do_texto = particiona_texto(segunda_passada, 1)
    segunda_metade_do_texto = particiona_texto(segunda_passada, 2)

    criptografada_segunda_metdade_do_texto_1_esquerda = ''
    for char in segunda_metade_do_texto:
        criptografada_segunda_metdade_do_texto_1_esquerda += criptografa_char(char, 'l', 1)

    return primeira_metade_do_texto + criptografada_segunda_metdade_do_texto_1_esquerda


"""
Aqui vai a aplicação do desafio para ser enviado para o Juíz online beecrowd

N = int(input())
contador = 1

while contador <= N:
    texto = input()
    print(tres_requisitos(texto))
    contador += 1
"""