"""
                                                beecrowd | 2310
                                                    Voleibol
                                        Por Leonardo Fernandes, IFSC BR Brazil
                                                   Timelimit: 1
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe.
A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques
cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques
tiveram sucesso (resultaram em pontos).
Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

Entrada

A entrada é dada pelo número de
jogadores N (1 ≤ N ≤ 100), seguido pelo nome de cada um dos jogadores.
Abaixo do nome de cada jogador,
seguem duas linhas com três inteiros cada.
Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000)
representam a quantidade de tentativas de saques, bloqueios e ataques e
na segunda linha, S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A)
com o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

Saída

A saída deve conter o percentual total de saques, bloqueios e ataques do t
ime todo que resultaram em pontos, conforme mostrado no exemplo.

3
Renan                                         Exemplo de Saída
10 20 12                                     Pontos de Saque: 19.05 %.
1 10 9                                       Pontos de Bloqueio: 63.33 %.
Jonas                                        Pontos de Ataque: 75.00 %.
8 7 1
2 7 0
Edson
3 3 3
1 2 3

"""


def coleta_tentativas_pontos(tentativas_pontos: list, flag: str) -> int:
    if flag == 's':
        tentativa_ponto = tentativas_pontos[0]
    elif flag == 'b':
        tentativa_ponto = tentativas_pontos[1]
    elif flag == 'a':
        tentativa_ponto = tentativas_pontos[2]

    return tentativa_ponto


if __name__ == '__main__':

    N = int(input())

    saque_tentativa = bloqueio_tentativa = ataque_tentativa = 0
    saque_ponto = bloqueio_ponto = ataque_ponto = 0
    contador = 1
    while contador <= N:
        nome = input()
        tentativas = [int(i) for i in input().split()]
        pontos = [int(i) for i in input().split()]

        saque_tentativa += coleta_tentativas_pontos(tentativas, 's')
        bloqueio_tentativa += coleta_tentativas_pontos(tentativas, 'b')
        ataque_tentativa += coleta_tentativas_pontos(tentativas, 'a')

        saque_ponto += coleta_tentativas_pontos(pontos, 's')
        bloqueio_ponto += coleta_tentativas_pontos(pontos, 'b')
        ataque_ponto += coleta_tentativas_pontos(pontos, 'a')

        contador += 1

    porcentagem_saque = (saque_ponto / saque_tentativa) * 100
    porcentagem_bloqueio = (bloqueio_ponto / bloqueio_tentativa) * 100
    porcentagem_ataque = (ataque_ponto / ataque_tentativa) * 100

    print(f'Pontos de Saque: {porcentagem_saque:.2f} %.')
    print(f'Pontos de Bloqueio: {porcentagem_bloqueio:.2f} %.')
    print(f'Pontos de Ataque: {porcentagem_ataque:.2f} %.')
