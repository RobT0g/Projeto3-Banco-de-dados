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

def quote(val):
    if type(val) is str:
        return val.replace("'", r'\'')
    return val

for k, v in car.iterrows():
    cursor.execute(f'''insert into carros (Fabricante, modelo, cor, ano) values ('{v['Fabricante']}', '{v['Modelo']}', '{v['Cor']}', '{v['Ano']}');''')
con.commit()


for k, v in df.iterrows():
    try:
        cursor.execute(f'''insert into cliente (nome_Cliente) values ('{quote(v['NomeCliente'])}');''')
        client.append(v['NomeCliente'])
    except:
        pass
    print(client)
    carro = car.loc[(v['Fabricante'] == car['Fabricante']) & (v['Modelo'] == car['Modelo']) &  (v['Cor'] == car['Cor']) &  (v['Ano'] == car['Ano'])]
    cursor.execute(f'''insert into venda (Estado, Valor_Venda, Valor_Custo, Total_Desconto, Custo_Entrega, Custo_Mao, Data_Compra, id_Cliente, id_Carro) values 
        ('{quote(v['Estado'])}', '{quote(v['ValorVenda'])}', '{quote(v['ValorCusto'])}', '{quote(v['TotalDesconto'])}', '{quote(v['CustoEntrega'])}', '{quote(v['CustoMaoDeObra'])}', 
        '{quote(v['DataNotaFiscal'])}', '{client.index(v['NomeCliente'])+1}', '{list(carro.index)[0]+1}');''')
    con.commit()
    

