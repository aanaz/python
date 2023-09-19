menu = """
[d] Depositar
[s] Saque
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao not in ["d", "s", "e", "q"]:
        print("Operação invalida, tente novamente:")
        continue

    if opcao == "d":
        # Depositar
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato += f"\nDepósito de {valor} - Saldo atual: {saldo}"

    elif opcao == "s":
        # Saque
        valor = float(input("Digite o valor do saque: "))

        # Verifica se o usuário excedeu o limite de saques
        if numero_saques >= LIMITES_SAQUES:
            print("Você excedeu o limite de saques.")
            continue

        # Verifica se o valor do saque é maior do que o saldo
        if valor > saldo:
            print("Saldo insuficiente.")
            continue

        # Realiza o saque
        saldo -= valor
        extrato += f"\nSaque de {valor} - Saldo atual: {saldo}"
        numero_saques += 1

    elif opcao == "e":
        # Extrato
        print(extrato)

    elif opcao == "q":
        break