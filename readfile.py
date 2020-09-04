import sqlite3 as bd
import pandas as pd

#Abrir arquivo de texto com pandas e eliminar tabulações
df = pd.read_csv('dados.txt', sep='\t')

#conectando e criando um banco de dados com Sqlite
conn = bd.connect("controle_compras.db")

#Converter data frame para SQL e criando a tabela
df.to_sql('ordens', conn, if_exists='replace', index=False)

#Selecionando a tabela para inserção
pd.read_sql('select * from ordens', conn)

#Fechando a conexão do banco
conn.close()