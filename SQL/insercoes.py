insercao = {
    "usuario" : ("""
        INSERT INTO usuario VALUES (default, 'AkeleMito', 'gabrieljulianigj@gmail.com', 'senhasegura1', 'Gabriel Segatto', 'Aquele Mesmo', 5);
        INSERT INTO usuario VALUES (default, 'DenteDeSabio', 'desntedesabio@gmail.com', 'senhasegura2', 'Jonathan Maciel do Santos', 'O maior jogadorde vava do sudeste do meu bairro', 2);
        INSERT INTO usuario VALUES (default, 'BoloFofo', 'nicolasgiaboeski@gmail.com', 'senhasegura3', 'Nicolas Giaboeski', 'widepeepoHappy', 33);
        INSERT INTO usuario VALUES (default, 'BotafoguenseTriste', 'bota.fogo.triste@gmail.com', 'senhasegura4', 'Fabrício Acevedo', NULL, 456);
        INSERT INTO usuario VALUES (default, 'TheArmyBR', 'joseph.ed@gmail.com', 'senhasegura5', 'José Edvaldo', 'A seven nations army couldnt hold me back!', 20);
        INSERT INTO usuario VALUES (default, 'bergamotaPotente17', 'gauderiodasberga@gmailcom', 'senhasegura6', 'BUTIA DOS BOLSO', 'come berga faz bem pra saude', 3);
        INSERT INTO usuario VALUES (default, 'ORO', 'Arthurgolden@gmail.com', 'senhasegura7', 'Arthur Deleao', 'Parceria sempre', 2);
        INSERT INTO usuario VALUES (default, 'bergod1', 'berzinho.god@ibest.com.br', 'senhasegura8', 'Bernardo Silver', 'Pro player de LOL', 20);
        INSERT INTO usuario VALUES (default, 'Pillar', 'eduardo.henrique@gmail.com', 'senhasegura9', 'Eduardo Henrique Tche', '', 11);
        INSERT INTO usuario VALUES (default, 'Shockwavex', 'shock.wave.x@gmail.com', 'senhasegura10', 'Guilherme Senn', 'Player recluso de dota e bdo', 11);         
    """),
    "raridade" : ("""
        INSERT INTO raridade VALUES (default, 'Comum');
        INSERT INTO raridade VALUES (default, 'Incomum');
        INSERT INTO raridade VALUES (default, 'Raro');
        INSERT INTO raridade VALUES (default, 'Épico');
        INSERT INTO raridade VALUES (default, 'Mítico');
        INSERT INTO raridade VALUES (default, 'Nomeado');
        INSERT INTO raridade VALUES (default, 'Único');
    """),
    "genero" : ("""
        INSERT INTO genero VALUES (100, 'Ação e Aventura');
        INSERT INTO genero VALUES (101, 'RPGs de Aventura');
        INSERT INTO genero VALUES (102, 'RPGs em Turnos');
        INSERT INTO genero VALUES (103, 'Hack and Slash');
        INSERT INTO genero VALUES (104, 'Luta e Artes Marciais');
        INSERT INTO genero VALUES (105, 'Roguelike');
        INSERT INTO genero VALUES (200, 'Tiro em Primeira Pessoa (FPS)');
        INSERT INTO genero VALUES (201, 'Tiro em Terceira Pessoa');
        INSERT INTO genero VALUES (202, 'Shoot em Up');
        INSERT INTO genero VALUES (203, 'Militar');
        INSERT INTO genero VALUES (300, 'Estratégia');
        INSERT INTO genero VALUES (301, 'Cidades e Colônias');
        INSERT INTO genero VALUES (302, 'Defesa de Torres');
        INSERT INTO genero VALUES (303, 'Estratégia Baseada em Turnos');
        INSERT INTO genero VALUES (304, 'Estratégia em Tempo Real (RTS)');
        INSERT INTO genero VALUES (305, 'Grande Estratégia e 4X');
        INSERT INTO genero VALUES (306, 'Construção e Automação');
        INSERT INTO genero VALUES (400, 'Simulação');
        INSERT INTO genero VALUES (401, 'Vida e Imersivos');
        INSERT INTO genero VALUES (402, 'Simuladores Automobilísticos');
        INSERT INTO genero VALUES (403, 'Simuladores de Esporte');
        INSERT INTO genero VALUES (404, 'Simuladores de Física');
        INSERT INTO genero VALUES (404, 'Empregos e Passatempo');
        INSERT INTO genero VALUES (500, 'Esportes');
        INSERT INTO genero VALUES (501, 'Corrida');
        INSERT INTO genero VALUES (502, 'Esporte em Equipe');
        INSERT INTO genero VALUES (503, 'Esportes Individuais');
        INSERT INTO genero VALUES (504, 'Pescaria e Caça');
        INSERT INTO genero VALUES (505, 'Futebol');
        INSERT INTO genero VALUES (506, 'Basquete');
        INSERT INTO genero VALUES (600, 'Romance Visual');
        INSERT INTO genero VALUES (601, 'Trama Excepcional');
        INSERT INTO genero VALUES (602, 'Encontros');
    """),
    "desenvolvedor" : ("""
        INSERT INTO desenvolvedor VALUES (default, 'NCSOFT', 'A NCSoft Corporation é uma desenvolvedora e publicadora sul-coreana de jogos eletrônicos sediada em Seongnam, Região Metropolitana de Seul. Foi fundada em março de 1997 por Taek Jin Kim e é a empresa responsável por títulos como Lineage, Guild Wars e Blade & Soul.');
        INSERT INTO desenvolvedor VALUES (default, 'Obsidian Entertainment', 'Obsidian Entertainment é uma desenvolvedora de jogos eletrônicos americana fundada em 2003 após a desativação da Black Isle Studios, desenvolvedora da Interplay Entertainment.');
        INSERT INTO desenvolvedor VALUES (default, 'Amazon Games', 'Amazon Game Studios é um estúdio de desenvolvedor de jogos eletrônicos, pertencente à Amazon.com.');
        INSERT INTO desenvolvedor VALUES (default, 'Devolver', 'A Devolver Digital Inc. é uma publicadora de jogos eletrônicos estadunidense sediada em Austin, Texas, se especializando na publicação de jogos independentes.');
        INSERT INTO desenvolvedor VALUES (default, 'EA', 'Eletronic Arts Inc. é uma empresa de jogos eletrônicos sediada em Redwood City, Califórnia. Fundada em maio de 1982 por Trip Hawkins.');
        INSERT INTO desenvolvedor VALUES (default, 'Blizzard', 'Blizzard Entertainment é uma editora e desenvolvedora de videojogos americana tendo sua sede na cidade de Irvine, California. A companhia é uma subsidiária da Activision Blizzard e foi fundada em 8 de fevereiro de 1991.');
        INSERT INTO desenvolvedor VALUES (default, 'Nintendo', 'A Nintendo Co., Ltd. é uma desenvolvedora e publicadora japonesa de jogos eletrônicos e consoles sediada em Quioto.');
        INSERT INTO desenvolvedor VALUES (default, 'Ubisoft', 'Ubisoft Entertainment é uma empresa francesa de jogos eletrônicos com sede no subúrbio de Montreuil, em Paris, com vários estúdios de desenvolvimento em todo o mundo.');
        INSERT INTO desenvolvedor VALUES (default, 'Rockstar Games', 'Rockstar Games, Inc. é uma produtora e publicadora de jogos eletrônicos fundada em 1994. Conhecida por ter criado grandes nomes dos jogos eletrônicos, a Rockstar é criadora das famosas séries Grand Theft Auto, Red Dead, Midnight Club, Bully, Max Payne e Manhunt.');
        INSERT INTO desenvolvedor VALUES (default, 'Square Enix', 'A Square Enix Holdings Co., Ltd. é uma desenvolvedora e publicadora japonesa de jogos eletrônicos sediada em Tóquio. Ela é mais conhecida por suas franquias de RPGs eletrônicos, que incluem Final Fantasy, Dragon Quest e Kingdom Hearts.');
        INSERT INTO desenvolvedor VALUES (default, 'Kojima Productions', 'A Kojima Productions Co., Ltd. é um estúdio japonês de desenvolvimento de videojogos, fundado por Hideo Kojima, criador da popular série Metal Gear.');
        INSERT INTO desenvolvedor VALUES (default, 'CD Projekt Red', 'A CD Projekt S.A. é uma desenvolvedora e publicadora de jogos eletrônicos polonesa sediada em Varsóvia, Mazóvia. A companhia foi fundada em maio de 1994 por Marcin Iwiński e Michał Kiciński.');
        INSERT INTO desenvolvedor VALUES (default, 'Valve Corporation', 'Valve Corporation é uma empresa norte-americana desenvolvedora de jogos eletrônicos e de distribuição digital, com sede em Bellevue, Washington, Estados Unidos.');
        INSERT INTO desenvolvedor VALUES (default, 'Guerrilla Games', 'A Guerrilla B.V. é uma desenvolvedora holandesa de jogos eletrônicos sediada em Amsterdã. Era originalmente uma subsidiária da Lost Boys e depois da Media Republic, sendo atualmente propriedade da Sony Interactive Entertainment. A companhia foi fundada em 2000 depois da fusão entre a Orange Games e a Digital Infinity.');
        INSERT INTO desenvolvedor VALUES (default, 'BioWare', 'A BioWare é uma desenvolvedora canadense de jogos eletrônicos sediada em Edmonton, Alberta. Foi fundada em fevereiro de 1995 por Ray Muzyka, Greg Zeschuk, Trent Oster, Brent Oster, Marcel Zeschuk e Augustine Yip, sendo desde 2007 uma subsidiária da Electronic Arts.');
        INSERT INTO desenvolvedor VALUES (default, 'Riot Games', 'A Riot Games, Inc. é uma desenvolvedora, editora e organizadora de torneios de esportes eletrônicos americana com sede em West Los Angeles, Califórnia.');
        INSERT INTO desenvolvedor VALUES (default, 'Naughty Dog', 'A Naughty Dog, LLC é uma desenvolvedora norte-americana de jogos eletrônicos sediada em Santa Mônica, Califórnia. Foi fundada em setembro de 1984 pelos então estudantes colegiais Andy Gavin e Jason Rubin como JAM Software, sendo renomeada para seu nome atual alguns anos depois em 1989.');
        INSERT INTO desenvolvedor VALUES (default, 'Tencent Games', 'A Tencent investiu em uma série de editoras e desenvolvedores de jogos não chineses, variando de ações minoritárias ao controle total da empresa. Por meio desses investimentos, em março de 2018 a Tencent foi considerada a maior empresa de videogame do mundo. Entre seus investimentos conhecidos incluem: Epic Games, Garena, Riot, Baidu, BlueStacks, Alibaba Group, SuperCell etc.');
        INSERT INTO desenvolvedor VALUES (default, 'Supercell', 'Supercell é uma desenvolvedora finlandesa de jogos eletrônicos para dispositivos móveis fundada em maio de 2010 por Ilkka Paananen.');
        INSERT INTO desenvolvedor VALUES (default, 'Epic Games', 'A Epic Games, Inc., anteriormente chamada de Potomac Computer Systems e Epic MegaGames, é uma desenvolvedora norte-americana de jogos eletrônicos e softwares sediada em Cary, Carolina do Norte. Foi fundada em 1991 por Tim Sweeney e originalmente ficava localizada na cidade de Potomac em Maryland.');
        INSERT INTO desenvolvedor VALUES (default, 'Capcom', 'Capcom Co., Ltd. é uma desenvolvedora e publicadora japonesa de jogos eletrônicos sediada em Osaka. Ela é conhecida por ter criado franquias multimilionárias, tais como Resident Evil, Street Fighter, Mega Man, Devil May Cry, Dino Crisis e Onimusha. Sua sede principal está situada em Chuo-ku, Osaka.');
    """),
    "jogo" : ("""
        INSERT INTO jogo VALUES (default, 1, 'THRONE AND LIBERTY', 'Bem-vindos ao THRONE AND LIBERTY, um MMORPG multiplataforma gratuito. Em um ambiente em contínua mudança e PvPvE em escala massiva, você tem a habilidade de se transformar em criaturas que lutam por terra, mar e ar.', 0, '2023-12-07');
        INSERT INTO jogo VALUES (default, 2, 'Grounded', 'The world is a vast, beautiful and dangerous place – especially when you have been shrunk to the size of an ant. Can you thrive alongside the hordes of giant insects, fighting to survive the perils of the backyard?', 199,00, '2022-09-27');
        INSERT INTO jogo VALUES (default, 3, 'New World', 'Explore um MMO de mundo aberto emocionante e cheio de perigos e oportunidades, onde você irá forjar um novo destino na ilha sobrenatural de Aeternum.', 201,99, '2021-09-28');
        INSERT INTO jogo VALUES (default, 4, 'Inscryption', 'Inscryption é uma sombria odisseia pavimentada por cartas que mescla roguelike de construção de baralhos, quebra-cabeças no estilo de "escape rooms" e horror psicológico para criar uma amálgama sanguinolenta. Ainda mais obscuros são os segredos das cartas...', 49,99, '2021-10-19');
        INSERT INTO jogo VALUES (default, 5, 'EA SPORTS FC™ 24', 'O EA SPORTS FC™ 24 traz o Jogo de Todo Mundo: a experiência mais realista de futebol com o HyperMotionV, PlayStyles otimizada pela Opta, e uma Frostbite™ Engine melhorada.', 359,00, '2023-09-29');
        INSERT INTO jogo VALUES (default, 6, 'Overwatch', 'Overwatch® 2 é um jogo de tiro em equipe aclamado pela crítica, ambientado em um futuro otimista com um elenco crescente de heróis. Jogue com seus amigos e entre agora mesmo!', 0, '2022-10-04');
        INSERT INTO jogo VALUES (default, 7, 'Mario Kart™ 8 Deluxe', 'Queime o asfalto nas pistas do Reino Cogumelo! Debaixo d'água, no céu, no espaço ou de cabeça para baixo a caminho da vitória! Acelere no modo multijogador local*, em torneios online**, no modo de batalha renovado e muito mais!', 299.00, '2017-04-28');
        INSERT INTO jogo VALUES (default, 8, 'Watch_Dogs™', 'In today's hyper-connected world, Chicago operates under ctOS, the most advanced computer network in America.', 89.99, '2015-05-16');
        INSERT INTO jogo VALUES (default, 9, 'Grand Theft Auto V', 'Grand Theft Auto V para PC oferece aos jogadores a opção de explorar o gigantesco e premiado mundo de Los Santos e Blaine County em resoluções de até 4K e além, assim como a chance de experimentar o jogo rodando a 60 FPS (quadros por segundo).', 90.99, '2013-09-17');
        INSERT INTO jogo VALUES (default, 10, 'FINAL FANTASY VII REMAKE INTERGRADE', 'Cloud Strife, ex-agente da SOLDIER, chega a Midgar, a cidade movida a energia de mako. O clássico atemporal FINAL FANTASY VII renasceu, com gráficos de última geração, um novo sistema de combate e uma aventura adicional com Yuffie Kisaragi.', 349,90, '2022-06-17');
        INSERT INTO jogo VALUES (default, 11, 'DEATH STRANDING DIRECTORS CUT', 'Do lendário criador de jogos Hideo Kojima, surge uma experiência totalmente inédita que desafia o gênero. Sam Bridges precisa enfrentar um mundo profundamente transformado pelo Death Stranding. Carregando os restos desconectados do nosso futuro em suas mãos, ele embarca em uma jornada para reconectar o mundo destruído.', 159.00, '2022-03-30');
        INSERT INTO jogo VALUES (default, 12, 'The Witcher® 3: Wild Hunt', 'The Witcher 3: Wild Hunt é um jogo eletrônico de RPG de ação em mundo aberto desenvolvido pela CD Projekt RED e lançado no dia 19 de maio de 2015 para as plataformas Microsoft Windows, PlayStation 4, Xbox One e em outubro de 2019 para o Nintendo Switch, sendo o terceiro título da série de jogos The Witcher. ', 129.99, '2015-05-18');
        INSERT INTO jogo VALUES (default, 13, 'Half-Life 2', 'Half-Life 2 (estilizado como HλLF-LIFE2) é um jogo de tiro em primeira pessoa, lançado em 2004 pela Valve Corporation. Trazendo diversas inovações para o campo dos games, Half-Life 2 logo se tornou um enorme sucesso de vendas e de crítica, ganhando vários prêmios importantes e sendo inclusive amplamente aclamado como o "Jogo do Ano" e, posteriormente, como o "Jogo da Década".', 32.99, '2004-11-16');
        INSERT INTO jogo VALUES (default, 14, 'Horizon Forbidden West', 'Horizon Forbidden West é um jogo eletrônico de RPG de ação desenvolvido pela Guerrilla Games e publicado pela Sony Interactive Entertainment.', 299.90, '2022-02-18');
        INSERT INTO jogo VALUES (default, 15, 'Anthem', 'Anthem é um jogo eletrônico de RPG de ação multijogador desenvolvido pela BioWare e publicado pela Electronic Arts.', 44, '2022-02-19');
        INSERT INTO jogo VALUES (default, 16, 'League of Legends', 'League of Legends é um jogo eletrônico do gênero multiplayer online battle arena desenvolvido e publicado pela Riot Games. Foi lançado em outubro de 2009 para Microsoft Windows e em março de 2013 para macOS.', 0, '2009-10-27');
        INSERT INTO jogo VALUES (default, 17, 'Crash Bandicoot™ N. Sane Trilogy', 'Crash Bandicoot é uma franquia de jogos eletrônicos desenvolvida originalmente pela Naughty Dog para o console PlayStation. A série passou por várias desenvolvedoras e foi publicada em diversas plataformas posteriormente. Os jogos são do gênero plataforma com diversos spin-offs do gênero corrida e em grupo.', 150, '2017-06-30');
        INSERT INTO jogo VALUES (default, 18, 'PUBG Mobile', 'PUBG Mobile é um videogame Battle Royale gratuito desenvolvido pela LightSpeed e Quantum Studio, uma divisão da Tencent Games. É uma adaptação de jogo para celular de PUBG: Battlegrounds.', 0, '2017-03-19');
        INSERT INTO jogo VALUES (default, 19, 'Clash Royale', 'Clash Royale é um videojogo de estratégia freemium Também conhecido como o melhor jogo manual do mundo, desenvolvido e publicado pela Supercell, empresa sediada em Helsinki, na Finlândia.', 0, '2016-03-02');
        INSERT INTO jogo VALUES (default, 20, 'Fortnite', 'Fortnite é um jogo eletrônico multijogador online revelado originalmente em 2011, desenvolvido pela Epic Games e lançado como diferentes modos de jogo que compartilham a mesma jogabilidade e motor gráfico de jogo.', 0, '2017-07-21');
        INSERT INTO jogo VALUES (default, 21, 'Resident Evil 3', 'Resident Evil 3, chamado no Japão de Biohazard RE:3, é um jogo eletrônico de survival horror desenvolvido e publicado pela Capcom.', 139.90, '2020-04-03');
    """),
}
