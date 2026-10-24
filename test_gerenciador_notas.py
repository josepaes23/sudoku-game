"""Testes automáticos do gerenciador de notas.

Como executar (na pasta do projeto):
    python -m unittest -v test_gerenciador_notas

Objetivo da atividade: fazer TODOS os testes passarem, corrigindo um bug por vez
(um bug = uma branch = um commit/PR). Não altere este arquivo.
"""
import importlib
import os
import unittest

# O professor pode apontar para outra versão do módulo (ex.: a versão correta).
g = importlib.import_module(os.environ.get("MODULO_ALVO", "gerenciador_notas"))


def turma_exemplo():
    return g.dados_exemplo()


class TestValidacaoECalculos(unittest.TestCase):
    def test_validar_nota_aceita_limites(self):
        self.assertTrue(g.validar_nota(0))
        self.assertTrue(g.validar_nota(10))
        self.assertTrue(g.validar_nota(7.5))

    def test_validar_nota_rejeita_fora_do_intervalo(self):
        self.assertFalse(g.validar_nota(-1))
        self.assertFalse(g.validar_nota(10.5))
        self.assertFalse(g.validar_nota(100))

    def test_media_considera_todas_as_notas(self):
        self.assertAlmostEqual(g.calcular_media([6, 8, 10]), 8.0)

    def test_media_lista_vazia(self):
        self.assertEqual(g.calcular_media([]), 0.0)

    def test_media_ponderada(self):
        self.assertAlmostEqual(g.calcular_media_ponderada([10, 5], [3, 1]), 8.75)

    def test_percentual_de_faltas(self):
        self.assertAlmostEqual(g.percentual_faltas(10), 25.0)
        self.assertAlmostEqual(g.percentual_faltas(4), 10.0)
        self.assertAlmostEqual(g.percentual_faltas(0), 0.0)

    def test_maior_nota(self):
        self.assertEqual(g.maior_nota([7, 5, 9, 6]), 9)

    def test_menor_nota(self):
        self.assertEqual(g.menor_nota([7, 5, 9, 6]), 5)

    def test_maior_e_menor_lista_vazia(self):
        self.assertIsNone(g.maior_nota([]))
        self.assertIsNone(g.menor_nota([]))


class TestSituacaoEConceito(unittest.TestCase):
    def test_media_exatamente_sete_aprova(self):
        self.assertEqual(g.situacao(7.0, 0), "Aprovado")

    def test_aprovado_e_recuperacao_e_reprovado(self):
        self.assertEqual(g.situacao(8.5, 2), "Aprovado")
        self.assertEqual(g.situacao(5.0, 2), "Recuperação")
        self.assertEqual(g.situacao(6.9, 2), "Recuperação")
        self.assertEqual(g.situacao(4.9, 2), "Reprovado")

    def test_reprova_por_falta(self):
        self.assertEqual(g.situacao(9.0, 11), "Reprovado por falta")

    def test_limite_de_faltas_ainda_permitido(self):
        self.assertEqual(g.situacao(9.0, 10), "Aprovado")  # exatamente 25%

    def test_conceito_a(self):
        self.assertEqual(g.converter_conceito(9.5), "A")
        self.assertEqual(g.converter_conceito(9.0), "A")

    def test_demais_conceitos(self):
        self.assertEqual(g.converter_conceito(8.0), "B")
        self.assertEqual(g.converter_conceito(5.5), "C")
        self.assertEqual(g.converter_conceito(3.0), "D")
        self.assertEqual(g.converter_conceito(1.0), "F")


class TestListaDeAlunos(unittest.TestCase):
    def test_alunos_nao_compartilham_lista_de_notas(self):
        a = g.criar_aluno("A")
        b = g.criar_aluno("B")
        a["notas"].append(10)
        self.assertEqual(b["notas"], [])

    def test_adicionar_aluno(self):
        alunos = []
        g.adicionar_aluno(alunos, "Zeca", [7, 8], 1)
        self.assertEqual(len(alunos), 1)
        self.assertEqual(alunos[0]["nome"], "Zeca")

    def test_buscar_aluno_ignora_maiusculas(self):
        self.assertEqual(g.buscar_aluno(turma_exemplo(), "ANA")["nome"], "Ana")

    def test_buscar_aluno_que_nao_e_o_primeiro(self):
        self.assertEqual(g.buscar_aluno(turma_exemplo(), "Felipe")["nome"], "Felipe")

    def test_buscar_aluno_inexistente(self):
        self.assertIsNone(g.buscar_aluno(turma_exemplo(), "Fulano"))

    def test_contar_aprovados(self):
        # Ana, Bruno (média 7.0) e Felipe
        self.assertEqual(g.contar_aprovados(turma_exemplo()), 3)

    def test_remover_reprovados_consecutivos(self):
        alunos = []
        g.adicionar_aluno(alunos, "R1", [2, 3], 0)
        g.adicionar_aluno(alunos, "R2", [1, 2], 0)
        g.adicionar_aluno(alunos, "OK", [9, 9], 0)
        removidos = g.remover_reprovados(alunos)
        self.assertEqual(removidos, 2)
        self.assertEqual([a["nome"] for a in alunos], ["OK"])

    def test_remover_reprovados_na_turma_exemplo(self):
        alunos = turma_exemplo()
        self.assertEqual(g.remover_reprovados(alunos), 2)  # Diego e Elisa
        nomes = [a["nome"] for a in alunos]
        self.assertNotIn("Diego", nomes)
        self.assertNotIn("Elisa", nomes)

    def test_bonus_limitado_a_dez(self):
        alunos = []
        g.adicionar_aluno(alunos, "Top", [10, 9.8, 9.0], 0)
        g.aplicar_bonus(alunos)
        self.assertEqual(alunos[0]["notas"], [10, 10, 9.5])

    def test_bonus_so_para_quem_nao_falta(self):
        alunos = []
        g.adicionar_aluno(alunos, "Faltoso", [5.0], 3)
        g.aplicar_bonus(alunos)
        self.assertEqual(alunos[0]["notas"], [5.0])

    def test_ranking_da_maior_para_a_menor_media(self):
        nomes = [a["nome"] for a in g.ranking(turma_exemplo())]
        self.assertEqual(nomes, ["Ana", "Elisa", "Felipe", "Bruno", "Carla", "Diego"])

    def test_ranking_nao_altera_a_lista_original(self):
        alunos = turma_exemplo()
        g.ranking(alunos)
        self.assertEqual(alunos[0]["nome"], "Ana")
        self.assertEqual(alunos[1]["nome"], "Bruno")


class TestEstatisticas(unittest.TestCase):
    def test_media_da_turma(self):
        self.assertAlmostEqual(g.media_da_turma(turma_exemplo()), 6.7222222, places=4)

    def test_media_da_turma_vazia(self):
        self.assertEqual(g.media_da_turma([]), 0.0)

    def test_distribuicao_de_conceitos(self):
        # Ana 9.0 (A), Elisa 8.5 (B), Bruno 7.0 (B), Felipe 7.17 (B), Carla 5.5 (C), Diego 3.17 (D)
        esperado = {"A": 1, "B": 3, "C": 1, "D": 1, "F": 0}
        self.assertEqual(g.distribuicao_conceitos(turma_exemplo()), esperado)

    def test_boletim_contem_os_dados_do_aluno(self):
        aluno = g.buscar_aluno(turma_exemplo(), "Bruno")
        texto = g.gerar_boletim(aluno)
        self.assertIn("Bruno", texto)
        self.assertIn("Faltas: 4", texto)
        self.assertIn("Aprovado", texto)


if __name__ == "__main__":
    unittest.main()
