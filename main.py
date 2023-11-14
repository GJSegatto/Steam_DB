from Funcao import funcoes as fc

try:
    fc.inicializacao()
    opcao = 1

    while opcao != 0:
        fc.menu()
        opcao = int(input("Selecione um numero: "))

        if opcao == 0:
            fc.fechamento()
        elif opcao == 1:
            fc.criaTabelas() 
        elif opcao == 2:
            fc.drop_tabelas()   
        elif opcao == 3:
            fc.insert_valores()    
        elif opcao == 4:
            fc.consulta_total_genero()    
        elif opcao == 5:
            fc.op5()    
        elif opcao == 6:
            fc.op6()   
        elif opcao == 7:
            print("n tem 7 ainda")   
        else:
            print("Escolha um valor entre 0 e 7.")

except fc.psycopg2.Error as err:
    print("Não foi possível se conectar ao Banco de Dados devido ao seguinte erro: \n", err.args)

