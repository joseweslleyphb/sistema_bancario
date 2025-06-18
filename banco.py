def main():
    saldo = 0.0
    historico = []
    contador_saques = 0
    total_saques = 0.0
    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE_DIARIO = 500.0

    def depositar(valor):
        nonlocal saldo
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
            return
        saldo += valor
        historico.append(f"Depósito: +R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(valor):
        nonlocal saldo, contador_saques, total_saques
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return
        if contador_saques >= LIMITE_SAQUES_DIARIOS:
            print("Limite diário de 3 saques atingido.")
            return
        if total_saques + valor > LIMITE_VALOR_SAQUE_DIARIO:
            print(f"Valor excede o limite diário de saque de R$ {LIMITE_VALOR_SAQUE_DIARIO:.2f}.")
            return
        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        saldo -= valor
        contador_saques += 1
        total_saques += valor
        historico.append(f"Saque: -R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostra_extrato():
        print("\n======= Extrato Bancário =======")
        if not historico:
            print("Nenhuma movimentação realizada.")
        else:
            for item in historico:
                print(item)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===============================\n")

    while True:
        print("=== Sistema Bancário Simples ===")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 4.")
            continue

        if opcao == 1:
            try:
                valor = float(input("Digite o valor para depósito: "))
                depositar(valor)
            except ValueError:
                print("Valor inválido. Digite um número válido.")
        elif opcao == 2:
            try:
                valor = float(input("Digite o valor para saque: "))
                sacar(valor)
            except ValueError:
                print("Valor inválido. Digite um número válido.")
        elif opcao == 3:
            mostra_extrato()
        elif opcao == 4:
            print("Saindo do sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 4.")

if __name__ == "__main__":
    main()




