from datetime import datetime
import csv

arquivo = 'dados/transacoes.csv'

def gerar_relatorio():
    total_entrada = total_saida = 0

    # Adicionado tratamento para o caso do arquivo não existir ou estar vazio
    try:
        with open(arquivo, 'r') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                if not linha:
                    continue
                    
                valor = float(linha['valor'])
                if linha['tipo'] == 'entrada':
                    total_entrada += valor
                else:
                    total_saida += valor
    except FileNotFoundError:
        print(f"Aviso: Arquivo de transações '{arquivo}' não encontrado. O relatório será zerado.")
        # Se o arquivo não for encontrado, total_entrada e total_saida permanecem 0.
        
    saldo = total_entrada - total_saida
    data = datetime.now().strftime('%d/%m/%Y')
    
    nome_relatorio = f'relatorio_{data}.txt'

    with open(nome_relatorio, 'w') as f:
        f.write(f'RELATORIO FINANCEIRO ({data})\n')
        f.write(f'Entradas: R$ {total_entrada:.2f}\n')
        f.write(f'Saídas: R$ {total_saida:.2f}\n')
        f.write(f'Saldo final: R$ {saldo:.2f}\n')
    
    print(f'Relatório gerado com sucesso em {nome_relatorio}')