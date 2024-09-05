class ContaBancaria():
    def __init__(self):
        self.depositos = []
        self.saques = []
        self.saldo = 0
        self.saques_dias = 3

    def depositar(self, deposito):
        
        if deposito >= 0:
            self.depositos.append(deposito)
            self.saldo += deposito
            print(f"Você depositou R${deposito}, seu saldo atual é R${self.saldo}!")
        else:
            print("Você digitou um valor incorreto, por favor, retorne ao menu inicial e refaça a operação!")

    def sacar(self, saque):

        if self.saques_dias < 1:
            print("Você chegou ao limite de saque do dia, por favor faça outra operação ou retorne outro dia!")
        elif saque > 500:
            print("Você ultrapassou o limite do valor de saque permitido, por favor, refaça a operação e tente outro valor.")
        elif saque > self.saldo or self.saldo < 0:
            print("Saldo insuficiente, por favor refaça a operação e tente outro valor.")
        else:
            self.saques.append(saque)
            self.saldo -= saque
            self.saques_dias -= 1
            print(f"Você sacou R${saque}, seu saldo atual é R${self.saldo}!")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
            return
        
        print("Extrato:")
        if self.depositos:
            print("Depósitos:")
            for deposito in self.depositos:
                print(f"R${deposito:.2f}")
        
        if self.saques:
            print("Saques:")
            for saque in self.saques:
                print(f"R${saque:.2f}")
        
        print("Saldo:")
        print(self.saldo)