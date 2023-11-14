import psycopg2
from SQL import criacao, drop, insercoes, consultas

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
    [4] - 
    [5] - 
    [6] - 
    [0] - Sair.
    """
)

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
        
def op4():
    print("4")

def op5():
    print("5")

def op6():
    print("6")

def op0():
    print("0")