Saldo = 0
Saque_Dia = 3
extrato_d = []
extrato_s = []

print("""Qual operação deseja realizar?
1 - Saldo;
2 - Deposito;
3 - Saque;
4 - Extrato:
0 - Sair""")

op = int(input("Qual operação deseja fazer? (1, 2, 3, 4 ou 0)"))

while op != 0:
    if op == 1:
        print("R$ {:.2f}".format(Saldo))
    elif op == 2:
        deposito = float(input("Quanto deseja depositar? "))
        if deposito >= 1:
            extrato_d.append(deposito)
            Saldo += deposito
        else:
            print("Valor de depósito inválido. O depósito deve ser maior ou igual a R$ 1.")
    elif op == 3:
        saque = float(input("Quanto deseja sacar? "))
        if saque <= Saldo:
            if Saque_Dia != 0:
                extrato_s.append(saque)
                Saldo -= saque
                Saque_Dia -= 1
                print("Saque realizado com sucesso!")
            else:
                print("Você ultrapassou a quantidade de saques diários. Tente novamente amanhã!")
        else:
            print("Seu saldo é insuficiente para este saque!")
    elif op == 4:
        print("Gerando extrato...")
        print(f"Segue seus depósitos {extrato_d}, segue seus saques {extrato_s} e seu saldo atual é R$ {Saldo:.2f}")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    print("Deseja realizar uma nova ação?")
    op = int(input("Qual operação deseja realizar? (1, 2, 3, 4 ou 0)"))

print("Até logo. Obrigado!")









