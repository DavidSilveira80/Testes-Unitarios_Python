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


def cripto_char(char: str, flag: str, step: int) -> str:
    if flag == 'r':
        cod_ascii = ord(char)
        char_criptografado = chr(cod_ascii + step)
    elif flag == 'l':
        cod_ascii = ord(char)
        char_criptografado = chr(cod_ascii - step)

    return char_criptografado


def cripto_minusculas_maiusculas(texto_entrada: str, flag: str, step: int) -> str:
    primeira_pasada_minusculas_maiusculas = ''
    for letra in texto_entrada:
        if letra.isalpha():
            primeira_pasada_minusculas_maiusculas += cripto_char(letra, flag, step)
        else:
            primeira_pasada_minusculas_maiusculas += letra

    return primeira_pasada_minusculas_maiusculas
