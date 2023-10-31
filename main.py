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
print(f"Qual é a nota em matemática do aluno de index 502? \n{df.iloc[[502],[5]]}\n\n")
print(f"Quantos grupos étnicos existem no dataframe? \n{len(pd.unique(df['etnia']))}\n\n")
print(f"Dentro da coluna etnia, qual é o grupo que possui a maior quantidade de pessoas? \n{df.value_counts('etnia').idxmax()}\n\n")

alunas_df = df[df['genero'] == 'female']
indice_menor_nota = alunas_df[['nota literatura']].idxmin()

print(f"Qual é o index da aluna que tirou a menor nota em literatura? \n{indice_menor_nota}\n\n")
print(f"Qual é a escolaridade mais comum entre os pais dos alunos? \n{df.value_counts('escolaridade dos pais').idxmax()}\n\n")



# Não entendi essa pegunta :(
# print(f"Printe a correlação entre as variáveis e identifique a variável que tem a maior correlação positiva com as notas em redação.")



grupo_escolaridade = df.groupby('escolaridade dos pais')['nota matematica'].mean()
grupo_com_maior_nota_media = grupo_escolaridade.idxmax()
maior_nota_media = grupo_escolaridade.max()

print(f"Realize um groupby e agrupe a coluna 'escolaridade dos pais'. Após agrupado, verifique qual é a maior nota média em matemática dentre os grupos. \n{maior_nota_media}\n\n")

completaram = df[df['simulado'] == 'completed']
nao_completaram = df[df['simulado'] == 'none']

media_completaram_por_materia = completaram[['nota matematica', 'nota literatura', 'nota redacao']].mean()
media_nao_completaram_por_materia = nao_completaram[['nota matematica', 'nota literatura', 'nota redacao']].mean()

media_completaram_geral = media_completaram_por_materia.mean()
media_nao_completaram_geral = media_nao_completaram_por_materia.mean()

print(f"Verifique qual é a média geral de pessoas que completaram o simulado e compare com a média geral de pessoas que não completaram o simulado. (RESPOSTA ABAIXO)")

print(f"Media dos que completaram o simulado: {media_completaram_geral}")
print(f"Media dos que não completaram o simulado: {media_nao_completaram_geral}")
