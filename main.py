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
car = pd.DataFrame(columns=['Fabricante', 'Modelo', 'Cor', 'Ano'])

def quote(val):
    if type(val) is str:
        return val.replace("'", r'\'')
    return val

for k, v in df.iterrows():
    if v['NomeCliente'] not in client:
        cursor.execute(f'''insert into cliente (nome_Cliente) values ('{quote(v['NomeCliente'])}');''')
        client.append(v['NomeCliente'])
    carro = v[['Fabricante', 'Modelo', 'Cor', 'Ano']].copy()
    if len((d:=car.loc[(car['Fabricante'] == carro['Fabricante']) & (car['Modelo'] == carro['Modelo']) & (car['Cor'] == carro['Cor']) & (car['Ano'] == carro['Ano'])])) == 0:
        car = car.append(carro, ignore_index=True)
        cursor.execute(f'''insert into carros (Fabricante, modelo, cor, ano) values ('{quote(v['Fabricante'])}', '{quote(v['Modelo'])}', '{quote(v['Cor'])}', '{quote(v['Ano'])}');''')
    cursor.execute(f'''insert into venda (Estado, Valor_Venda, Valor_Custo, Total_Desconto, Custo_Entrega, Custo_Mao, Data_Compra, id_Cliente, id_Carro) values 
        ('{quote(v['Estado'])}', '{quote(v['ValorVenda'])}', '{quote(v['ValorCusto'])}', '{quote(v['TotalDesconto'])}', '{quote(v['CustoEntrega'])}', '{quote(v['CustoMaoDeObra'])}', 
        '{quote(v['DataNotaFiscal'])}', '{client.index(v['NomeCliente'])+1}', '{len(car)+1 if len(d) == 0 else d.index[0]}');''')
    con.commit()
    

