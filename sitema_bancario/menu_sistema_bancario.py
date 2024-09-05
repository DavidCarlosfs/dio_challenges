from func_sistema_bancario import *
conta = ContaBancaria()
menu = 5

while menu != 0:
    menu = int(input(
                 """
                 ============MENU=============
                 [1] Digite 1 para depositar\n
                 [2] Digite 2 para sacar\n
                 [3] Digite 3 para ver o extrato\n
                 [0] Digite 0 para encerrar a operação
                 """
                 ))
    
    if menu == 1:
        deposito = int(input("Digite o valor a ser depositado: R$"))
        conta.depositar(deposito)
    
    elif menu == 2:
        saque = int(input("Digite o valor a ser sacado: R$"))
        conta.sacar(saque)
    
    elif menu == 3:
        conta.extrato()
    
    elif menu == 0:
        print("Agradecemos a preferência!")
        break

    else:
        print("Valor inválido, por favor, retorne ao menu e digite um valor válido.")