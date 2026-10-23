import os
import random

solucaoLinha1Coluna1 = 5
solucaoLinha1Coluna2 = 3
solucaoLinha1Coluna3 = 4
solucaoLinha1Coluna4 = 6
solucaoLinha1Coluna5 = 7
solucaoLinha1Coluna6 = 8
solucaoLinha1Coluna7 = 9
solucaoLinha1Coluna8 = 1
solucaoLinha1Coluna9 = 2

solucaoLinha2Coluna1 = 6
solucaoLinha2Coluna2 = 7
solucaoLinha2Coluna3 = 2
solucaoLinha2Coluna4 = 1
solucaoLinha2Coluna5 = 9
solucaoLinha2Coluna6 = 5
solucaoLinha2Coluna7 = 3
solucaoLinha2Coluna8 = 4
solucaoLinha2Coluna9 = 8

solucaoLinha3Coluna1 = 1
solucaoLinha3Coluna2 = 9
solucaoLinha3Coluna3 = 8
solucaoLinha3Coluna4 = 3
solucaoLinha3Coluna5 = 4
solucaoLinha3Coluna6 = 2
solucaoLinha3Coluna7 = 5
solucaoLinha3Coluna8 = 6
solucaoLinha3Coluna9 = 7

solucaoLinha4Coluna1 = 8
solucaoLinha4Coluna2 = 5
solucaoLinha4Coluna3 = 9
solucaoLinha4Coluna4 = 7
solucaoLinha4Coluna5 = 6
solucaoLinha4Coluna6 = 1
solucaoLinha4Coluna7 = 4
solucaoLinha4Coluna8 = 2
solucaoLinha4Coluna9 = 3

solucaoLinha5Coluna1 = 4
solucaoLinha5Coluna2 = 2
solucaoLinha5Coluna3 = 6
solucaoLinha5Coluna4 = 8
solucaoLinha5Coluna5 = 5
solucaoLinha5Coluna6 = 3
solucaoLinha5Coluna7 = 7
solucaoLinha5Coluna8 = 9
solucaoLinha5Coluna9 = 1

solucaoLinha6Coluna1 = 7
solucaoLinha6Coluna2 = 1
solucaoLinha6Coluna3 = 3
solucaoLinha6Coluna4 = 9
solucaoLinha6Coluna5 = 2
solucaoLinha6Coluna6 = 4
solucaoLinha6Coluna7 = 8
solucaoLinha6Coluna8 = 5
solucaoLinha6Coluna9 = 6

solucaoLinha7Coluna1 = 9
solucaoLinha7Coluna2 = 6
solucaoLinha7Coluna3 = 1
solucaoLinha7Coluna4 = 5
solucaoLinha7Coluna5 = 3
solucaoLinha7Coluna6 = 7
solucaoLinha7Coluna7 = 2
solucaoLinha7Coluna8 = 8
solucaoLinha7Coluna9 = 4

solucaoLinha8Coluna1 = 2
solucaoLinha8Coluna2 = 8
solucaoLinha8Coluna3 = 7
solucaoLinha8Coluna4 = 4
solucaoLinha8Coluna5 = 1
solucaoLinha8Coluna6 = 9
solucaoLinha8Coluna7 = 6
solucaoLinha8Coluna8 = 3
solucaoLinha8Coluna9 = 5

solucaoLinha9Coluna1 = 3
solucaoLinha9Coluna2 = 4
solucaoLinha9Coluna3 = 5
solucaoLinha9Coluna4 = 2
solucaoLinha9Coluna5 = 8
solucaoLinha9Coluna6 = 6
solucaoLinha9Coluna7 = 1
solucaoLinha9Coluna8 = 7
solucaoLinha9Coluna9 = 9

