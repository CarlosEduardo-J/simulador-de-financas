import csv
from datetime import datetime

ARQUIVO_TRANSACOES = 'dados/transacoes.csv'

def adicionar_transacao():
    tipo = input('Tipo (entrada/saída):').lower()
    descricao = input('Descrição:')
    # Adicionado um bloco try/except simples para garantir que o valor seja um número
    try:
        valor = float(input('Valor:'))
    except ValueError:
        print("Valor inválido. Transação não adicionada.")
        return
        
    data = datetime.now().strftime('%d/%m/%Y')

    with open(ARQUIVO_TRANSACOES, 'a', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow([tipo, descricao, valor, data])

    print('Transação adicionada com exito!')

def listar_transacao():
    try:
        with open(ARQUIVO_TRANSACOES, 'r') as f:
            leitor = csv.reader(f)

            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("Nenhuma transação encontrada. O arquivo 'dados/transacoes.csv' não existe.")

def ver_saldo():
    saldo = 0
    try:
        with open(ARQUIVO_TRANSACOES, 'r') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if not linha or len(linha) < 3:
                    continue
                    
                try:
                    valor = float(linha[2])
                except ValueError:

                    print(f"Aviso: Valor inválido encontrado na linha: {linha}. Ignorando.")
                    continue
                    
                if linha[0] == 'entrada':
                    saldo += valor
                elif linha[0] == 'saída':
                    saldo -= valor
            
            print(f'Saldo atual: R$ {saldo:.2f}')
            
    except FileNotFoundError:
        print("Nenhuma transação encontrada. Saldo é R$ 0.00.")
