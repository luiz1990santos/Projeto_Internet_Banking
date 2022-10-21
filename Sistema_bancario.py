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
    print(f'SUJEITO A ALTERAÇÃO ATÉ O FINAL DO DIA.')


try:
    dec()
    print(' ' * 29, f'--- SISTEMA BANCÁRIO ---')
    dec()

    menu = str('''MENU:
                [1]   SALDO
                [2]   SAQUE
                [3]   EXTRATO
                [4]   DEPÓSITO
                [5]   CÂMBIO
                [6]   EMPRÉSTIMO
                [7]   SAIR
                ESCOLHA UMA OPÇÃO: ''')

    SENHA = 123456
    saldo = 0
    dolar = 0
    limite = float(2000)
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 5
    contador = 1
    TENTATIVAS = 3

    while contador < 4:
        pul()
        div()
        usuario = str(input(f'\nDIGITE O LOGIN: ')).strip().upper().lower()
        password = int(input('DIGITE SUA SENHA: '))
        div()
        contador += 1
        TENTATIVAS -= 1
        if SENHA == password:
            load()
            print(' ' * 40, f' ACESSO PERMITIDO ')
            sleep(1)
            pul()
            dec()
            print(' ' * 29, f'{usuario} seja bem-vindo, como posso ajudar hoje?'.upper())
            dec()
            sleep(1)
            while True:
                opcao = int(input(menu))
                if opcao == 1:
                    load()
                    dec()
                    print(f'O Saldo atual é de R${saldo:,.2f}')
                    print(f'O valor disponível em dólares é de U${dolar:,.2f}')
                    msg()
                    dec()
                    pul()
                elif opcao == 2:
                    load()
                    div()
                    saque = str(input('deseja fazer um saque em Real(R) ou Dolar(D)'))
                    if saque in 'Rr':
                        saque_real = float(input(f'DIGITE A VALOR DO SAQUE(R$): '))
                        div()

                        excedeu_saldo = saque_real > saldo
                        excedeu_limite = saque_real > limite
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
                        elif saque_real > 0:
                            saldo -= saque_real
                            pul()
                            load()
                            dec()
                            extrato += f'\nSaque: R${saque_real:,.2f} -'
                            print(f'Saldo atual é de {saldo:,.2f}')
                            print(f'O valor disponível em dólares é de U${dolar:,.2f}')
                            msg()
                            pul()
                            numero_saques += 1
                        else:
                            pul()
                            div()
                            print('Falha na operação! O valor informado não é válido.')
                            div()
                            pul()
                    elif saque in 'Dd':
                        saque_dolar = float(input(f'DIGITE A VALOR DO SAQUE(US$): '))
                        div()

                        excedeu_saldo = saque_dolar > saldo
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
                        elif saque_dolar > 0:
                            dolar -= saque_dolar
                            pul()
                            load()
                            dec()
                            extrato += f'\nSaque: US${saque_dolar:,.2f} -'
                            print(f'Saldo atual é de {saldo:,.2f}')
                            print(f'O valor disponível em dólares é de U${dolar:,.2f}')
                            msg()
                            pul()
                            numero_saques += 1
                        else:
                            pul()
                            div()
                            print('Falha na operação! O valor informado não é válido.')
                            div()
                            pul()
                elif opcao == 3:
                    load()
                    pul()
                    print('-' * 41, 'EXTRATO'.center(10), '-' * 44)
                    print('Não foram realizadas movimentações.' if not extrato else extrato)
                    print(f'\nSaldo: R${saldo:,.2f}')
                    print(f'Saldo Dolar: US${dolar:,.2f}')
                    div()
                    pul()

                elif opcao == 4:
                    div()
                    deposito = float(input(f'DIGITE O VALOR DE DEPÓSITO (R$): '))
                    if deposito > 0:
                        saldo += deposito
                        load()
                        dec()
                        extrato += f'\nDepósito: R${deposito:,.2f} +'
                        print(f'O VALOR DE DEPÓSITO É DE R${deposito:,.2f}')
                        print(f'SALDO ATUAL É DE R${saldo:,.2f}')
                        msg()
                        pul()

                    else:
                        print('Falha na operação! O valor informado é inválido.')
                    div()
                    sleep(1)
                    pul()
                    dec()

                    msg()
                    dec()
                    pul()
                elif opcao == 5:
                    div()
                    real = float(input('Digite o valor em reais para cotação: '))
                    div()
                    load()
                    pul()
                    dec()
                    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
                    response = requests.get(url)
                    if response.status_code == 200:
                        dol = response.json()['USD']['low']
                        valor = real / float(dol)
                        print(f'O dolar pela cotação atual é US${float(dol):,.2f}')
                        print(f'Com o valor de R${real:,.2f}, você comprou US${valor:,.2f}')

                        excedeu_saldo = real > saldo

                        if excedeu_saldo:
                            pul()
                            div()
                            print('Falha na operação! Você não tem saldo Suficiente.')
                            div()
                            pul()
                        else:
                            saldo -= real
                            dolar += valor
                            extrato += f'\nConvertido: R${real:,.2f} -'
                            extrato += f'\nDólares: US${valor:,.2f} +'
                    dec()
                    pul()

                elif opcao == 6:
                    load()
                    div()
                    emprestimo = float(input(f'DIGITE O VALOR DE EMPRÉSTIMO QUE DESEJA (R$): '))
                    saldo += emprestimo
                    extrato += f'\nEmpréstimo: R${emprestimo:,.2f} +'
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
                            VALOR SOLICITADO: R${emprestimo:,.2f}
                            QUANTIDADE DE PARCELAS: {parcelamento}x
                            VALOR DE PARCELAS: R${juros:,.2f}
                            TOTAL: R${total:,.2f}
                        ''')
                        dec()
                        sleep(1)
                        div()
                        print(f'SALDO ATUAL: RS{saldo:,.2f}')
                        msg()
                        pul()
                    else:
                        dec()
                        print(f'ERRO! O LIMITE DE PARCELAS É 48X')
                        dec()
                        pul()
                elif opcao == 7:
                    pul()
                    dec()
                    print(f'SESSÃO ENCERRADA.')
                    dec()
                    break
                else:
                    pul()
                    dec()
                    print(f'ESCOLHA UMA OPÇÃO VÁLIDA.')
                    dec()

        elif contador < 4:
            pul()
            dec()
            print(f'SENHA INVÁLIDA.')
            sleep(0.5)
            print(f'VOCÊ PODE TENTAR MAIS {TENTATIVAS} VEZE(S).')
            dec()
    else:
        sleep(0.5)
        pul()
        pul()
        pul()
        dec()
        print(' ' * 44, f'ACESSO NEGADO')
        sleep(0.3)
        print(' ' * 25, f'SEU ACESSO FOI BLOQUEADO, TENTE NOVAMENTE MAIS TARDE.')
        dec()
except NameError:
    pul()
    print('Erro! Opcão invãlida.')
except ValueError:
    pul()
    print('Erro! Valor digitado inválido.')
except KeyboardInterrupt:
    pul()
    print('Você encerrou.')
