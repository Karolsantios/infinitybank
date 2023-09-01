from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.deposito import depositar
from operacoes.transferencia import transferir
from banco import *

def menu():
    while True:
        print("---- Bem vindo ao menu ----")
        print("1 - Adicionar conta")
        print("2 - Edita nome")
        print("3 - Consultar conta")
        print("4 - Excluir conta")
        print("5 - Listar todos")
        print("6 - Realizar Saque")
        print("7 - Realizar depósito")
        print("8 - Realizar transferência")
        print("9 - Consultar saldo")
        print("10 - Sair")
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            nome = input("Digite o nome do cliente: ")
            saldo = float(input("Digite o saldo: "))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o número da conta: '))
            nome = input('Digite o novo nome do cliente: ')
            editarNome(conta, nome)
        elif opcao == 3:
            conta = int(input('Digite o número da conta: '))
            buscarCliente(conta)
        elif opcao == 4:
            conta = int(input('Digite o número da conta: '))
            removerConta(conta)
        elif opcao == 5:
            listarTodos()
        elif opcao == 6:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do saque: '))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de depósito: '))
            depositar(conta, valor)
        elif opcao == 8:
            contaOrigem = int('Informe a conta de origem: ')
            contaDestino = int('Infomre a conta de destino: ')
            valor = float(input('Digite o valor para transferir : '))
            transferir(contaOrigem, contaDestino, valor)
        elif opcao == 9:
            conta = int(input('Digite o número da conta: '))
            consultarSaldo(conta)
        elif opcao == 10:
            print("---Você saiu do programa!")
            break
        else:
            print("Opção inválida!")
menu()