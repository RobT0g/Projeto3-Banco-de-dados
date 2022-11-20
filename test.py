
import pandas as pd
from mysql import connector
con = connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'vendas'
)
cursor = con.cursor()

df = pd.read_excel('VendaCarros.xlsx')
client = []
car = df[['Fabricante', 'Modelo', 'Cor', 'Ano']].dropna(how='all').drop_duplicates().reset_index(drop=True).copy()
for k, v in car.iterrows():
    cursor.execute(f'''insert into cliente (nome_Cliente) values ('{v['Fabricante']}{v['Modelo']}{v['Cor']}{v['Ano']}');''')
con.commit()