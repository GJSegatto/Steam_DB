import psycopg2
from SQL import criacao, drop, insercoes, consultas
import matplotlib.pyplot as plt
import pandas as pd

def inicializacao():
    global cnx 
    global cursor
    cnx = psycopg2.connect(host='localhost', port='5432', database='Steam', user='postgres', password='teste123')
    cnx.autocommit = False
    cursor = cnx.cursor()
    drop_tabelas()

def fechamento():
    cnx.close()

def menu():
    print("""
        --- STEAMZERA ---
    [1] - Criar Todas as Tabelas.
    [2] - Dropar Todas as Tabelas.
    [3] - Popular Todas as Tabelas.
    [4] - Consulta 1: Distribuição de Gêneros.
    [5] - Consulta 2: Total Gasto por Usuário.
    [6] - Consulta 3: Total Vendido em Expansões no ano de 2023.
    [7] - Consulta Extra: Total de Itens com Raridade >= 3 por Usuário.
    [8] - Mostrar uma Tabela Específica.
    [0] - Sair.
    """
)

def monta_grafico(data, linha, coluna, titulo):
    plt.barh(data[linha], data[coluna])
    plt.gca().invert_yaxis()
    plt.xlabel(linha)
    plt.ylabel(coluna)
    plt.title(titulo)
    plt.get_current_fig_manager().full_screen_toggle()
    plt.show()

def criaTabelas():
    print("Iniciando criação das tabelas...")
    try:
        for nome_tabela in criacao.create:
            query = criacao.create[nome_tabela]
            cursor.execute(query)
        cnx.commit()
        
    except psycopg2.Error as err:
        print("Não foi possível fazer a criação das tabelas por conta do seguinte erro: \n", err.args)
        cnx.rollback()

def drop_tabelas():
    print("Dropando tabelas...")
    try:
        for nome_tabela in drop.drop:
            query = drop.drop[nome_tabela]
            cursor.execute(query)
        cnx.commit()
    except psycopg2.Error as err:
        print("Não foi possível dropar as tabelas por conta do seguinte erro: \n", err.args)
        cnx.rollback()

def insert_valores():
    print("Inserindo Valores nas Tabelas")
    try:
        for nome_tabela in insercoes.insercao:
            query = insercoes.insercao[nome_tabela]
            cursor.execute(query)
        cnx.commit()
    except psycopg2.Error as err:
        print("Não foi possível concluir a iclusão de valores no banco de dados por conta do seguinte erro:\n", err.args)
        cnx.rollback()
        
def consulta_total_genero():
    print("Primeira consulta: Exibir a quantidade de gêneros dos jogos que foram adquiridos pelos usuários da plataforma com o intuito de descobrir os gêneros mais apreciados pelos jogadores. \n")
    
    query = consultas.total_genero

    try:
        cursor.execute(query)
        recset = cursor.fetchall()
        data = pd.DataFrame(recset, columns = ['GENERO', 'QUANTIDADE'])
    
        print('\n')
        print(data)
        monta_grafico(data, linha='GENERO', coluna='QUANTIDADE', titulo='QUANTIDADE DE GÊNEROS')

    except psycopg2.Error as err:
        print("Não foi possível concluir a consulta por conta do seguinte erro: \n", err.args)


def consulta_total_gasto_usuario():
    print("Segunda Consulta: Total de dinheiro gasto por cada usuário na plataforma, a consulta envolve o total gasto tanto em jogos quanto em expansões, os valores são somados em um valor total final.")
    
    query = consultas.total_gasto_usuario
    
    try:
        cursor.execute(query)
        recset = cursor.fetchall()
        data = pd.DataFrame(recset, columns=['USUÁRIO', 'GASTO (R$)'])
        
        print('\n')
        print(data)
        monta_grafico(data, linha='USUÁRIO', coluna='GASTO (R$)', titulo='TOTAL GASTO POR USUÁRIO')

    except psycopg2.Error as err:
        print("Não foi possível concluir a consulta por conta do seguinte erro: \n", err.args)

def consulta_total_expansoes_vendidas():
    print("Terceira Consulta: Total de valor vendido em DLC's disponíveis na loja no ano de 2023.")
    
    query = consultas.total_expansoes_vendidas
    try:
        cursor.execute(query)
        recset = cursor.fetchall()
        data = pd.DataFrame(recset, columns=['EXPANSÃO', 'VALOR TOTAL (R$)'])

        print('\n')
        print(data)
        monta_grafico(data, linha='EXPANSÃO', coluna='VALOR TOTAL (R$)', titulo='TOTAL VENDIDO POR EXPANSAO')

    except psycopg2.Error as err:
        print("Não foi possível concluir a consulta por conta do seguinte erro: \n", err.args)

def consulta_extra_raridades():
    print("Consulta Extra! Essa consulta mostra a quantidade de itens com raridade maior ou igual a 3 que usuários possuem.")
    query = consultas.total_raridade
    try:
        cursor.execute(query)
        recset = cursor.fetchall()
        data = pd.DataFrame(recset, columns=['USUÁRIO', 'ITENS COM RARIDADE >= 3'])
        
        print('\n')
        print(data)
        monta_grafico(data, linha='USUÁRIO', coluna='ITENS COM RARIDADE >= 3', titulo='TOTAL DE ITENS COM RARIDADE >= 3')
        
    except psycopg2.Error as err:
        print("Não foi possível concluir a consulta por conta do seguinte erro: \n", err.args)

def mostrar_tabela():
    print("\nSELECIONAR UMA DAS TABELAS: ")
    
    for table_name in criacao.create:
        print("\t" + table_name)
    try:
        name = input(str("\nDigite o nome da tabela que deseja consultar: ")).lower()
        query_colunas = "SELECT COLUMN_NAME FROM information_schema.columns WHERE TABLE_NAME = '{}';".format(name)
        cursor.execute(query_colunas)
        nomes_colunas = cursor.fetchall()
        colunas = list(sum(nomes_colunas, ()))
        query = "select * from " + name
        cursor.execute(query)
    except psycopg2.Error as err:
        print("Não foi possível concluir a consulta por conta do seguinte erro: \n", err.args)
    else:
        print("\nTABELA {}\n".format(name))
        myresult = cursor.fetchall()
        data = pd.DataFrame(myresult, columns=colunas)
        print(data)
