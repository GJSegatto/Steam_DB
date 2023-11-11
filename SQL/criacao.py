tabelas = {
    "usuario" : ("""
        CREATE TABLE usuario (
	    id_usuario serial PRIMARY KEY,
	    nickname varchar(50) NOT NULL UNIQUE,
	    email varchar(100),
	    senha varchar(100),
	    nome varchar(50),
	    descricao varchar(500),
	    nivel integer
        );
    """),
    "desenvolvedor" : ("""
        CREATE TABLE desenvolvedor (
	    id_dev integer PRIMARY KEY,
	    nome varchar(50) NOT NULL UNIQUE,
	    descricao varchar(200)
    );
    """),
    "amigo" : ("""
        CREATE TABLE amigo (
	    id_usuario integer REFERENCES usuario (id_usuario),
	    id_amigo integer REFERENCES usuario (id_usuario),
	    PRIMARY KEY(id_usuario, id_amigo)
        );
    """),
    "compra" : ("""
        CREATE TABLE compra (
	    id_compra serial PRIMARY KEY,
	    id_usuario integer REFERENCES usuario (id_usuario),
	    valor numeric NOT NULL
        );
    """),
    "raridade" : ("""
        CREATE TABLE raridade (
        id_raridade integer PRIMARY KEY,
        nome varchar(50) NOT NULL
        );
    """),
    "jogo" : ("""
        CREATE TABLE jogo (
	    id_jogo integer PRIMARY KEY,
	    id_dev integer REFERENCES desenvolvedor (id_dev),
	    nome varchar(100) NOT NULL,
	    descricao varchar(150),
	    valor numeric NOT NULL,
	    data_lancamento date NOT NULL
        );
    """),
    "compra_jogo" : ("""
        CREATE TABLE compra_jogo (
        id_jogo integer REFERENCES jogo (id_jogo),
        id_compra integer REFERENCES compra (id_compra),
        data_compra timestamp NOT NULL,
        comprovante varchar(50) NOT NULL UNIQUE,
        PRIMARY KEY(id_jogo, id_compra)
        );
    """),
    "item" : ("""
        CREATE TABLE item (
        id_item integer PRIMARY KEY,
        id_usuario integer REFERENCES usuario(id_usuario),
        id_jogo integer REFERENCES jogo(id_jogo),
        tipo varchar(50) NOT NULL,
        descricao varchar(100),
        nome varchar(50) NOT NULL
        );
    """),
    "item_raridade" : ("""
        CREATE TABLE item_raridade (
        id_item_raridade integer PRIMARY KEY,
        id_item integer REFERENCES item (id_item),
        id_raridade integer
        );
    """),
    "genero" : ("""
        CREATE TABLE genero (
	    id_genero integer PRIMARY KEY,
	    nome varchar(50) NOT NULL
        );
    """),
    "jogo_genero" : ("""
        CREATE TABLE jogo_genero (
	    id_genero integer REFERENCES genero (id_genero),
	    id_jogo integer REFERENCES jogo (id_jogo),
	    PRIMARY KEY(id_genero,id_jogo)
        );
    """),
    "avaliacao" : ("""
        CREATE TABLE avaliacao (
	    id_avaliacao integer PRIMARY KEY,
	    id_jogo integer REFERENCES jogo (id_jogo),
	    id_usuario integer REFERENCES usuario (id_usuario),
	    conteudo varchar(500),
	    nota integer NOT NULL
        );
    """),
    "conquista" : ("""
        CREATE TABLE conquista (
	    id_conquista integer,
	    id_usuario integer REFERENCES usuario (id_usuario),
	    id_jogo integer REFERENCES jogo (id_jogo),
	    nome varchar(50) NOT NULL,
	    descricao varchar(50),
	    PRIMARY KEY(id_conquista, id_usuario)
        );
    """),
    "promocao" : ("""
        CREATE TABLE promocao (
	    id_promocao integer PRIMARY KEY,
	    nome varchar(50) NOT NULL UNIQUE,
	    descricao varchar(100)
        );
    """),
    "jogo_promocao" : ("""
        CREATE TABLE jogo_promocao (
        id_jogo integer REFERENCES jogo (id_jogo),
        id_promocao integer REFERENCES promocao (id_promocao),
        data_inicio timestamp NOT NULL,
        desconto numeric NOT NULL,
        data_final timestamp NOT NULL,
        PRIMARY KEY(id_jogo,id_promocao)
        );
    """),
    "midia" : ("""
        CREATE TABLE midia (
        id_midia integer PRIMARY KEY,
        id_jogo integer REFERENCES jogo (id_jogo),
        arquivo bytea NOT NULL,
        tipo varchar(25) NOT NULL
        );
    """),
    "expansao" : ("""
        CREATE TABLE expansao (
        id_expansao integer PRIMARY KEY,
        id_jogo integer REFERENCES jogo (id_jogo),
        nome varchar(100) NOT NULL,
        descricao varchar(500),
        valor numeric NOT NULL
        );
    """),
    "compra_expansao" : ("""
        CREATE TABLE compra_expansao (
        id_compra integer REFERENCES compra (id_compra),
        id_expansao integer REFERENCES expansao (id_expansao),
        data_compra timestamp NOT NULL,
        comprovante varchar(50) NOT NULL,
        PRIMARY KEY(id_compra,id_expansao)
        );
    """),
    
}










