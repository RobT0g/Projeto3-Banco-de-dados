import pandas as pd
from mysql import connector

def main():
    con = connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'vendas'
    )
    cursor = con.cursor()

    df = pd.read_excel('VendaCarros.xlsx')
    client = df[['NomeCliente']].dropna(how='all').drop_duplicates().reset_index(drop=True).copy()
    car = df[['Fabricante', 'Modelo', 'Ano']].dropna(how='all').drop_duplicates().reset_index(drop=True).copy()
    fab = df[['Fabricante']].dropna(how='all').drop_duplicates().reset_index(drop=True).copy()
    cor = df[['Cor']].dropna(how='all').drop_duplicates().reset_index(drop=True).copy()

    print(fab)
    print(cor)
    #return

    def quote(val):
        if type(val) is str:
            return val.replace("'", r'\'')
        return val

    for k, v in client.iterrows():
        cursor.execute(f'''insert into cliente (nome) values ('{quote(v['NomeCliente'])}');''')
    con.commit()

    for k, v in fab.iterrows():
        cursor.execute(f'''insert into fabricante (fabricante) values ('{quote(v['Fabricante'])}');''')
    con.commit()

    for k, v in cor.iterrows():
        cursor.execute(f'''insert into cor (cor) values ('{v['Cor']}');''')
    con.commit()

    for k, v in car.iterrows():
        cursor.execute(f'''insert into carros (modelo, ano, fabricante) values ('{v['Modelo']}', '{v['Ano']}', '{fab.loc[fab['Fabricante'] == v['Fabricante']].index[0]+1}');''')
    con.commit()


    for k, v in df.iterrows():
        carro = car.loc[(v['Fabricante'] == car['Fabricante']) & (v['Modelo'] == car['Modelo']) &  (v['Ano'] == car['Ano'])]
        cursor.execute(f'''insert into venda (estado, valor, custo, desconto, entrega, mao, data, cliente, carro, cor) values 
            ('{quote(v['Estado'])}', '{quote(v['ValorVenda'])}', '{quote(v['ValorCusto'])}', '{quote(v['TotalDesconto'])}', 
            '{quote(v['CustoEntrega'])}', '{quote(v['CustoMaoDeObra'])}', '{quote(v['DataNotaFiscal'])}', '{client.loc[client['NomeCliente'] == v['NomeCliente']].index[0]+1}',
            '{list(carro.index)[0]+1}', '{cor.loc[cor['Cor'] == v['Cor']].index[0]+1}');''')
        con.commit()
    
if __name__ == '__main__':
    main()
