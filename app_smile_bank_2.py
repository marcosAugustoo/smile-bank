import textwrap

def menu():
    menu = """\n
    ============|| Menu ||============
    [d]\tdepositar.
    [s]\tsacar.
    [e]\textrato.
    [nc]\tnova conta.
    [lc]\tlistar contas.
    [nu]\tnovo usuário.
    [q]\tsair.

    (Selecione uma opção válida.)
    ==>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print(f'=== Operação realizada: depósito no valor de R${valor:.2f} ===')
    else:
        print('@@@ Operação falhou: valor informado é inválido @@@')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
            print('@@@ Operação falhou: saldo insuficiente @@@')
    elif excedeu_limite:
        print(f'@@@ Operação falhou: valor do saque excede limite de R${limite} @@@')
    elif excedeu_saque:
        print(f'@@@ Operação falhou: número máximo de saques excedido. Limite de {limite_saques} @@@')

    elif valor > 0:
        saldo -= valor
        extrato = f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print(f'\n=== Operação realizada: saque no valor de {valor:.2f}===')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n=======|| EXTRATO ||=======')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print('')
    print('')

def criar_usuario(usuarios):

    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe um usuário com este CPF @@@')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento(dd-mm-aa): ')
    endereco = input('Informe seu endereço (logradouro, número - bairro , cidade/sigla Estado): ')

    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':endereco})

    print('=== Usuário criado com sucesso ===')

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('=== Conta criada com sucesso ===')
        return {'agencia':agencia,
                'numero_conta':numero_conta,
                'usuario':usuario}
    
    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agência\t{conta['agencia']}
            CC:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('='*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = 1

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valor a ser depositado R$: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Digite o valor a ser sacado R$: '))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == 'e':

            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 'nu':

            criar_usuario(usuarios)

        elif opcao == 'nc':

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação falhou: por favor, selecione uma das opções abaixo...')

main()