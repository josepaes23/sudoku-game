
print("===================================")
print("       CONTROLE DE ESTOQUE")
print("===================================")

produto1 = "Teclado"
preco1 = 120.00
quantidade1 = 10

produto2 = "Mouse"
preco2 = 65.00
quantidade2 = 15

produto3 = "Monitor"
preco3 = 850.00
quantidade3 = 5

print("\n--- PRODUTO 1 ---")
print("Nome:", produto1)
print("Preço: R$", preco1)
print("Quantidade:", quantidade1)
print("Valor em estoque: R$", preco1 * quantidade1)

print("\n--- PRODUTO 2 ---")
print("Nome:", produto2)
print("Preço: R$", preco2)
print("Quantidade:", quantidade2)
print("Valor em estoque: R$", preco2 * quantidade2)

print("\n--- PRODUTO 3 ---")
print("Nome:", produto3)
print("Preço: R$", preco3)
print("Quantidade:", quantidade3)
print("Valor em estoque: R$", preco3 * quantidade3)

total_estoque = (
    preco1 * quantidade1
    + preco2 * quantidade2
    + preco3 * quantidade3
)

print("\n--- RESUMO DO ESTOQUE ---")
print("Valor total do estoque: R$", total_estoque)

if quantidade1 < 5:
    print("ALERTA: estoque baixo de", produto1)

if quantidade2 < 5:
    print("ALERTA: estoque baixo de", produto2)

if quantidade3 < 5:
    print("ALERTA: estoque baixo de", produto3)

print("\nSistema encerrado.")
