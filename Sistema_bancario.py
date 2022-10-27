from time import sleep
import requests


def dec():
    print(f'=' * 98)


def div():
    print(f'-' * 98)


def pul():
    print('\n')


def load():
    pul()
    print(f'-' * 98)
    print(f'AGUARDE...')
    print(f'-' * 98)
    pul()
    sleep(1)


def msg():
    dec()
    print(f'SUJEITO A ALTERAÇÃO ATÉ O FINAL DO DIA.')
    dec()


def menu():
    opcoes = '''
        =============== MENU ==================
                [1]\t\tDEPÓSITO
                [2]\t\tSAQUE
                [3]\t\tEXTRATO
                [4]\t\tCÂMBIO
                [5]\t\tEMPRÉSTIMO
                [6]\t\tCADASTRAR NOVO USUÁRIO
                [7]\t\tCADASTRAR NOVA CONTA
                [8]\t\tLISTAR CONTAS
                [0]\t\tSAIR
                ESCOLHA UMA OPÇÃO
        =======================================
                    ==> '''
    return input(opcoes)


def depositar(saldo, deposito, extrato, /):
    div()
    if deposito >= 10:
        saldo += deposito
        load()
        extrato += f'\nDepósito:\t\tR${deposito:,.2f} +'
        div()
        print('Depósito realizado com sucesso!')
        div()
        pul()
        sleep(1)
        dec()
        print(f'O VALOR DE DEPÓSITO É DE R${deposito:,.2f}')
        print(f'SALDO ATUAL É DE R${saldo:,.2f}')
        msg()
        pul()

    else:
        print('Operação não realizado! O valor mínimo para depósito é de R$10.00.')
        div()
        sleep(1)
        pul()
        dec()
        msg()
        dec()
        pul()

    return saldo, deposito, extrato


def sacar_real(saldo, saque_real, extrato, limite_r, numero_saques, LIMITE_SAQUES):
    div()
    excedeu_saldo = saque_real > saldo
    excedeu_limite = saque_real > limite_r
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    if excedeu_saldo:
        pul()
        div()
        print('Falha na operação! Você não tem saldo Suficiente.')
        div()
        pul()
    elif excedeu_limite:
        pul()
        div()
        print(f'Falha na operação! O valor do saque excede o limite diário de R${limite_r:,.2f}')
        div()
        pul()
    elif excedeu_saques:
        pul()
        div()
        print('Falha na operação! Número máximo de saques excedido.')
        div()
        pul()
    elif saque_real >= 5:
        saldo -= saque_real
        pul()
        load()
        dec()
        extrato += f'\nSaque:\t\t\tR${saque_real:,.2f} -'
        print('Saque realizado com sucesso!')
        sleep(1)
        print(f'Saldo atual é de {saldo:,.2f}')
        msg()
        pul()
        numero_saques += 1
    else:
        pul()
        div()
        print('Operação não realizado! O valor mínimo para saque é de R$5.00.')
        div()
        pul()

    return saldo, saque_real, extrato, numero_saques


def sacar_dolar(dolar, saque_dolar, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = saque_dolar > dolar
    excedeu_limite = saque_dolar > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        pul()
        div()
        print('Falha na operação! Você não tem saldo Suficiente.')
        div()
        pul()
    elif excedeu_limite:
        pul()
        div()
        print('Falha na operação! O valor do saque excede o limite diário.')
        div()
        pul()
    elif excedeu_saques:
        pul()
        div()
        print('Falha na operação! Número máximo de saques excedido.')
        div()
        pul()
    elif saque_dolar > 20:
        dolar -= saque_dolar
        pul()
        load()
        dec()
        extrato += f'\nSaque:\t\t\tUS${saque_dolar:,.2f} -'
        print('Saque realizado com sucesso!')
        sleep(1)
        print(f'O valor disponível em dólares é de U${dolar:,.2f}')
        msg()
        pul()
        numero_saques += 1
    else:
        pul()
        div()
        print('Operação não realizado! O valor mínimo para saque é de US$20.00.')
        div()
        pul()
    return saldo, saque_dolar, extrato, numero_saques


def exibir_extrato(saldo, extrato, dolar):
    load()
    pul()
    print('-' * 41, 'EXTRATO'.center(10), '-' * 44)
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\t\tR${saldo:,.2f}')
    print(f'Saldo Dolar:\tUS${dolar:,.2f}')
    msg()
    div()
    pul()


def cotacao_atual():
    load()
    pul()
    div()
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
    response = requests.get(url)
    if response.status_code == 200:
        dolar = response.json()['USD']['low']
        print(f'Cotação atual:\tUS${float(dolar):,.2f}')
    div()


def comprar_dolar(saldo, real, valor, extrato, dolar):
    load()
    pul()
    dec()
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
    response = requests.get(url)
    if response.status_code == 200:
        dolar = response.json()['USD']['low']
        valor = real / float(dolar)
        print(f'Com o valor de R${real:,.2f}, você comprou US${valor:,.2f}')
        excedeu_saldo = real > saldo
        if excedeu_saldo:
            pul()
            div()
            print('Falha na operação! Você não tem saldo Suficiente.')
            div()
            pul()
        else:
           #PROBLEMA DO PROGRAMA ESTÁ AKI!
            saldo -= real
            dolar += valor
            extrato += f'\nConvertido:\tR${real:,.2f} -'
            extrato += f'\nDólares:\tUS${valor:,.2f} +'
            dec()
            pul()
    return saldo, real, dolar, valor, extrato,


def pedir_emprestimo(saldo,emprestimo,extrato):
    load()
    div()
    saldo += emprestimo
    extrato += f'\nEmpréstimo:\tR${emprestimo:,.2f} +'
    sleep(0.5)
    parcelamento = int(input(f'''DESEJA PARCELAR EM QUANTAS VEZES
    (LIMITE DE PARCELAS 48X):'''))
    div()
    parcelas = float(emprestimo / parcelamento)
    juros = float(parcelas * 0.15) + parcelas
    total = float(juros * parcelamento)
    load()

    if parcelamento <= 48:
        dec()
        print(f'''DETALHES DO EMPRÉSTIMO:\n
            VALOR SOLICITADO:\tR${emprestimo:,.2f}
            QUANTIDADE DE PARCELAS:\t{parcelamento}x
            VALOR DE PARCELAS:\tR${juros:,.2f}
            TOTAL:\tR${total:,.2f}
        ''')
        dec()
        sleep(1)
        div()
        print(f'SALDO ATUAL:\tRS{saldo:,.2f}')
        msg()
        pul()
    else:
        dec()
        print(f'ERRO! O LIMITE DE PARCELAS É 48X')
        dec()
        pul()


def criar_usuario(usuarios):
    cpf = input('INFORME O CPF(SOMENTE NÚMERO): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        pul()
        print('Já existe usuário com esse CPF!')
        return
    nome = input('INFORME O NOME COMPLETO: ')
    nascimento = input('INFORME A DATA DE NASCIMENTO(DD-MM-AAAA): ')
    endereco = input('INFORME O ENDEREÇO (LOGRADOURO, Nº - BAIRRO - CIDADE/UF): ')
    usuarios.append({'nome': nome, 'nascimento': nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso! ')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('INFORME O CPF DO USUÁRIO: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('USUÁRIO NÃO ENCONTRADO! FLUXO ENCERRADO.')


def listar_contas(contas):
    div()
    for conta in contas:
        linha = f'''
            AGÊNCIA:\t{conta['agencia']}
            CONTA:\t\t{conta['numero_conta']}
            TÍTULAR:\t{conta['usuario']['nome']}
        '''
        print(linha)
    div()
