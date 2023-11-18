delete = ("""
    DELETE FROM item_raridade WHERE id_item = 3038;
    DELETE FROM item WHERE id_item = 3038;
          
    DELETE FROM compra_jogo WHERE id_jogo = 1011;
    DELETE FROM jogo_genero WHERE id_jogo = 1011;
    DELETE FROM midia WHERE id_jogo = 1011;
    DELETE FROM compra_expansao WHERE id_expansao = 5006;
    DELETE FROM expansao WHERE id_jogo = 1011;
    DELETE FROM jogo WHERE id_jogo = 1011;
""")