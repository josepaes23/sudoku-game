
print("================================")
print("     SISTEMA DE ALUNOS")
print("================================")

nome1 = "Ana"
idade1 = 20
curso1 = "Ciência da Computação"

nome2 = "Carlos"
idade2 = 22
curso2 = "Engenharia da Computação"

print("\n--- Aluno 1 ---")
print("Nome:", nome1)
print("Idade:", idade1)
print("Curso:", curso1)

print("\n--- Aluno 2 ---")
print("Nome:", nome2)
print("Idade:", idade2)
print("Curso:", curso2)

print("\n--- Relatório ---")

if idade1 >= 18:
    print(nome1, "é maior de idade.")
else:
    print(nome1, "é menor de idade.")

if idade2 >= 18:
    print(nome2, "é maior de idade.")
else:
    print(nome2, "é menor de idade.")

print("\nSistema encerrado.")
