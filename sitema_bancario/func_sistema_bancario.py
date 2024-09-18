from datetime import datetime
import pytz

class Usuario:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria():
    def __init__(self):
        self.depositos = []
        self.saques = []
        self.saldo = 0
        self.saques_dias = 3
        self.transacoes = 10
        self.usuarios = []
        self.usuario_cpf = {}  # Alterado para um dicionário
        self.contas = []
        self.numero_conta = 0

        self.AGENCIA = "0001"

    def criar_usuario(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        if cpf in self.usuario_cpf:
            print("CPF já cadastrado, por favor, retorne ao menu e informe um CPF diferente")
            return
        
        novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        self.usuario_cpf[cpf] = []  # Inicialmente, o CPF não tem contas
        print(f"Usuário {nome} foi cadastrado com sucesso!")
    
    def criar_conta(self, cpf):
        if cpf in self.usuario_cpf:
            self.numero_conta += 1
            conta = {"agencia": self.AGENCIA, "numero_conta": self.numero_conta, "usuario_cpf": cpf}
            self.contas.append(conta)
            self.usuario_cpf[cpf].append(self.numero_conta)  # Adiciona o número da conta à lista de contas do CPF
            print(f"Conta criada com sucesso!")
        else:
            print("Usuário não encontrado, por favor, retorne ao menu e informe um CPF já cadastrado.")
            return

    def depositar(self, deposito: float):
        if self.transacoes < 1:
            print("Você chegou ao limite de transações diárias, por favor retorne outro dia!")
        elif deposito <= 0:
            print("Você digitou um valor incorreto, por favor, retorne ao menu inicial e refaça a operação!")    
        elif deposito > 0:
            self.transacoes -= 1
            self.depositos.append((deposito, datetime.now(pytz.timezone("America/Sao_Paulo"))))
            self.saldo += deposito
            print(f"Você depositou R${deposito}, seu saldo atual é R${self.saldo}!")

    def sacar(self, *, saque: float):
        if self.transacoes < 1:
            print("Você chegou ao limite de transações diárias, por favor retorne outro dia!")
        elif self.saques_dias < 1:
            print("Você chegou ao limite de saque do dia, por favor faça outra operação ou retorne outro dia!")
        elif saque > 500:
            print("Você ultrapassou o limite do valor de saque permitido, por favor, refaça a operação e tente outro valor.")
        elif saque > self.saldo or self.saldo <= 0:
            print("Saldo insuficiente, por favor refaça a operação e tente outro valor.")
        else:
            self.transacoes -= 1
            self.saques_dias -= 1
            self.saques.append((saque, datetime.now(pytz.timezone("America/Sao_Paulo"))))
            self.saldo -= saque
            print(f"Você sacou R${saque}, seu saldo atual é R${self.saldo}!")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
            return
        
        print("Extrato:")
        if self.depositos:
            print("Depósitos:")
            for deposito, data_hora in self.depositos:
                print(f"{data_hora.strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R${deposito:.2f}")
        
        if self.saques:
            print("Saques:")
            for saque, data_hora in self.saques:
                print(f"{data_hora.strftime('%d/%m/%Y %H:%M:%S')} - Saque: R${saque:.2f}")
        
        print("Saldo:")
        print(f"R${self.saldo:.2f}")

    def encontrar_contas_por_cpf(self, cpf: str):
        if cpf not in self.usuario_cpf:
            print("CPF não encontrado!")
        elif not self.usuario_cpf[cpf]:
            print("Não há contas vinculadas ao CPF informado!")
        else:
            contas_vinculadas = [conta for conta in self.contas if conta["usuario_cpf"] == cpf]
            if contas_vinculadas:
                print(f"Contas vinculadas ao CPF {cpf}:")
                for conta in contas_vinculadas:
                    print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}")
            else:
                print("Não há contas vinculadas ao CPF informado!")

    def deletar_conta(self, cpf: str, numero_conta: int):
        if cpf not in self.usuario_cpf:
            print("CPF não encontrado!")
            return
        
        # Verifica se o CPF tem contas associadas
        if numero_conta not in self.usuario_cpf[cpf]:
            print("Conta não encontrada para o CPF informado.")
            return
        
        # Remove a conta da lista de contas
        conta_a_deletar = next((conta for conta in self.contas if conta["numero_conta"] == numero_conta and conta["usuario_cpf"] == cpf), None)
        
        if conta_a_deletar:
            self.contas.remove(conta_a_deletar)
            self.usuario_cpf[cpf].remove(numero_conta)  # Remove o número da conta da lista de contas do CPF
            print(f"Conta número {numero_conta} vinculada ao CPF {cpf} foi deletada com sucesso!")
        else:
            print("Conta não encontrada para o CPF informado.")
