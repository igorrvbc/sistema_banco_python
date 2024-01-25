from datetime import date   

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
hora = date.today().strftime('%d/%m/%Y')

while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado:\n")) 
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} realizado em {hora}\n"
            print(f'Depósito realizado com sucesso!')
        else: 
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("você excedeu seu limite de saque diário")
        else:
            valor = float(input("Digite o valor do saque: \n"))
            if valor > 0:
                if valor > saldo:
                    print('Saldo insuficiente. Tente novamente.')
                else:               
                    numero_saques +=1
                    saldo -= valor
                    print("Saque realizado com sucesso")
                    extrato += f"Saque no valor de R$ {valor:.2f} realizado em {hora}\n"
            else: 
                print("Operação falhou! o valor informado é inválido.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========\n")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==============================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")