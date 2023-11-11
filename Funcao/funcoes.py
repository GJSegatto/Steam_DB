from SQL import criacao as cria
import psycopg2

def inicializacao():
    global cnx 
    global cursor
    cnx = psycopg2.connect(host='localhost', port='5432', database='Steam', user='postgres', password='teste123')
    cnx.autocommit = False
    cursor = cnx.cursor()

def fechamento():
    cnx.close()

def menu():
    print("""
        --- STEAMZERA ---
    [1] - Criar Tabelas.
    [2] - 
    [3] - 
    [4] - 
    [5] - 
    [6] - 
    [0] - Sair.
    """
)
    
def criaTabelas():
    try:
        for nome_tabela in cria.tabelas:
            query = cria.tabelas[nome_tabela]
            cursor.execute(query)
        cnx.commit()
        
    except psycopg2.Error as err:
        print("Não foi possível fazer a inclusão das tabelas por conta do seguinte erro: \n", err.args)

def op2():
    print("2")

def op3():
    print("3")

def op4():
    print("4")

def op5():
    print("5")

def op6():
    print("6")

def op0():
    print("0")