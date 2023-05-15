print(""" 
Bem vindo a lanchonete do Gabriel Schinoff
*******************Cardapio******************
| Código |         Descrição        | Valor |
|  100   |      Cachorro Quente     |  9,00 |
|  101   |   Cachorro Quente Duplo  | 11,00 |
|  102   |           X-Egg          | 12,00 |
|  103   |          X-Salada        | 12,00 |
|  104   |           X-Bacon        | 14,00 |
|  105   |           X-Tudo         | 17,00 |
|  200   |     Refrigerante Lata    |  5,00 |
|  201   |         Chá Gelado       |  4,00 |
*********************************************
""")

tabela_produtos = {
    100: ["Cachorro Quente", 9.00],
    101: ["Cachorro Quente Duplo", 11.00],
    102: ["X-Egg", 12.00],
    103: ["X-Salada", 13.00],
    104: ["X-Bacon", 14.00],
    105: ["X-Tudo", 17.00],
    200: ["Refrigerante Lata", 5.00],
    201: ["Chá Gelado", 4.00]
}

valor_total = 0

while True:
    codigo = int(input("Entre com o código do pruduto desejado: "))

    if codigo not in tabela_produtos:
        print("Opção inválida.")
        continue

    produto = tabela_produtos[codigo]
    descricao = produto[0]
    valor = produto[1]
    valor_total += valor

    print(f"\nVocê pediu um {descricao} no valor de R${valor:.2f}!!\n")

    while True:
        s_n = int(input("Deseja pedir mais alguma coisa?\n1- Sim\n2- Não\n"))

        if s_n == 1:
            break
        elif s_n == 2:
            break
        else:
            print("Opção inválida. Digite novamente.")

    if s_n == 2:
        break

print(f"Valor total a pagar: R${valor_total:.2f}")
