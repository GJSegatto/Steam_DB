from Imagens import Imagens

insercao = {
    "usuario" : ("""
        INSERT INTO usuario VALUES (50001, 'AkeleMito', 'gabrieljulianigj@gmail.com', 'senhasegura1', 'Gabriel Segatto', 'Aquele Mesmo', 5);
        INSERT INTO usuario VALUES (50002, 'DenteDeSabio', 'desntedesabio@gmail.com', 'senhasegura2', 'Jonathan Maciel do Santos', 'O maior jogadorde vava do sudeste do meu bairro', 2);
        INSERT INTO usuario VALUES (50003, 'BoloFofo', 'nicolasgiaboeski@gmail.com', 'senhasegura3', 'Nicolas Giaboeski', 'widepeepoHappy', 33);
        INSERT INTO usuario VALUES (50004, 'BotafoguenseTriste', 'bota.fogo.triste@gmail.com', 'senhasegura4', 'Fabrício Acevedo', NULL, 456);
        INSERT INTO usuario VALUES (50005, 'TheArmyBR', 'joseph.ed@gmail.com', 'senhasegura5', 'José Edvaldo', 'A seven nations army couldnt hold me back!', 20);
        INSERT INTO usuario VALUES (50006, 'bergamotaPotente17', 'gauderiodasberga@gmailcom', 'senhasegura6', 'BUTIA DOS BOLSO', 'come berga faz bem pra saude', 3);
        INSERT INTO usuario VALUES (50007, 'ORO', 'Arthurgolden@gmail.com', 'senhasegura7', 'Arthur Deleao', 'Parceria sempre', 2);
        INSERT INTO usuario VALUES (50008, 'bergod1', 'berzinho.god@ibest.com.br', 'senhasegura8', 'Bernardo Silver', 'Pro player de LOL', 20);
        INSERT INTO usuario VALUES (50009, 'Pillar', 'eduardo.henrique@gmail.com', 'senhasegura9', 'Eduardo Henrique Tche', '', 11);
        INSERT INTO usuario VALUES (50010, 'Shockwavex', 'shock.wave.x@gmail.com', 'senhasegura10', 'Guilherme Senn', 'Player recluso de dota e bdo', 11);         
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
        INSERT INTO genero VALUES (405, 'Empregos e Passatempo');
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
        INSERT INTO jogo VALUES (1001, 1, 'THRONE AND LIBERTY', 'Bem-vindos ao THRONE AND LIBERTY, um MMORPG multiplataforma gratuito. Em um ambiente em contínua mudança e PvPvE em escala massiva, você tem a habilidade de se transformar em criaturas que lutam por terra, mar e ar.', 0, '2023-12-07');
        INSERT INTO jogo VALUES (1002, 2, 'Grounded', 'The world is a vast, beautiful and dangerous place – especially when you have been shrunk to the size of an ant. Can you thrive alongside the hordes of giant insects, fighting to survive the perils of the backyard?', 199.00, '2022-09-27');
        INSERT INTO jogo VALUES (1003, 3, 'New World', 'Explore um MMO de mundo aberto emocionante e cheio de perigos e oportunidades, onde você irá forjar um novo destino na ilha sobrenatural de Aeternum.', 201.99, '2021-09-28');
        INSERT INTO jogo VALUES (1004, 4, 'Inscryption', 'Inscryption é uma sombria odisseia pavimentada por cartas que mescla roguelike de construção de baralhos, quebra-cabeças no estilo de "escape rooms" e horror psicológico para criar uma amálgama sanguinolenta. Ainda mais obscuros são os segredos das cartas...', 49.99, '2021-10-19');
        INSERT INTO jogo VALUES (1005, 5, 'EA SPORTS FC™ 24', 'O EA SPORTS FC™ 24 traz o Jogo de Todo Mundo: a experiência mais realista de futebol com o HyperMotionV, PlayStyles otimizada pela Opta, e uma Frostbite™ Engine melhorada.', 359.00, '2023-09-29');
        INSERT INTO jogo VALUES (1006, 6, 'Overwatch', 'Overwatch® 2 é um jogo de tiro em equipe aclamado pela crítica, ambientado em um futuro otimista com um elenco crescente de heróis. Jogue com seus amigos e entre agora mesmo!', 0, '2022-10-04');
        INSERT INTO jogo VALUES (1007, 7, 'Mario Kart™ 8 Deluxe', 'Queime o asfalto nas pistas do Reino Cogumelo! Debaixo da água, no céu, no espaço ou de cabeça para baixo a caminho da vitória! Acelere no modo multijogador local*, em torneios online**, no modo de batalha renovado e muito mais!', 299.00, '2017-04-28');
        INSERT INTO jogo VALUES (1008, 8, 'Watch_Dogs™', 'In todays hyper-connected world, Chicago operates under ctOS, the most advanced computer network in America.', 89.99, '2015-05-16');
        INSERT INTO jogo VALUES (1009, 9, 'Grand Theft Auto V', 'Grand Theft Auto V para PC oferece aos jogadores a opção de explorar o gigantesco e premiado mundo de Los Santos e Blaine County em resoluções de até 4K e além, assim como a chance de experimentar o jogo rodando a 60 FPS (quadros por segundo).', 90.99, '2013-09-17');
        INSERT INTO jogo VALUES (1010, 10, 'FINAL FANTASY VII REMAKE INTERGRADE', 'Cloud Strife, ex-agente da SOLDIER, chega a Midgar, a cidade movida a energia de mako. O clássico atemporal FINAL FANTASY VII renasceu, com gráficos de última geração, um novo sistema de combate e uma aventura adicional com Yuffie Kisaragi.', 349.90, '2022-06-17');
        INSERT INTO jogo VALUES (1011, 11, 'DEATH STRANDING DIRECTORS CUT', 'Do lendário criador de jogos Hideo Kojima, surge uma experiência totalmente inédita que desafia o gênero. Sam Bridges precisa enfrentar um mundo profundamente transformado pelo Death Stranding. Carregando os restos desconectados do nosso futuro em suas mãos, ele embarca em uma jornada para reconectar o mundo destruído.', 159.00, '2022-03-30');
        INSERT INTO jogo VALUES (1012, 12, 'The Witcher® 3: Wild Hunt', 'The Witcher 3: Wild Hunt é um jogo eletrônico de RPG de ação em mundo aberto desenvolvido pela CD Projekt RED e lançado no dia 19 de maio de 2015 para as plataformas Microsoft Windows, PlayStation 4, Xbox One e em outubro de 2019 para o Nintendo Switch, sendo o terceiro título da série de jogos The Witcher. ', 129.99, '2015-05-18');
        INSERT INTO jogo VALUES (1013, 13, 'Half-Life 2', 'Half-Life 2 (estilizado como HλLF-LIFE2) é um jogo de tiro em primeira pessoa, lançado em 2004 pela Valve Corporation. Trazendo diversas inovações para o campo dos games, Half-Life 2 logo se tornou um enorme sucesso de vendas e de crítica, ganhando vários prêmios importantes e sendo inclusive amplamente aclamado como o "Jogo do Ano" e, posteriormente, como o "Jogo da Década".', 32.99, '2004-11-16');
        INSERT INTO jogo VALUES (1014, 14, 'Horizon Forbidden West', 'Horizon Forbidden West é um jogo eletrônico de RPG de ação desenvolvido pela Guerrilla Games e publicado pela Sony Interactive Entertainment.', 299.90, '2022-02-18');
        INSERT INTO jogo VALUES (1015, 15, 'Anthem', 'Anthem é um jogo eletrônico de RPG de ação multijogador desenvolvido pela BioWare e publicado pela Electronic Arts.', 44, '2022-02-19');
        INSERT INTO jogo VALUES (1016, 16, 'League of Legends', 'League of Legends é um jogo eletrônico do gênero multiplayer online battle arena desenvolvido e publicado pela Riot Games. Foi lançado em outubro de 2009 para Microsoft Windows e em março de 2013 para macOS.', 0, '2009-10-27');
        INSERT INTO jogo VALUES (1017, 17, 'Crash Bandicoot™ N. Sane Trilogy', 'Crash Bandicoot é uma franquia de jogos eletrônicos desenvolvida originalmente pela Naughty Dog para o console PlayStation. A série passou por várias desenvolvedoras e foi publicada em diversas plataformas posteriormente. Os jogos são do gênero plataforma com diversos spin-offs do gênero corrida e em grupo.', 150, '2017-06-30');
        INSERT INTO jogo VALUES (1018, 18, 'PUBG Mobile', 'PUBG Mobile é um videogame Battle Royale gratuito desenvolvido pela LightSpeed e Quantum Studio, uma divisão da Tencent Games. É uma adaptação de jogo para celular de PUBG: Battlegrounds.', 0, '2017-03-19');
        INSERT INTO jogo VALUES (1019, 19, 'Clash Royale', 'Clash Royale é um videojogo de estratégia freemium Também conhecido como o melhor jogo manual do mundo, desenvolvido e publicado pela Supercell, empresa sediada em Helsinki, na Finlândia.', 0, '2016-03-02');
        INSERT INTO jogo VALUES (1020, 20, 'Fortnite', 'Fortnite é um jogo eletrônico multijogador online revelado originalmente em 2011, desenvolvido pela Epic Games e lançado como diferentes modos de jogo que compartilham a mesma jogabilidade e motor gráfico de jogo.', 0, '2017-07-21');
        INSERT INTO jogo VALUES (1021, 21, 'Resident Evil 3', 'Resident Evil 3, chamado no Japão de Biohazard RE:3, é um jogo eletrônico de survival horror desenvolvido e publicado pela Capcom.', 139.90, '2020-04-03');
    """),
    "promocao" : ("""
        INSERT INTO promocao VALUES (default, 'Summer Sale', 'Chegou o Verão!!! Confira os mais diversos jogos nessa super promoção.');
        INSERT INTO promocao VALUES (default, 'Halloween', 'Doces ou Desconturas? Aposto que você vai querer conferir os nossos preços baixíssimos nos seus jogos preferidos.');
        INSERT INTO promocao VALUES (default, 'Férias de Inverno', 'FSHHHH!! É o vento do inverno levando a temperatura e os preços lá em baixo');
        INSERT INTO promocao VALUES (default, 'Natal', 'HO HO HO! Papai Noel chegou e trouxe MUUITAS promoções pra você que foi um bom garoto durante o  ano, ou nem tanto...');
        INSERT INTO promocao VALUES (default, 'Ano Novo Chinês', '888, A sorte é sua, os preços dos jogos desenvolvidos pelas empresas de origem chinesa estão em promoção!!!');
        INSERT INTO promocao VALUES (default, 'Promoção de Fim de Semana', 'Relaxe no Fim de Semana com aquele jogo que você estava de olho!');
        INSERT INTO promocao VALUES (default, 'Páscoa', 'A época é de chocolate e de GAMES. Aproveite a Páscoa para curtir os melhores jogos pelo melhor preço!');
        INSERT INTO promocao VALUES (default, 'Aniversário da Plataforma', 'Comemore o aniversário da plataforma, e quem recebe os presentes é você, que nos faz melhores a cada ano!');
    """),
    "expansao" : ("""
        INSERT INTO expansao VALUES (default, 1009, 'Grand Theft Auto V - Criminal Enterprise Starter Pack', 'Requer Grand Theft Auto V no Steamzera para ser acessado.', 18.9);
        INSERT INTO expansao VALUES (default, 1002, 'Grounded (Original Soundtrack)', 'The Grounded Official Soundtrack contains 34 tracks from Year 1 and Year 2 of the games Early Access development period, combined Track files are in WAV format, 44.1 kHz, 16-bit depth.', 20.69);
        INSERT INTO expansao VALUES (default, 1012, 'The Witcher 3: Wild Hunt - Hearts of Stone', 'Requer The Witcher® 3: Wild Hunt no Steamzera para ser acessado.', 29.99);
        INSERT INTO expansao VALUES (default, 1003, 'New World: Rise of the Angry Earth', 'Uma nova ameaça paira sobre terras até então familiares. Empunhe uma nova arma, descubra uma nova habilidade e faça novos aliados na forma de montarias para lutar contra um risco crescente que ameaça aniquilar Aeternum!', 88.99);
        INSERT INTO expansao VALUES (default, 1012, 'The Witcher 3: Wild Hunt Soundtrack', 'Conteúdo adicional para The Witcher® 3: Wild Hunt. Não inclui o jogo.', 22.79);
        INSERT INTO expansao VALUES (default, 1011, 'DEATH STRANDING Digital Artbook', 'Requer DEATH STRANDING DIRECTORS CUT no Steam para ser acessado.', 0);
        INSERT INTO expansao VALUES (default, 1006, 'Overwatch® 2 - Oferta Invasão', 'Requer Overwatch® 2 no Steam para ser acessado.', 69);
        INSERT INTO expansao VALUES (default, 1006, 'Overwatch® 2 - 5.000 Moedas de Overwatch (+2.500 de bônus)', 'Requer Overwatch® 2 no Steam para ser acessado.', 230);
        INSERT INTO expansao VALUES (default, 1016, 'League of Legends - 400 Riot Points', 'Receba 400 Riot Points', 10.90);
        INSERT INTO expansao VALUES (default, 1016, 'League of Legends - 1380 Riot Points', 'Receba 1275 + 105 Riot Points.', 34.90);
        INSERT INTO expansao VALUES (default, 1016, 'League of Legends - 2800 Riot Points', 'Receba 2575 + 225 Riot Points.', 69.90);
        INSERT INTO expansao VALUES (default, 1016, 'League of Legends - 5075 Riot Points', 'Receba 4575 + 500 Riot Points.', 124.90);
        INSERT INTO expansao VALUES (default, 1016, 'League of Legends - 7200 Riot Points', 'Receba 6425 + 775 Riot Points.', 174.90);
        INSERT INTO expansao VALUES (default, 1016, 'League of Legends - 15000 Riot Points', 'Receba 12850 + 2150 Riot Points.', 349.90);
        INSERT INTO expansao VALUES (default, 1021, 'Resident Evil 3 Special Soundtrack', 'Conteúdo adicional para Resident Evil 3. Não inclui o jogo.', 56.99);
        INSERT INTO expansao VALUES (default, 1007, 'Mario Kart™ 8 Deluxe – Passe de pistas adicionais', 'Corra em mais pistas e obtenha mais opções de personagens com o conteúdo extra da licença Mario Kart™ 8 Deluxe – Passe de pistas adicionais', 128);
    """),
    "item" : ("""
        INSERT INTO item VALUES (default, 50009, 1002, 'Skin/Roupa', NULL, 'Roupa Florida de Primavera');
        INSERT INTO item VALUES (default, 50003, 1002, 'Skin/Arma', NULL, 'Bastão do Esqueleto Imperador');
        INSERT INTO item VALUES (default, 50001, 1002, 'Skin/Roupa', NULL, 'Roupa de Praia');
        INSERT INTO item VALUES (default, 50002, 1002, 'Skin/Conjunto', NULL, 'Conjunto Tabuleiro e Cartas Natalinas');
        INSERT INTO item VALUES (default, 50002, 1004, 'Skin/Conjunto', NULL, 'Conjunto Tabuleiro e Cartas Halloween');
        INSERT INTO item VALUES (default, 50002, 1002, 'Skin/Conjunto', NULL, 'Conjunto Tabuleiro e Cartas Carnaval');
        INSERT INTO item VALUES (default, 50001, 1006, 'Skin/Conjunto', NULL, 'Cassidy Van Helsin');
        INSERT INTO item VALUES (default, 50001, 1006, 'Skin/Conjunto', NULL, 'Cassidy Chapéu Branco');
        INSERT INTO item VALUES (default, 50008, 1006, 'Skin/Conjunto', NULL, 'Brigitte SÓL');
        INSERT INTO item VALUES (default, 50010, 1006, 'Skin/Conjunto', NULL, 'Brigitte Caçadora de Vampiros');
        INSERT INTO item VALUES (default, 50010, 1006, 'Skin/Conjunto', NULL, 'Illari Corvo Noturno');
        INSERT INTO item VALUES (default, 50010, 1006, 'Skin/Conjunto', NULL, 'Ramattra Monge Peregrino');
        INSERT INTO item VALUES (default, 50001, 1006, 'Skin/Conjunto', NULL, 'Ashe Chapeuzinho Vermelho');
        INSERT INTO item VALUES (default, 50004, 1006, 'Skin/Conjunto', NULL, 'Ashe Encantadora de Serpentes');
        INSERT INTO item VALUES (default, 50004, 1006, 'Skin/Conjunto', NULL, 'Roadhog Tóxico');
        INSERT INTO item VALUES (default, 50006, 1006, 'Skin/Conjunto', NULL, 'Ana Polar');
        INSERT INTO item VALUES (default, 50007, 1006, 'Skin/Conjunto', NULL, 'Ana Guardiã Espiritual');
        INSERT INTO item VALUES (default, 50001, 1006, 'Skin/Conjunto', NULL, 'Winston Lobisgorila');
        INSERT INTO item VALUES (default, 50008, 1016, 'Skin/Conjunto', 'Adquirido em 04/11/2023', 'THRESH IMPERADOR LUNAR');
        INSERT INTO item VALUES (default, 50008, 1016, 'Skin/Conjunto', 'Adquirido em 02/04/2023', 'TRYNDAMERE ESPADA DEMONÍACA');
        INSERT INTO item VALUES (default, 50008, 1016, 'Skin/Conjunto', 'Adquirido em 09/02/2023', 'NIDALEE CAÇADORA CÓSMICA');
        INSERT INTO item VALUES (default, 50005, 1016, 'Skin/Conjunto', 'Adquirido em 31/05/2022', 'NAMI DESTINO CÓSMICO');
        INSERT INTO item VALUES (default, 50002, 1016, 'Skin/Conjunto', 'Adquirido em 30/12/2021', 'PYKE SENTINELA');
        INSERT INTO item VALUES (default, 50005, 1016, 'Skin/Conjunto', 'Adquirido em 30/11/2021', 'POPPY HEXTEC');
        INSERT INTO item VALUES (default, 50002, 1016, 'Skin/Conjunto', 'Adquirido em 09/12/2021', 'PANTHEON ASCENDENTE DE PRESTÍGIO');
        INSERT INTO item VALUES (default, 50005, 1016, 'Skin/Conjunto', 'Adquirido em 23/09/2021', 'LEE SIN DRAGÃO DA TORMENTA');
        INSERT INTO item VALUES (default, 50005, 1016, 'Skin/Conjunto', 'Adquirido em 04/02/2021', 'SKARNER MÁQUINA DE COMBATE ALFA');
        INSERT INTO item VALUES (default, 50010, 1016, 'Skin/Conjunto', 'Adquirido em 12/12/2020', 'TRISTANA TREINADORA DE DRAGÕES');
        INSERT INTO item VALUES (default, 50010, 1016, 'Skin/Conjunto', 'Adquirido em 21/08/2020', 'MORGANA CONGREGAÇÃO DAS BRUXAS');
        INSERT INTO item VALUES (default, 50001, 1016, 'Skin/Conjunto', 'Adquirido em 22/01/2017', 'POPPY BONECA DE PANO');
        INSERT INTO item VALUES (default, 50007, 1016, 'Skin/Conjunto', 'Adquirido em 26/10/2019', 'XAYAH GUARDIÃ ESTELAR');
        INSERT INTO item VALUES (default, 50003, 1018, 'Skin/Arma', NULL, 'Gold Plate - S12K');
        INSERT INTO item VALUES (default, 50003, 1018, 'Skin/Arma', NULL, 'Tick Tock - M416');
        INSERT INTO item VALUES (default, 50003, 1018, 'Skin/Arma', NULL, 'Gold Plate - Groza');
        INSERT INTO item VALUES (default, 50003, 1018, 'Skin/Arma', NULL, 'Silver Plave - UMP45');
        INSERT INTO item VALUES (default, 50009, 1020, 'Skin/Item', NULL, 'Mochila Rosa da Slone');
        INSERT INTO item VALUES (default, 50009, 1020, 'Skin/Item', NULL, 'Paraquedas do Homem Morcego');
        INSERT INTO item VALUES (default, 50009, 1020, 'Skin/Roupa', 'Skin do Homem de Ferro', 'Homem de Ferro');
        INSERT INTO item VALUES (default, 50009, 1020, 'Skin/Roupa', 'Skin do Peixotoon', 'Peixotoon');
        INSERT INTO item VALUES (default, 50009, 1020, 'Skin/Arma', NULL, 'Cor Ciano Brilhante');
    """),
    "conquista" : ("""
        INSERT INTO conquista VALUES (default, 50009, 1002, 'Analista', 'Analise 15 recursos', 'TRUE');
        INSERT INTO conquista VALUES (default, 50009, 1002, 'Jantar Requintado', 'Cozinhe um inseto no Espeto para Assar', 'TRUE');
        INSERT INTO conquista VALUES (default, 50007, 1002, 'Dores do Crescimento', 'Obtenha sua primeira mutação', 'TRUE');
        INSERT INTO conquista VALUES (default, 50010, 1003, 'Progresso I: Aprendendo a me Virar', NULL, 'TRUE');
        INSERT INTO conquista VALUES (default, 50004, 1003, 'Morte I: E Então, O Que Aprendemos?', NULL, 'TRUE');
        INSERT INTO conquista VALUES (default, 50010, 1003, 'Suprimentos Pilhados I: Parecem Solitários. Vou Levá-los Comigo', NULL, 'FALSE');
        INSERT INTO conquista VALUES (default, 50001, 1004, 'Artista do sangue', NULL, 'TRUE');
        INSERT INTO conquista VALUES (default, 50002, 1004, 'Perdição dos mineradores', 'Derrote o Garimpeiro.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50001, 1004, 'Inseto inócuo', NULL, 'TRUE');
        INSERT INTO conquista VALUES (default, 50001, 1006, 'Sai pra lá', 'Evite que a equipe atacante toque na carga por 1 minuto em Jogo Rápido ou Competitivo.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50007, 1006, 'De lavada', 'Vença mapa de controle sem deixar que o inimigo capture um objetivo em Jogo Rápido ou Competitivo.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50001, 1006, 'Condecorado', 'Conclua 50 desafios.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50001, 1009, 'Bem-vindo a Los Santos', NULL, 'FALSE');
        INSERT INTO conquista VALUES (default, 50002, 1009, 'Carne Fresca', 'GTA Online: Complete o Tutorial.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50004, 1009, 'O Sonho Americano', 'GTA Online: Seja dono de uma Casa, uma Garagem e um Veículo Segurado.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50004, 1021, 'Armeiro', 'Aprimore uma arma.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50004, 1021, 'Oi, Charlie!', 'Destrua um Boneco Charlie.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50004, 1021, 'Nemesis Abatido?', NULL, 'TRUE');
        INSERT INTO conquista VALUES (default, 50006, 1013, 'Afrontador', NULL, 'FALSE');
        INSERT INTO conquista VALUES (default, 50002, 1013, 'Carcereiro Freeman', 'Sobreviva ao segundo confronto com torretas em Nova Prospekt.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50002, 1013, 'Sigam o Freeman', 'Assuma o comando de uma equipe de rebeldes durante a rebelião.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50001, 1013, 'Rebelde', 'Escape da invasão no bloco de apartamentos.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50001, 1013, 'Ferramenta Confiável', 'Pegue o pé de cabra.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50001, 1013, 'Armamento Pesado', 'Pegue a arma montada para o aerobarco.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50003, 1012, 'Terapeuta da família', NULL, 'TRUE');
        INSERT INTO conquista VALUES (default, 50003, 1012, 'Rato de biblioteca', 'Leia trinta livros, diários ou documentos variados.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50005, 1012, 'Vamos Cozinhar!', 'Aprenda 12 fórmulas de poções.', 'TRUE');
        INSERT INTO conquista VALUES (default, 50005, 1012, 'O carniceiro de Blaviken', 'Assassine pelo menos cinco adversários em menos de dez segundos.', 'FALSE');
        INSERT INTO conquista VALUES (default, 50005, 1012, 'Lilás e groselha', NULL, 'TRUE');
    """),
    "amigo" : ("""
        INSERT INTO amigo VALUES (50001, 50003);
        INSERT INTO amigo VALUES (50003, 50002);
        INSERT INTO amigo VALUES (50010, 50006);
        INSERT INTO amigo VALUES (50006, 50009);
        INSERT INTO amigo VALUES (50003, 50004);
        INSERT INTO amigo VALUES (50004, 50001);
        INSERT INTO amigo VALUES (50001, 50002);
        INSERT INTO amigo VALUES (50009, 50010);
    """),
    "avaliacao" : ("""
        INSERT INTO avaliacao VALUES (default, 1009, 50004, 'Vim do presente avisar que o trailer do GTA VI (6) vai sair em dezembro de 2023', 5);
        INSERT INTO avaliacao VALUES (default, 1009, 50007, 'JOGO MUITO BOM', 4);
        INSERT INTO avaliacao VALUES (default, 1006, 50002, 'Lee, oh Lee, o que foi que eu fiz? Olha só para você, nem está consciente e continua se empenhando em mostrar para o mundo o que pode fazer. Ele está nocauteado, tudo que o mantém de pé é o poder de sua vontade.', 2);
        INSERT INTO avaliacao VALUES (default, 1006, 50001, 'O jogo tem a comunidade mais tóxica que eu já presenciei. Se for jogar, jogue com os amigos/conhecidos ou simplesmente desabilite o chat. O MMR (Matchmaking) do jogo também é quebrado e ruim.', 1);
        INSERT INTO avaliacao VALUES (default, 1004, 50001, 'Eu criei uma carta chamada Manoel Gomes. Acho que só isso já devia ser o suficiente pra te fazer querer jgoar.', 5);
        INSERT INTO avaliacao VALUES (default, 1004, 50006, 'INSCRYPTION é o melhor jogo de cartas que já joguei até agora. Tem uma trama excelente e apesar de ser apenas um jogo de cartas, tem uma gameplay viciante no qual nunca se enjoara. Compre fora da promoção porque vale cada centavo! Uma experiencia unica.', 5);
        INSERT INTO avaliacao VALUES (default, 1017, 50007, 'Trilogia perfeita tanto versão original e também esse ótimo remake, única diferença além dos gráficos é que os pulos exige mais precisão nas plataformas tornado mais difícil que o original. Sobre a não recomendação... é mais um protesto por não lançarem o CRASH TEAM RACING NITRO-FUELED para PC... Ta de tiração Activision. _|_', 3);
        INSERT INTO avaliacao VALUES (default, 1017, 50004, 'Muito bom, agora pra ficar melhor só fazendo um remaster do Crash Twinsanity de 2004', 4);
        INSERT INTO avaliacao VALUES (default, 1016, 50010, 'O jogo tinha tudo para ser bom, porém a empresa não trabalha direito contra scripts, só quer saber de ganhar dinheiro com skins de fada', 1);
        INSERT INTO avaliacao VALUES (default, 1016, 50008, 'Estou muito feliz com minha nova skin de Irelia, porém podia ser mais barato', 3);
        INSERT INTO avaliacao VALUES (default, 1018, 50001, 'Jogo muito bom, uma pena não tem mais server BR pra jogar solo, ou duo', 3);
        INSERT INTO avaliacao VALUES (default, 1018, 50003, 'PUBG LITE ERA MELHOR', 1);
        INSERT INTO avaliacao VALUES (default, 1021, 50008, 'Depois de jogar o remake do RE4 consigo entender porque esse foi tão criticado. Sem analisar como um remake, se torna um jogo divertido (apesar de curto). Mas, de fato, é muito triste saber que cortaram tantas coisas importantes do jogo original. Ainda assim, vale a pena jogar e pegar numa boa promoção.', 4);
        INSERT INTO avaliacao VALUES (default, 1021, 50009, 'Mudou tudo e é muito curto o tempo de jogo', 1);
        INSERT INTO avaliacao VALUES (default, 1021, 50010, 'Terminei RE2 e fui sedento pro RE3 achando que ia ser tão bom quanto, porém me deparei com essa decepção.', 2);
    """),
    "midia" : ("""
        INSERT INTO midia VALUES(default, 1017, 'Imagem');
    """)
}
