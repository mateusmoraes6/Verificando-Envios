# Extração de E-mails Não Enviados de um Arquivo CSV

Este guia descreve os passos tomados para extrair e-mails não enviados de um arquivo CSV e apresentá-los em um formato apropriado usando Python.

## Situação

Este projeto visa resolver um problema em que um sistema web de uma empresa responsável por processos seletivos teve um rompimento na criação de um arquivo JSON com a lista dos candidatos já avisados da alteração de um concurso adiado. Como resultado, foram gerados dois novos arquivos com dados parciais. O objetivo é criar uma função que, com base nessas informações, retorne uma lista de e-mails que ainda precisam ser enviados.

Os dados são fornecidos em dois dicionários Python com a seguinte estrutura: 'nome', 'email' e 'enviado'. Cada dicionário contém listas associadas a essas chaves, onde 'nome' e 'email' armazenam listas de nomes e e-mails, respectivamente, e 'enviado' armazena uma lista de valores booleanos indicando se o e-mail correspondente já foi enviado.

Para solucionar o problema, será criada uma função que tratará os dados fornecidos nos dicionários e retornará uma lista de e-mails que ainda não foram enviados.

Exemplo de estrutura de dados:

```
dict_1 = {
  'nome': ['nome_1'],
  'email': ['email_1'],
  'enviado': [False]
}
```

Este resumo destaca os principais pontos do problema e define o escopo do projeto a ser abordado pelo desenvolvedor.

## 1. Preparação dos Dados

Os dados devem estar no formato correto no arquivo CSV, com cada linha representando um registro contendo nome, e-mail e um indicador de envio.

Exemplo:
`nome, email, true/false`

nome do arquivo:
`tratando_dados.py`

Os que estão em um arquivo chamado `dados.csv` serão tratados no arquivo anterior.

## 2. Estrutura dos Dados em Python

Os dados serão armazenados em dois dicionários Python: `dados_1` e `dados_2`, correspondendo aos dois conjuntos de dados separados por uma linha vazia no arquivo CSV.

## 3. Extração dos E-mails Não Enviados

Um script Python será usado para ler o arquivo CSV, armazenar os dados nos dicionários e extrair os e-mails que ainda não foram enviados.

## 4. Resultado

Os e-mails não enviados serão apresentados em um formato adequado de forma organizada.