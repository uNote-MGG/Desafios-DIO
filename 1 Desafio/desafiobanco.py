menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0 :
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação invalida, Valor De Deposito Invalido")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
       
        if valor <= 0 :
            print("Operação invalida, Valor De Saque Invalido")
        elif valor > 500 :
            print ("Operação invalida, Limite maxido para saque é de R$500.00")

        elif numero_saques == LIMITE_SAQUES:
            print("Operação invalida, Limite Diario de Saque Atingido")

        elif numero_saques <= 3 :
          saldo = saldo - valor 
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques += 1

        else:
            print("Valor de saque maior que o saldo")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas de movimentações." if not extrato else extrato)
        print(f"Saldo Atual de R${saldo:.2f}")
        print("==========================================")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")