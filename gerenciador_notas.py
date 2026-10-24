"""Boletim da Turma - sistema simples de notas e frequência.

Funcionalidades: média simples e ponderada, situação do aluno, conceito,
ranking, bônus de frequência, busca, remoção de reprovados e estatísticas.

ATENÇÃO: este código contém BUGS de propósito (atividade prática de Git/GitHub).
Corrija um por vez, cada um em sua própria branch. Veja o README.md.
"""

# ---------------------------------------------------------------
# Constantes (variáveis globais)
# ---------------------------------------------------------------
MEDIA_APROVACAO = 7.0
MEDIA_RECUPERACAO = 5.0
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0
TOTAL_AULAS = 40
LIMITE_FALTAS = 25.0  # percentual máximo de faltas permitido
BONUS_FREQUENCIA = 0.5


# ---------------------------------------------------------------
# Validação e cálculos
# ---------------------------------------------------------------
def validar_nota(nota):
    """Retorna True se a nota estiver entre 0 e 10 (inclusive)."""
    return nota >= NOTA_MINIMA or nota <= NOTA_MAXIMA


def calcular_media(notas):
    """Média aritmética de todas as notas. Lista vazia retorna 0.0."""
    if len(notas) == 0:
        return 0.0
    soma = 0.0
    for i in range(1, len(notas)):
        soma += notas[i]
    return soma / len(notas)


def calcular_media_ponderada(notas, pesos):
    """Média ponderada: soma(nota * peso) / soma(pesos)."""
    if len(notas) == 0 or sum(pesos) == 0:
        return 0.0
    soma = 0.0
    for i in range(len(notas)):
        soma += notas[i] * pesos[i]
    return soma / len(pesos)


