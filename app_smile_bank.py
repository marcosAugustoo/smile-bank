menu = """
============|| Menu ||============

[d] depositar.
[s] sacar.
[e] extrato.
[q] sair.

(Selecione uma opção válida.)
==>"""

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor a ser depositado R$: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Operação realizada: depósito no valor de R${valor:.2f}')

        else:
            print('Operação falhou: valor inválido...')

    elif opcao == 's':
        valor = float(input('Digite o valor a ser sacado R$: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou: saldo insuficiente...')
        elif excedeu_limite:
            print(f'Operação falhou: valor do saque excede limite de R${limite}...')
        elif excedeu_saque:
            print(f'Operação falhou: número máximo de saques excedido. Limite de {LIMITE_SAQUES} saques...')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'Operação realizada: saque no valor de R${valor:.2f}')
        else:
            print('Operação falhou: valor inválido...')

    elif opcao == 'e':
        print('\n==========|| EXTRATO ||==========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('===================================')

    elif opcao == 'q':
        break
    else:
        print('Operação falhou: por favor, selecione uma das opções abaixo...')

        