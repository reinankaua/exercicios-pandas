import pandas as pd

df = pd.read_excel('Notas.xlsx')

print(f"Qual a quantidade de linhas e colunas desse dataframe? \n{df.shape}\n\n")
print(f"Quais os tipos das váriaveis desse dataframe? \n{df.dtypes}\n\n")
print(f"Há valores nulos nesse dataframe? \n{df.isnull().sum()}\n\n")
df1 = df[['genero', 'almoco']]
print(f"Crie um novo dataframe chamado 'df1', esse dataframe deve possuir somente as colunas 'genero' e 'almoco'. \n{df1}\n\n")
print(f"Ordene o dataset de forma crescente de acordo com a nota de redação. \n{df.sort_values(by='nota redacao')}\n\n")
print(f"Qual é a maior nota em matemática? \n{df[['nota matematica']].max()}\n\n")
print(f"Qual é a menor nota em literatura? \n{df[['nota literatura']].min()}\n\n")
print(f"Qual é a soma de todas as notas em redacao? \n{df[['nota redacao']].sum()}\n\n")
print(f"Qual é a nota em matemática do aluno de index 502?")


"""
print(f"Quantos grupos étnicos existem no dataframe?")
print(f"Dentro da coluna etnia, qual é o grupo que possui a maior quantidade de pessoas?Qual é o index da aluna que tirou a menor nota em literatura?")
print(f"Qual é a escolaridade mais comum entre os pais dos alunos?")
print(f"Printe a correlação entre as variáveis e identifique a variável que tem a maior correlação positiva com as notas em redação.")
print(f"Realize um groupby e agrupe a coluna 'escolaridade dos pais'. Após agrupado, verifique qual é a maior nota média em matemática dentre os grupos.")
print(f"Crie uma nova coluna chamada 'media geral', ela deve ser uma média das notas de matemática, literatura e redação.")
print(f"Verifique qual é a média geral de pessoas que completaram o simulado e compare com a média geral de pessoas que não completaram o simulado.")

"""


