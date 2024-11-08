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
            print("Valor De Deposito Invalido")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
       
        if valor <= 0 :
            print("Valor De Saque Invalido")
        elif valor > 500 :
            print ("Operação invalida Limite maxido para saque é de R$500.00")

        elif numero_saques == LIMITE_SAQUES:
            print("Limite Diario de Saque Atingido")

        elif numero_saques <= 3 :
          saldo = saldo - valor 
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques += 1
          print(saldo)              
          print(f"Numero de Saques {numero_saques}")

        else:
            print("Valor de saque maior que o saldo")

    elif opcao == "e":
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo Atual de R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")