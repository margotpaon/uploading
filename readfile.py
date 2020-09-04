import sqlite3 as bd
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template')

#Abrir arquivo de texto com pandas e eliminar tabulações
df = pd.read_csv('dados.txt', sep='\t')

#conectando e criando um banco de dados com Sqlite
conn = bd.connect("controle_compras.db")

#Criando cursor para iterações no banco 
cur = conn.cursor()

#Deletando tabela
cur.execute('''DROP TABLE IF EXISTS ordens''')

#Converter data frame para SQL e criando a tabela
df.to_sql('ordens', conn, if_exists='replace', index=False)

#Salvando alterações no banco
conn.commit()

#Selecionando todas colunas da tabela para serem exibidos
cur.execute('SELECT * FROM ordens')

items = cur.fetchall()

#exibindo na página
@app.route('/')
def index():
    return render_template("index.html", items=items)

if __name__ == "__main__":
 app.run()

#Fechando a conexão do banco
conn.close()