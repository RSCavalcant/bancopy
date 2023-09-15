class Conta:
    def __init__(self):
        self.Saldo = 0
        self.Saque_Dia = 3
        self.extrato_d = []
        self.extrato_s = []

    def saldo_conta(self):
        print("R$ {:.2f}".format(self.Saldo))

    def deposito_conta(self, valor):
        if valor >= 1:
            self.extrato_d.append(valor)
            self.Saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito inválido. O depósito deve ser maior ou igual a R$ 1.")

    def saque_conta(self, valor):
        if valor <= self.Saldo:
            if self.Saque_Dia > 0:
                self.extrato_s.append(valor)
                self.Saldo -= valor
                self.Saque_Dia -= 1
                print("Saque realizado com sucesso!")
            else:
                print("Você ultrapassou a quantidade de saques diários. Tente novamente amanhã!")
        else:
            print("Seu saldo é insuficiente para este saque.")

    def gerar_extrato(self):
        print("Gerando extrato...")
        print(
            f"Segue seus depósitos {self.extrato_d}, segue seus saques {self.extrato_s} e seu saldo atual é R$ {self.Saldo:.2f}")

    def gerar_extrato(self):
        print("Gerando extrato...")
        print(
            f"Segue seus depósitos {self.extrato_d}, segue seus saques {self.extrato_s} e seu saldo atual é R$ {self.Saldo:.2f}")

def cadastro_conta():
    cliente = {"nome": "", "nasc": "", "CPF": "", "endereco": {}}
    cliente["nome"] = input("Qual é o seu nome? ")
    cliente["nasc"] = input("Qual é a sua data de nascimento? (dd/mm/aaaa) ")
    cliente["CPF"] = input("Qual é o seu CPF? ")
    if len(cliente["CPF"]) != 11:
        print("CPF inválido. Deve conter 11 dígitos.")
        return None
    endereco = input("Qual é o seu endereço? (rua, numero, cidade/estado) ")
    endereco_info = endereco.split(", ")
    if len(endereco_info) == 3:
        cliente["endereco"]["rua"] = endereco_info[0]
        cliente["endereco"]["numero"] = endereco_info[1]
        cliente["endereco"]["cidade_estado"] = endereco_info[2]
    else:
        print("Endereço inválido. Deve conter rua, número e cidade/estado.")
        return None


    while True:
        opcao = input("Cadastro realizado com sucesso!\nDigite 'menu' para voltar ao menu principal ou 'sair' para encerrar o programa: ")
        if opcao == 'menu':
            return cliente
        elif opcao == 'sair':
            exit()
        else:
            print("Opção inválida. Digite 'menu' ou 'sair'.")

def logar_conta(cliente):
    global loguin
    while True:
        cpf = input("Por favor, digite seu CPF para fazer login: ")
        if cpf == cliente["CPF"]:
            loguin = cpf
            print("Login realizado com sucesso!")
            break
        else:
            print("CPF não corresponde a nenhum cliente cadastrado. Tente novamente.")


def trocar_conta(cadastro):
    global loguin, cliente
    loguin = ""

    cpf = input("Por favor, digite seu CPF para fazer login: ")
    for c in cadastro:
        if c["CPF"] == cpf:
            cliente = c
            print("Login realizado com sucesso!")
            return


    print("CPF não corresponde a nenhum cliente cadastrado. Tente novamente.")


def main():
    cadastro = []
    cliente = {}

    print("0 - Cadastro")
    print("1 - Login")
    print("5 - Trocar de Conta")
    first = input("O que deseja realizar? ")

    if first == "0":
        cliente = cadastro_conta()
        if cliente is not None:
            cadastro.append(cliente)

    elif first == "1":
        if not cadastro:
            print("Você precisa cadastrar uma conta primeiro.")
        else:
            trocar_conta(cadastro)
            if "CPF" in cliente:  #
                conta = Conta()

                while True:
                    print("\nOperações da Conta:")
                    print("1 - Saldo")
                    print("2 - Depósito")
                    print("3 - Saque")
                    print("4 - Extrato")
                    print("5 - Trocar de Conta")
                    print("0 - Sair")

                    op = input("Qual operação deseja fazer? (1, 2, 3, 4, 5 ou 0): ")

                    if op == "1":
                        conta.saldo_conta()
                    elif op == "2":
                        valor = float(input("Quanto deseja depositar? "))
                        conta.deposito_conta(valor)
                    elif op == "3":
                        valor = float(input("Quanto deseja sacar? "))
                        conta.saque_conta(valor)
                    elif op == "4":
                        conta.gerar_extrato()
                    elif op == "5":
                        trocar_conta(cadastro)
                    elif op == "0":
                        break
                    else:
                        print("Opção inválida. Por favor, escolha uma opção válida.")

                print("Até logo. Obrigado!")


if __name__ == "__main__":
    main()









