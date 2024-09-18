from func_sistema_bancario import *
conta = ContaBancaria()

menu = 9

while menu != 0:
    menu = int(input(
                 """
                 ============MENU=============
                 [1] Digite 1 para adcionar um novo usuário\n
                 [2] Digite 2 para criar uma conta\n
                 [3] Digite 3 para acessar a lista de contas do usuário\n
                 [4] Digite 4 para deletar uma conta\n
                 [5] Digite 5 para depositar\n
                 [6] Digite 6 para sacar\n
                 [7] Digite 7 para ver o extrato\n
                 [0] Digite 0 para encerrar a operação
                 """
                 ))
    
    if menu == 1:
        nome_usuário = input("Digite o nome do usuário: ")
        data_nascimento_usuario = input("Digite a data de nascimento do usuário (dd-mm-aaaa): ")
        cpf_usuario = input("Digite o CPF do usuario (somente números): ")
        endereco_usuario = input("Digite o endereço do usuário (logradouro, nº, bairo - cidade/sigla estado): ")
        conta.criar_usuario(nome_usuário, data_nascimento_usuario,cpf_usuario,endereco_usuario)

    elif menu == 2:
        cpf = input("Digite o número do CPF de usuário já cadastrado: ")
        conta.criar_conta(cpf)

    elif menu == 3:
        usuario = input("Digite o CPF do usuário que deseja encontrar alguma conta: ")
        conta.encontrar_contas_por_cpf(cpf=usuario)

    elif menu == 4:
        cpf_deletar = input("Digite o CPF da conta que deseja deletar: ")
        numero_conta = input("Digite o número da conta que deseja deletar: ")
        conta.deletar_conta(cpf=cpf_deletar, numero_conta=numero_conta)

    elif menu == 5:
        deposito = float(input("Digite o valor a ser depositado: R$"))
        conta.depositar(deposito)

    elif menu == 6:
        saque = float(input("Digite o valor a ser sacado: R$"))
        conta.sacar(saque=saque)
    
    elif menu == 7:
        conta.extrato()
    
    elif menu == 0:
        print("Agradecemos a preferência!")
        break

    else:
        print("Valor inválido, por favor, retorne ao menu e digite um valor válido.")