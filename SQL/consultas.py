total_genero = ("""
    SELECT genero.nome, SUM(res.quantidade) AS total_genero 
    FROM genero JOIN(
	    SELECT jogo.id_jogo, jogo_genero.id_genero, COUNT(jogo_genero.id_genero) AS quantidade 
        FROM jogo JOIN jogo_genero
	    ON jogo.id_jogo = jogo_genero.id_jogo
	    GROUP BY jogo.id_jogo, jogo_genero.id_genero
	    ) AS res
    ON res.id_genero = genero.id_genero
    GROUP BY genero.nome
    ORDER BY total_genero DESC
""")