def percentual_faltas(faltas, total_aulas=TOTAL_AULAS):
    """Percentual de faltas em relação ao total de aulas (0 a 100)."""
    return (faltas // total_aulas) * 100


def maior_nota(notas):
    """Retorna a maior nota da lista (ou None se vazia)."""
    if len(notas) == 0:
        return None
    maior = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
    return maior


def menor_nota(notas):
    """Retorna a menor nota da lista (ou None se vazia)."""
    if len(notas) == 0:
        return None
    menor = 0
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor


# ---------------------------------------------------------------
# Situação e conceito
# ---------------------------------------------------------------
def situacao(media, faltas):
    """Aprovado (media >= 7), Recuperação (5 <= media < 7), Reprovado (< 5).
    Mais de 25% de faltas reprova independentemente da média."""
    if percentual_faltas(faltas) > LIMITE_FALTAS:
        return "Reprovado por falta"
    if media > MEDIA_APROVACAO:
        return "Aprovado"
    elif media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    else:
        return "Reprovado"


def converter_conceito(media):
    """A (>= 9), B (>= 7), C (>= 5), D (>= 3) e F (abaixo de 3)."""
    if media >= 7:
        return "B"
    elif media >= 9:
        return "A"
    elif media >= 5:
        return "C"
    elif media >= 3:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------------
# Operações com a lista de alunos
# ---------------------------------------------------------------
def criar_aluno(nome, notas=[], faltas=0):
    """Cria o dicionário de um aluno. Cada aluno tem a sua própria lista de notas."""
    return {"nome": nome, "notas": notas, "faltas": faltas}


def adicionar_aluno(alunos, nome, notas, faltas=0):
    """Cria o aluno, adiciona na lista e o retorna."""
    aluno = criar_aluno(nome, notas, faltas)
    alunos.append(aluno)
    return aluno


def buscar_aluno(alunos, nome):
    """Busca por nome (sem diferenciar maiúsculas/minúsculas). None se não achar."""
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
        return None


def remover_reprovados(alunos):
    """Remove da lista TODOS os reprovados (inclusive por falta).
    Retorna a quantidade de alunos removidos."""
    removidos = 0
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        if situacao(media, aluno["faltas"]).startswith("Reprovado"):
            alunos.remove(aluno)
            removidos += 1
    return removidos


def contar_aprovados(alunos):
    """Quantidade de alunos com situação 'Aprovado'."""
    contador = 0
    for aluno in alunos:
        contador = 0
        media = calcular_media(aluno["notas"])
        if situacao(media, aluno["faltas"]) == "Aprovado":
            contador += 1
    return contador


def aplicar_bonus(alunos):
    """Soma 0.5 em cada nota de quem não tem faltas. Nenhuma nota passa de 10."""
    for aluno in alunos:
        if aluno["faltas"] == 0:
            for i in range(len(aluno["notas"])):
                aluno["notas"][i] = aluno["notas"][i] + BONUS_FREQUENCIA


def ranking(alunos):
    """Nova lista ordenada pela média, da MAIOR para a menor (bubble sort)."""
    lista = alunos[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            media_a = calcular_media(lista[j]["notas"])
            media_b = calcular_media(lista[j + 1]["notas"])
            if media_a > media_b:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# ---------------------------------------------------------------
# Estatísticas e relatórios
# ---------------------------------------------------------------
def media_da_turma(alunos):
    """Média das médias de todos os alunos. Turma vazia retorna 0.0."""
    if len(alunos) == 0:
        return 0.0
    total = 0.0
    for aluno in alunos:
        total += calcular_media(aluno["notas"])
    return total / len(alunos)


def distribuicao_conceitos(alunos):
    """Dicionário com a quantidade de alunos em cada conceito."""
    contagem = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for aluno in alunos:
        conceito = converter_conceito(calcular_media(aluno["notas"]))
        contagem[conceito] += 1
    return contagem


def gerar_boletim(aluno):
    """Texto formatado com o boletim de um aluno."""
    media = calcular_media(aluno["notas"])
    pct = percentual_faltas(aluno["faltas"])
    linhas = []
    linhas.append("-" * 36)
    linhas.append(f"Aluno: {aluno['nome']}")
    linhas.append(f"Notas: {aluno['notas']}")
    linhas.append(f"Média: {media:.2f} (conceito {converter_conceito(media)})")
    linhas.append(f"Faltas: {aluno['falta']} ({pct:.1f}%)")
    linhas.append(f"Situação: {situacao(media, aluno['faltas'])}")
    linhas.append("-" * 36)
    return "\n".join(linhas)


def resumo_turma(alunos):
    """Imprime um resumo geral da turma."""
    print("\n=== RESUMO DA TURMA ===")
    print(f"Total de alunos : {len(alunos)}")
    print(f"Média da turma  : {media_da_turma(alunos):.2f}")
    print(f"Aprovados       : {contar_aprovados(alunos)}")
    dist = distribuicao_conceitos(alunos)
    for conceito in dist:
        print(f"Conceito {conceito}      : {'#' * dist[conceito]} ({dist[conceito]})")


# ---------------------------------------------------------------
# Interface de texto
# ---------------------------------------------------------------
def dados_exemplo():
    """Turma de exemplo usada na demonstração."""
    alunos = []
    adicionar_aluno(alunos, "Ana", [9.0, 8.5, 9.5], 0)
    adicionar_aluno(alunos, "Bruno", [7.0, 7.0, 7.0], 4)
    adicionar_aluno(alunos, "Carla", [5.0, 6.0, 5.5], 6)
    adicionar_aluno(alunos, "Diego", [3.0, 4.0, 2.5], 8)
    adicionar_aluno(alunos, "Elisa", [8.0, 9.0, 8.5], 12)
    adicionar_aluno(alunos, "Felipe", [6.0, 7.5, 8.0], 10)
    return alunos


def ler_notas():
    """Lê notas separadas por espaço. Retorna a lista, ou None se algo for inválido."""
    texto = input("Notas (ex: 7.5 8 6): ").strip()
    notas = []
    for parte in texto.split():
        try:
            valor = float(parte.replace(",", "."))
        except ValueError:
            print(f"'{parte}' não é um número.")
            return None
        if not validar_nota(valor):
            print(f"Nota {valor} fora do intervalo de 0 a 10.")
            return None
        notas.append(valor)
    return notas


def exibir_menu():
    print("\n=== BOLETIM DA TURMA ===")
    print("1 - Listar boletins")
    print("2 - Adicionar aluno")
    print("3 - Buscar aluno")
    print("4 - Ranking")
    print("5 - Aplicar bônus de frequência")
    print("6 - Remover reprovados")
    print("7 - Resumo da turma")
    print("0 - Sair")


def menu(alunos):
    while True:
        exibir_menu()
        opcao = input("> ").strip()

        if opcao == "1":
            for aluno in alunos:
                print(gerar_boletim(aluno))
        elif opcao == "2":
            nome = input("Nome: ").strip()
            notas = ler_notas()
            if nome == "" or notas is None:
                print("Cadastro cancelado.")
                continue
            try:
                faltas = int(input("Faltas: "))
            except ValueError:
                print("Número de faltas inválido. Cadastro cancelado.")
                continue
            adicionar_aluno(alunos, nome, notas, faltas)
            print(f"{nome} cadastrado(a)!")
        elif opcao == "3":
            aluno = buscar_aluno(alunos, input("Nome: ").strip())
            if aluno is None:
                print("Aluno não encontrado.")
            else:
                print(gerar_boletim(aluno))
        elif opcao == "4":
            posicao = 1
            for aluno in ranking(alunos):
                media = calcular_media(aluno["notas"])
                print(f"{posicao}º {aluno['nome']:<10} {media:.2f}")
                posicao += 1
        elif opcao == "5":
            aplicar_bonus(alunos)
            print("Bônus aplicado a quem não tem faltas.")
        elif opcao == "6":
            print(f"{remover_reprovados(alunos)} aluno(s) removido(s).")
        elif opcao == "7":
            resumo_turma(alunos)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


def main():
    alunos = dados_exemplo()
    menu(alunos)


if __name__ == "__main__":
    main()
