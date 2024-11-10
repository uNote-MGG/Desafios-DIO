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

def deposito (valor):
    global saldo
    global extrato
    if valor > 0 :
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nO Valor Depósitado foi de R$ {valor:.2f}\n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def excedeu_saldo(valor):
    global saldo
    excedeu_valor_saldo = valor > saldo
    return excedeu_valor_saldo

def limite_de_saque (valor):
    saque_limite = valor > 500
    return saque_limite

def excedeu_num_saque(numero_saques):
    saque_excedido = numero_saques >= LIMITE_SAQUES
    return saque_excedido

def sacar (valor):
    global saldo
    global extrato
    global numero_saques
    saldo -= valor
    numero_saques += 1
    extrato += f"Saque: R$ {valor:.2f}\n" 
    return saldo,extrato,numero_saques



while True:

    opcao = input(menu)
#A Função deposito deve receber os argumentos apenas por posição(position only). Sugestão de argumentos: saldo.valor. extrato; sugestão de retorno: saldo e extrato.

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))   
        deposito(valor)
        

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if excedeu_saldo(valor):
            print ("Operação falhou! O valor informado é maior que o saldo.")
        elif limite_de_saque(valor):
            print ("Operação falhou! O valor e maior que limite de R$ 500,00 ")
        elif excedeu_num_saque(numero_saques):
            print("Operação falhou! O limite de saques diarios atingida.")
        else:
            sacar(valor)
            print("Saque realizado com sucesso! ")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
