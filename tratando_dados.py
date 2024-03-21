import csv

# Função para converter 'True'/'False' em booleano
def str_para_booleano(valor):
    if valor.lower() == 'true':
        return True
    elif valor.lower() == 'false':
        return False
    else:
        return valor

# Arquivo CSV
arquivo_csv = 'dados.csv'

# Dicionários para armazenar os dados
dados_1 = {'nome': [], 'email': [], 'enviado': []}
dados_2 = {'nome': [], 'email': [], 'enviado': []}

# Abre o arquivo CSV para leitura
with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)

    # Variável para determinar em qual dicionário os dados devem ser armazenados
    em_dados_1 = True

    # Lê cada linha do arquivo CSV
    for linha in leitor_csv:
        # Verifica se a linha está vazia, indicando a separação entre os dois conjuntos de dados
        if not linha:
            em_dados_1 = False
            continue

        # Adiciona os dados à lista apropriada
        if em_dados_1:
            dados_1['nome'].append(linha[0])
            dados_1['email'].append(linha[1])
            dados_1['enviado'].append(str_para_booleano(linha[2])) 
        else:
            dados_2['nome'].append(linha[0])
            dados_2['email'].append(linha[1])
            dados_2['enviado'].append(str_para_booleano(linha[2]))  

# Imprime os dados lidos
print("\ndados_1 = {")
for chave, valor in dados_1.items():
    print(f"    '{chave}': {valor},")
print("}")

print("\ndados_2 = {")
for chave, valor in dados_2.items():
    print(f"    '{chave}': {valor},")
print("}")
