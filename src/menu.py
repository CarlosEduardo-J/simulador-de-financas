from transacoes import adicionar_transacao, listar_transacao, ver_saldo
from relatorios import gerar_relatorio

def exibir_menu():
    while True:
        print('\n💰 SIMULADOR DE FINANÇAS PESSOAIS')
        print('1. Adicionar transação')
        print('2. Listar transação')
        print('3. Ver saldo atual')
        print('4. Gerar relatório')
        print('5. Sair')

        opcao = input('Escolha uma das opções acima:')
        if opcao == '1':
            adicionar_transacao()
        elif opcao == '2':
            listar_transacao()
        elif opcao == '3':
            ver_saldo()
        elif opcao == '4':
            gerar_relatorio()
        elif opcao == '5':
            print('Saindo... até logo!')
            break
        else:
            print('Selecione uma opção válida')
