create = {
    "usuario" : ("""
        CREATE TABLE usuario (
	    id_usuario integer PRIMARY KEY,
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
	    descricao varchar(500)
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
	    id_compra integer PRIMARY KEY,
	    id_usuario integer REFERENCES usuario (id_usuario),
	    valor numeric NOT NULL,
        comprovante varchar(50) UNIQUE
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
	    descricao varchar(500),
	    valor numeric NOT NULL,
	    data_lancamento date NOT NULL
        );
    """),
    "compra_jogo" : ("""
        CREATE TABLE compra_jogo (
        id_compra integer REFERENCES compra (id_compra),
        id_jogo integer REFERENCES jogo (id_jogo),
        data_compra timestamp NOT NULL,
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
        id_item_raridade serial PRIMARY KEY,
        id_item integer REFERENCES item (id_item) NOT NULL,
        id_raridade integer NOT NULL
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
	    id_jogo integer REFERENCES jogo (id_jogo),
        id_genero integer REFERENCES genero (id_genero),
	    PRIMARY KEY(id_genero,id_jogo)
        );
    """),
    "avaliacao" : ("""
        CREATE TABLE avaliacao (
	    id_avaliacao serial,
	    id_jogo integer REFERENCES jogo (id_jogo),
	    id_usuario integer REFERENCES usuario (id_usuario),
	    conteudo varchar(500),
	    nota integer NOT NULL,
        PRIMARY KEY(id_avaliacao, id_usuario, id_jogo)
        );
    """),
    "conquista" : ("""
        CREATE TABLE conquista (
	    id_conquista serial,
	    id_usuario integer REFERENCES usuario (id_usuario),
	    id_jogo integer REFERENCES jogo (id_jogo),
	    nome varchar(100) NOT NULL,
	    descricao varchar(100),
        liberada varchar(10),
	    PRIMARY KEY(id_conquista, id_jogo, id_usuario)
        );
    """),
    "promocao" : ("""
        CREATE TABLE promocao (
	    id_promocao integer PRIMARY KEY,
	    nome varchar(50) NOT NULL UNIQUE,
	    descricao varchar(500)
        );
    """),
    "jogo_promocao" : ("""
        CREATE TABLE jogo_promocao (
        id_jogo integer REFERENCES jogo (id_jogo),
        id_promocao integer REFERENCES promocao (id_promocao),
        data_inicio timestamp NOT NULL,
        data_final timestamp NOT NULL,
        desconto numeric NOT NULL,
        PRIMARY KEY(id_jogo,id_promocao)
        );
    """),
    "midia" : ("""
        CREATE TABLE midia (
        id_midia serial PRIMARY KEY,
        id_jogo integer REFERENCES jogo (id_jogo),
        tipo varchar(25) NOT NULL,
        link varchar(50)
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
        PRIMARY KEY(id_compra,id_expansao)
        );
    """),
}