gab_base = [
    [
        solucaoLinha1Coluna1,
        solucaoLinha1Coluna2,
        solucaoLinha1Coluna3,
        solucaoLinha1Coluna4,
        solucaoLinha1Coluna5,
        solucaoLinha1Coluna6,
        solucaoLinha1Coluna7,
        solucaoLinha1Coluna8,
        solucaoLinha1Coluna9,
    ],
    [
        solucaoLinha2Coluna1,
        solucaoLinha2Coluna2,
        solucaoLinha2Coluna3,
        solucaoLinha2Coluna4,
        solucaoLinha2Coluna5,
        solucaoLinha2Coluna6,
        solucaoLinha2Coluna7,
        solucaoLinha2Coluna8,
        solucaoLinha2Coluna9,
    ],
    [
        solucaoLinha3Coluna1,
        solucaoLinha3Coluna2,
        solucaoLinha3Coluna3,
        solucaoLinha3Coluna4,
        solucaoLinha3Coluna5,
        solucaoLinha3Coluna6,
        solucaoLinha3Coluna7,
        solucaoLinha3Coluna8,
        solucaoLinha3Coluna9,
    ],
    [
        solucaoLinha4Coluna1,
        solucaoLinha4Coluna2,
        solucaoLinha4Coluna3,
        solucaoLinha4Coluna4,
        solucaoLinha4Coluna5,
        solucaoLinha4Coluna6,
        solucaoLinha4Coluna7,
        solucaoLinha4Coluna8,
        solucaoLinha4Coluna9,
    ],
    [
        solucaoLinha5Coluna1,
        solucaoLinha5Coluna2,
        solucaoLinha5Coluna3,
        solucaoLinha5Coluna4,
        solucaoLinha5Coluna5,
        solucaoLinha5Coluna6,
        solucaoLinha5Coluna7,
        solucaoLinha5Coluna8,
        solucaoLinha5Coluna9,
    ],
    [
        solucaoLinha6Coluna1,
        solucaoLinha6Coluna2,
        solucaoLinha6Coluna3,
        solucaoLinha6Coluna4,
        solucaoLinha6Coluna5,
        solucaoLinha6Coluna6,
        solucaoLinha6Coluna7,
        solucaoLinha6Coluna8,
        solucaoLinha6Coluna9,
    ],
    [
        solucaoLinha7Coluna1,
        solucaoLinha7Coluna2,
        solucaoLinha7Coluna3,
        solucaoLinha7Coluna4,
        solucaoLinha7Coluna5,
        solucaoLinha7Coluna6,
        solucaoLinha7Coluna7,
        solucaoLinha7Coluna8,
        solucaoLinha7Coluna9,
    ],
    [
        solucaoLinha8Coluna1,
        solucaoLinha8Coluna2,
        solucaoLinha8Coluna3,
        solucaoLinha8Coluna4,
        solucaoLinha8Coluna5,
        solucaoLinha8Coluna6,
        solucaoLinha8Coluna7,
        solucaoLinha8Coluna8,
        solucaoLinha8Coluna9,
    ],
    [
        solucaoLinha9Coluna1,
        solucaoLinha9Coluna2,
        solucaoLinha9Coluna3,
        solucaoLinha9Coluna4,
        solucaoLinha9Coluna5,
        solucaoLinha9Coluna6,
        solucaoLinha9Coluna7,
        solucaoLinha9Coluna8,
        solucaoLinha9Coluna9,
    ],
]

m = list(range(1, 10))
random.shuffle(m)

solucao = []
for l in range(9):
    linha_sol = []
    for c in range(9):
        val = gab_base[l][c]
        if val != 0:
            linha_sol.append(m[val])
        else:
            linha_sol.append(0)
    solucao.append(linha_sol)

mascara = [
    [1, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1],
]

tabuleiro = []
fixos = []

for l in range(9):
    linha_tab = []
    linha_fix = []
    for c in range(9):
        if mascara[l][c] == 1 and solucao[l][c] != 0:
            linha_tab.append(solucao[l][c])
            linha_fix.append(True)
        else:
            linha_tab.append(0)
            linha_fix.append(False)
    tabuleiro.append(linha_tab)
    fixos.append(linha_fix)

mensagem_erro = ""

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 37)
    print("            SUDOKU CLI")
    print("=" * 37)
    if mensagem_erro:
        print(f"\n[!] {mensagem_erro}")
        mensagem_erro = ""
    print()

    print("    1 2 3   4 5 6   7 8 9 (Coluna)")
    print("  +-------+-------+-------+")
    for i in range(9):
        linha_str = f"{i + 1} | "
        for j in range(9):
            val = tabuleiro[i][j]
            char = str(val) if val != 0 else "."
            linha_str += char + " "
            if (j + 1) % 3 == 0:
                linha_str += "| "
        print(linha_str)
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")

    completo = True
    for l in range(9):
        for c in range(8):
            if tabuleiro[l][c] == 0:
                completo = False
                break
        if not completo:
            break

    if completo:
        print("\n PARABÉNS! Você completou o Sudoku com sucesso!\n")
        break

    print("\nDigite no formato: LINHA COLUNA VALOR (ex: 1 3 4)")
    print("Para apagar um número inserido, use valor 0 (ex: 1 3 0)")
    entrada = input("> ").strip().split()

    if len(entrada) != 3:
        mensagem_erro = "Entrada inválida! Insira exatamente 3 números separados por espaço."
        continue

    valido = True
    for item in entrada:
        if not item.isdigit():
            valido = False

    if not valido:
        mensagem_erro = "Digite apenas números inteiros."
        continue

    linha = int(entrada[0])
    coluna = int(entrada[1]) - 1
    valor = int(entrada[2])

    if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
        mensagem_erro = "Linha e coluna devem ser valores entre 1 e 9."
        continue

    if valor <= 0 or valor > 9:
        mensagem_erro = "O valor inserido deve ser um número entre 1 e 9 (ou 0 para apagar)."
        continue

    if fixos[linha][coluna]:
        mensagem_erro = "Essa posição pertence ao tabuleiro original e não pode ser alterada!"
        continue

    if valor == 0:
        tabuleiro[linha][coluna] = 0
        continue

    conflito = False

    for c in range(9):
        if tabuleiro[linha][c] == valor:
            conflito = True
            mensagem_erro = f"O número {valor} já existe nesta LINHA!"
            break

    if not conflito:
        for l in range(9):
            if l != linha and tabuleiro[l][coluna] == valor:
                conflito = True
                mensagem_erro = f"O número {valor} já existe nesta COLUNA!"
                break

    if not conflito:
        inicio_linha = (linha // 3) * 3
        inicio_coluna = (coluna // 3) * 3
        for l in range(inicio_linha, inicio_linha + 3):
            for c in range(inicio_coluna, inicio_coluna + 3):
                if (l != linha and c != coluna) and tabuleiro[l][c] == valor:
                    conflito = True
                    mensagem_erro = f"O número {valor} já existe neste BLOCO 3x3!"
                    break

    if not conflito:
        tabuleiro[linha][coluna] = valor