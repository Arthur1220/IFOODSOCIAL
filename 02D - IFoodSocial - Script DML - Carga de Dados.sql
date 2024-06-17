-- -------------------------------------------------------------------
-- Script de Carga de Dados
-- -------------------------------------------------------------------

-- ****************************************************************************************
-- Dados básicos para localização de outros elementos
-- ****************************************************************************************

-- Dados básicos: CIDADE ---------------------------------------------
SELECT * FROM CIDADE;

INSERT INTO CIDADE
    (COD_CIDADE, DCR_CIDADE)
VALUES
    (1, 'Itabuna'),
    (2, 'Ilhéus'),
    (3, 'Itauípe');

-- Dados básicos: BAIRRO -------------------------------------------------------

SELECT * FROM BAIRRO ORDER BY COD_CIDADE;

INSERT INTO BAIRRO
    (COD_BAIRRO, DCR_BAIRRO, COD_CIDADE)
VALUES
    (10, 'Centro', 1),
    (11, 'Conceição', 1),
    (12, 'Góes Calmon', 1),
    (20, 'Salobrinho', 2),
    (21, 'Centro', 2),
    (22, 'Pontal', 2),
    (30, 'Centro', 3);

-- Dados básicos: LOCALIDADE  --------------------------------------------

SELECT c.COD_CIDADE, c.DCR_CIDADE,
       b.COD_BAIRRO, b.DCR_BAIRRO,
       loc.COD_LOCALIDADE, loc.DCR_LOCALIDADE
FROM LOCALIDADE loc
INNER JOIN BAIRRO b ON loc.COD_BAIRRO = b.COD_BAIRRO
INNER JOIN CIDADE c ON b.COD_CIDADE = c.COD_CIDADE
ORDER BY c.COD_CIDADE, b.COD_BAIRRO, loc.COD_LOCALIDADE;

INSERT INTO LOCALIDADE
    (COD_LOCALIDADE, DCR_LOCALIDADE, COD_BAIRRO, LOCALIDADE_COD_LOCALIDADE)
VALUES
    (100, 'Praça Camacan', 10, 100),
    (101, 'Igreja Matriz', 10, 101),
    (110, 'Pracinha', 11, 110),
    (111, 'Campo Lazer', 11, 111),
    (120, 'Daniel San', 12, 120),
    (121, 'Shopping', 12, 121),
    (122, 'Shopping - Praça Alimentação', 12, 121),
    (123, 'Shopping - Area 2o Andar', 12, 121),
    (200, 'UESC', 20, 200),
    (201, 'UESC - CEU', 20, 200),
    (202, 'UESC - Cantina Sandro', 20, 200),
    (203, 'UESC - Portaria', 20, 200),
    (204, 'UESC - Bosque', 20, 200),
    (210, 'Ponto da Rota', 21, 210),
    (220, 'Passarela do Álcool', 22, 210),
    (300, 'Rodoviária', 30, 300);

-- ****************************************************************************************
--  Empreendedor
-- ****************************************************************************************

-- Empreendedor: EMPREENDIMENTO --------------------------------------------------

INSERT INTO EMPREENDIMENTO
    (COD_EMPREEDIMENTO, DCR_EMPREENDIMENTO, DCR_NOME_FANTASIA, DCR_ENDERECO,
     DCR_COMPLEMENTO, NUM_CEP, COD_CIDADE, BAIRRO_COD_BAIRRO,
     COD_LOCALIDADE, IMG_EMPREENDIMENTO)
VALUES
    (1, 'Esmeralda Delícias', 'Esmeralda Delícias', 'Rua Central, 20',
     '-', '45662-000', 2, 20, 200, NULL),
    (2, 'Espaço das Empadas', 'Espaço das Empadas', 'Rua Aurora, 100',
     '20 Andar', '45605-340', 1, 11, 111, NULL);

-- Empreendedor: FUNCIONARIO -----------------------------------------------------

INSERT INTO FUNCIONARIO
    (COD_FUNCIONARIO, NOME_FUNCIONARIO, NUM_TELEFONE, DCR_EMAIL)
VALUES
    (10, 'Dona Esmeralda', '73 983217876', 'merinha@gmail.com'),
    (11, 'Fabiana - (Filha Esmeralda)', '73 983218023', 'fabizinha02@gmail.com'),
    (12, 'Luis Carlos - (Sobrinho Esmeralda)', '73 93748023', 'lcporradao@gmail.com'),
    (20, 'Aline', '73 983219500', 'alineempadas@gmail.com'),
    (21, 'Joice (Amiga Aline)', '73 995553210', 'joiceempadas@gmail.com'),
    (22, 'Crizaldino', '71 944213748', 'crizaldino@gmail.com');

-- Empreendedor: Empreend_Funciononario -------------------------------------------

SELECT e.COD_EMPREEDIMENTO, e.DCR_EMPREENDIMENTO,
       f.COD_FUNCIONARIO, f.NOME_FUNCIONARIO,
       ef.COD_EMPREEND_FUNCIONARIO, ef.TIP_FUNCIONARIO
FROM EMPREENDIMENTO e
INNER JOIN FUNCIONARIO f ON e.COD_EMPREEDIMENTO = ef.COD_EMPREEDIMENTO
INNER JOIN EMPREEND_FUNCIONARIO ef ON f.COD_FUNCIONARIO = ef.COD_FUNCIONARIO
ORDER BY e.COD_EMPREEDIMENTO, f.COD_FUNCIONARIO;

INSERT INTO EMPREEND_FUNCIONARIO
    (COD_EMPREEND_FUNCIONARIO, TIP_FUNCIONARIO,
     COD_EMPREEDIMENTO, COD_FUNCIONARIO, IMG_EMPREEND_FUNCIONARIO)
VALUES
    (10, 'P', 1, 10, NULL),
    (11, 'V', 1, 11, NULL),
    (12, 'E', 1, 12, NULL),
    (20, 'P', 2, 20, NULL),
    (21, 'V', 2, 21, NULL),
    (22, 'E', 2, 22, NULL);

-- ******************************************************************************************
-- PRODUTOs
-- ******************************************************************************************

-- PRODUTOs: CATEGORIA -----------------------------------------------------------

INSERT INTO CATEGORIA
    (COD_CATEGORIA, DCR_CATEGORIA, IMG_CATEGORIA, COD_EMPREEDIMENTO)
VALUES
    (10, 'Refeições', NULL, 1),
    (11, 'Lasanhas', NULL, 1),
    (12, 'Bebidas', NULL, 1),
    (13, 'Sobremesas', NULL, 1),
    (20, 'Empadas salgadas', NULL, 2),
    (21, 'Empadas doces', NULL, 2),
    (22, 'Quiches', NULL, 2),
    (23, 'Salgados diversos', NULL, 2),
    (24, 'Salgados light', NULL, 2),
    (25, 'Sucos', NULL, 2);

-- PRODUTOs: PRODUTOs -------------------------------------------------------------

-- 10 Refeições 1
INSERT INTO PRODUTO
    (COD_PRODUTO, DCR_PRODUTO, IMG_PRODUTO, VLR_PRODUTO,
     FLAG_DISPONIVEL, COD_CATEGORIA, COD_EMPREEDIMENTO)
VALUES
    (100, 'PF - 1 carne', NULL, 15.00, 'S', 10, 1),
    (101, 'PF - 2 carnes', NULL, 19.00, 'S', 10, 1);

-- 11 Lasanhas 1
INSERT INTO PRODUTO
    (COD_PRODUTO, DCR_PRODUTO, IMG_PRODUTO, VLR_PRODUTO,
     FLAG_DISPONIVEL, COD_CATEGORIA, COD_EMPREEDIMENTO)
VALUES
    (110, 'Lasanha de carne', NULL, 16.00, 'S', 11, 1),
    (111, 'Lasanha de frango', NULL, 13.00, 'S', 11, 1);

-- 12 Bebidas 1
INSERT INTO PRODUTO
    (COD_PRODUTO, DCR_PRODUTO, IMG_PRODUTO, VLR_PRODUTO,
     FLAG_DISPONIVEL, COD_CATEGORIA, COD_EMPREEDIMENTO)
VALUES
    (120, 'Refri - Caçulinha', NULL, 2.50, 'S', 12, 1),
    (121, 'Refri - Lata', NULL, 4.50, 'S', 12, 1),
    (122, 'Suco do dia', NULL, 2.00, 'S', 12, 1);

-- 13 Sobremesas 1
INSERT INTO PRODUTO
    (COD_PRODUTO, DCR_PRODUTO, IMG_PRODUTO, VLR_PRODUTO,
     FLAG_DISPONIVEL, COD_CATEGORIA, COD_EMPREEDIMENTO)
VALUES
    (130, 'Doce do dia', NULL, 2.20, 'S', 13, 1);

-- Produtos: Empadas Salgadas (COD_EMPREEDIMENTO = 2)
INSERT INTO `PRODUTO`
(`COD_PRODUTO`, `DCR_PRODUTO`, `IMG_PRODUTO`, `VLR_PRODUTO`, `FLAG_DISPONIVEL`, `COD_CATEGORIA`, `COD_EMPREEDIMENTO`)
VALUES
(200, 'Frango', NULL, 5.00, 'S', 20, 2),
(201, 'Frango com Catupiry', NULL, 5.50, 'S', 20, 2),
(202, 'Camarão', NULL, 6.50, 'S', 20, 2),
(203, 'Carne seca com banana', NULL, 5.00, 'S', 20, 2);

-- Produtos: Empadas Doces (COD_EMPREEDIMENTO = 2)
INSERT INTO `PRODUTO`
(`COD_PRODUTO`, `DCR_PRODUTO`, `IMG_PRODUTO`, `VLR_PRODUTO`, `FLAG_DISPONIVEL`, `COD_CATEGORIA`, `COD_EMPREEDIMENTO`)
VALUES
(210, 'Brigadeiro', NULL, 4.00, 'S', 21, 2),
(211, 'Romeu e Julieta', NULL, 4.00, 'S', 21, 2);

-- Produtos: Quiches (COD_EMPREEDIMENTO = 2)
INSERT INTO `PRODUTO`
(`COD_PRODUTO`, `DCR_PRODUTO`, `IMG_PRODUTO`, `VLR_PRODUTO`, `FLAG_DISPONIVEL`, `COD_CATEGORIA`, `COD_EMPREEDIMENTO`)
VALUES
(220, 'Alho poro com bacon', NULL, 6.50, 'S', 22, 2),
(221, 'Calabresa apimentada', NULL, 5.50, 'S', 22, 2);

-- Produtos: Salgados diversos (COD_EMPREEDIMENTO = 2)
INSERT INTO `PRODUTO`
(`COD_PRODUTO`, `DCR_PRODUTO`, `IMG_PRODUTO`, `VLR_PRODUTO`, `FLAG_DISPONIVEL`, `COD_CATEGORIA`, `COD_EMPREEDIMENTO`)
VALUES
(230, 'Coxinha de frango', NULL, 4.50, 'S', 23, 2),
(231, 'Quibe', NULL, 4.50, 'S', 23, 2);

-- Produtos: Salgados light (COD_EMPREEDIMENTO = 2)
INSERT INTO `PRODUTO`
(`COD_PRODUTO`, `DCR_PRODUTO`, `IMG_PRODUTO`, `VLR_PRODUTO`, `FLAG_DISPONIVEL`, `COD_CATEGORIA`, `COD_EMPREEDIMENTO`)
VALUES
(240, 'Pastel integral - frango com ricota', NULL, 6.50, 'S', 24, 2),
(241, 'Pastel integral - queijo e tomate seco', NULL, 6.50, 'S', 24, 2);

-- Produtos: Sucos (COD_EMPREEDIMENTO = 2)
INSERT INTO `PRODUTO`
(`COD_PRODUTO`, `DCR_PRODUTO`, `IMG_PRODUTO`, `VLR_PRODUTO`, `FLAG_DISPONIVEL`, `COD_CATEGORIA`, `COD_EMPREEDIMENTO`)
VALUES
(250, 'Cajá', NULL, 4.00, 'S', 25, 2),
(251, 'Manga', NULL, 4.00, 'S', 25, 2);

-- Cardápios: Esmeralda (COD_EMPREEDIMENTO = 1)
INSERT INTO `CARDAPIO`
(`COD_CARDAPIO`, `DCR_CARDAPIO`, `DCR_TITULO_APRES`, `COD_EMPREEDIMENTO`)
VALUES
(1, 'Versão inicial - Esmeralda', 'Cardápio Dona Esmeralda', 1);

-- Cardápios: Espaço da Empada (COD_EMPREEDIMENTO = 2)
INSERT INTO `CARDAPIO`
(`COD_CARDAPIO`, `DCR_CARDAPIO`, `DCR_TITULO_APRES`, `COD_EMPREEDIMENTO`)
VALUES
(2, 'Versão inicial - Aline', 'Cardápio Espaço da Empada', 2);

-- Seções do Cardápio
INSERT INTO `secao_CARDAPIO`
(`COD_SECAO_CARDAPIO`, `DCR_SECAO_CARDAPIO`, `DCR_TITULO_APRES`, `COD_CARDAPIO`, `NUM_ORDEM`)
VALUES
(10, 'Refeições', 'Refeições', 1, 1),
(11, 'Lasanhas', 'Lasanhas', 1, 2),
(12, 'Bebidas', 'Bebidas', 1, 3),
(13, 'Sobremesas', 'Sobremesas', 1, 4),
(20, 'Empadas Salgadas', 'Empadas Salgadas', 2, 1),
(21, 'Empadas Doces', 'Empadas Doces', 2, 2),
(22, 'Quiches', 'Quiches', 2, 3),
(23, 'Salgados diversos', 'Salgados diversos', 2, 4),
(24, 'Salgados light', 'Salgados light', 2, 5),
(25, 'Sucos', 'Sucos', 2, 6);

-- PRODUTOs: PRODUTOs nas Secoes dos Cardápios ------------------------------------------------
SELECT e.COD_EMPREEDIMENTO, e.DCR_EMPREENDIMENTO,
       c.COD_CARDAPIO, c.DCR_CARDAPIO,
       sc.COD_SECAO_CARDAPIO, sc.DCR_TITULO_APRES,
       p.COD_PRODUTO, p.DCR_PRODUTO
FROM secao_CARDAPIO sc
JOIN CARDAPIO c ON sc.cod_CARDAPIO = c.cod_CARDAPIO
JOIN EMPREENDIMENTO e ON c.COD_EMPREEDIMENTO = e.COD_EMPREEDIMENTO
JOIN SECAO_PRODUTO sp ON sp.SECAO_CARDAPIO_COD_SECAO_CARDAPIO = sc.COD_SECAO_CARDAPIO
JOIN PRODUTO p ON sp.PRODUTO_COD_PRODUTO = p.COD_PRODUTO
ORDER BY e.COD_EMPREEDIMENTO, c.COD_CARDAPIO, sc.COD_SECAO_CARDAPIO, sc.NUM_ORDEM;

-- Insertions into SECAO_PRODUTO table
INSERT INTO `SECAO_PRODUTO` (`COD_SECAO_PRODUTO`, `PRODUTO_COD_PRODUTO`, `SECAO_CARDAPIO_COD_SECAO_CARDAPIO`, `NUM_ORDEM`)
VALUES
(100, 100, 10, 1),
(101, 101, 10, 2),
(110, 110, 11, 1),
(111, 111, 11, 2),
(120, 120, 12, 1),
(121, 121, 12, 2),
(122, 122, 12, 3),
(130, 130, 13, 1),
(200, 200, 20, 1),
(201, 201, 20, 2),
(202, 202, 20, 3),
(203, 203, 20, 4),
(210, 210, 21, 1),
(211, 211, 21, 2),
(220, 220, 22, 1),
(221, 221, 22, 2),
(230, 230, 23, 1),
(231, 231, 23, 2),
(240, 240, 24, 1),
(241, 241, 24, 2),
(250, 250, 25, 1),
(251, 251, 25, 2);

-- *******************************************************************************************
-- CLIENTE
-- *******************************************************************************************
SELECT * FROM CLIENTE;

INSERT INTO `CLIENTE` (`COD_CLIENTE`, `NOME_CLIENTE`, `DCR_ENDERECO`, `DCR_COMPLEMENTO`, `NUM_CEP`, `COD_CIDADE`, `COD_BAIRRO`, `COD_LOCALIDADE`)
VALUES
(1, 'Carlos Alberto', 'UESC', 'UESC', '45662-900', 2, 20, 200),
(2, 'João Marcos', 'UESC', 'UESC', '45662-900', 2, 20, 200),
(3, 'Marcela', 'Rua Bela Vista, 30', 'Apto 102', '45605-255', 1, 11, 110);

-- *******************************************************************************************
-- PEDIDO
-- *******************************************************************************************
-- Forma de pagamento -----------------------------------------------------------------------
SELECT * FROM FORMA_PAGTO;

INSERT INTO `FORMA_PAGTO` (`COD_FORMA_PAGTO`, `DCR_FORMA_PAGTO`)
VALUES
(1, 'Dinheiro'),
(2, 'PIX'),
(3, 'Crédito'),
(4, 'Débito');

-- PEDIDO e Item PEDIDO -----------------------------------------------------------------------
SELECT cli.NOME_CLIENTE, 
       ped.COD_PEDIDO, ped.DATA_PEDIDO, ped.VLR_PEDIDO,
       prod.cod_PRODUTO, prod.DCR_PRODUTO,
       ip.QTD_PRODUTO, ip.VLR_PRODUTO, ip.VLR_TOTAL
FROM PEDIDO ped
JOIN item_PEDIDO ip ON ped.cod_PEDIDO = ip.COD_PEDIDO
JOIN CLIENTE cli ON ped.COD_CLIENTE = cli.COD_CLIENTE
JOIN PRODUTO prod ON ip.COD_PRODUTO = prod.COD_PRODUTO;

SELECT * FROM item_PEDIDO;

-- PEDIDO; Carlos Alberto ------------------------------------------------
INSERT INTO `PEDIDO` (`COD_PEDIDO`, `TIP_PEDIDO`, `DATA_PEDIDO`, `VLR_PEDIDO`, `TIP_STATUS`, `COD_CLIENTE`, `COD_FORMA_PAGTO`, `DCR_DADOS_PAGTO`)
VALUES
(10, 'P', STR_TO_DATE('05/06/2024 11:45', '%d/%m/%Y %H:%i'), 19.20, 'A', 1, 1, 'Dinheiro');

INSERT INTO `ITEM_PEDIDO` (`COD_ITEM_PEDIDO`, `VLR_PRODUTO`, `QTD_PRODUTO`, `VLR_TOTAL`, `COD_PEDIDO`, `COD_PRODUTO`)
VALUES
(100, 15.00, 1, 15.00, 10, 100),
(101, 2.00, 1, 2.00, 10, 122),
(102, 2.20, 1, 2.20, 10, 130);

-- PEDIDO 2 --------------------------------------------------------------------------------------
INSERT INTO `PEDIDO` (`COD_PEDIDO`, `TIP_PEDIDO`, `DATA_PEDIDO`, `VLR_PEDIDO`, `TIP_STATUS`,`COD_CLIENTE`, `COD_FORMA_PAGTO`, `DCR_DADOS_PAGTO`)
VALUES
(20, 'P', STR_TO_DATE('06/06/2024 15:12', '%d/%m/%Y %H:%i'), 33.5, 'A', 2, 2, 'CPF: 07129211032');

INSERT INTO `ITEM_PEDIDO` (`COD_ITEM_PEDIDO`, `VLR_PRODUTO`, `QTD_PRODUTO`, `VLR_TOTAL`, `COD_PEDIDO`, `COD_PRODUTO`)
VALUES
(200, 6.5, 2, 13.0, 20, 202),
(201, 4.0, 1, 4.0, 20, 210),
(202, 4.5, 1, 4.5, 20, 230),
(203, 4.0, 2, 8.0, 20, 250),
(204, 4.0, 1, 4.0, 20, 251);

-- PEDIDO 3 --------------------------------------------------------------------------------------
INSERT INTO `PEDIDO` (`COD_PEDIDO`, `TIP_PEDIDO`, `DATA_PEDIDO`, `VLR_PEDIDO`, `TIP_STATUS`,`COD_CLIENTE`, `COD_FORMA_PAGTO`, `DCR_DADOS_PAGTO`)
VALUES
(20, 'P', STR_TO_DATE('06/06/2024 15:12', '%d/%m/%Y %H:%i'), 33.5, 'A', 2, 2, 'CPF: 07129211032');

INSERT INTO `item_PEDIDO` (`COD_ITEM_PEDIDO`, `VLR_PRODUTO`, `QTD_PRODUTO`, `VLR_TOTAL`, `COD_PEDIDO`, `COD_PRODUTO`)
VALUES
(200, 6.5, 2, 13.0, 20, 202),
(201, 4.0, 1, 4.0, 20, 210),
(202, 4.5, 1, 4.5, 20, 230),
(203, 4.0, 2, 8.0, 20, 250),
(204, 4.0, 1, 4.0, 20, 251);

SELECT * FROM PEDIDO;

-- *******************************************************************************************
-- ENTREGAs
-- *******************************************************************************************
-- EVENTOs de ENTREGA ---------------------------------------------------------------------
INSERT INTO `EVENTO` (`COD_EVENTO`, `DCR_EVENTO`, `NUM_ORDEM_EVENTO`)
VALUES
(1, 'A - PEDIDO feito', 1),
(2, 'B - Iniciada preparação', 2),
(3, 'C - Retirada', 3),
(4, 'D - ENTREGA', 4);

-- ENTREGA ------------------------------------------------------------------------------
INSERT INTO `ENTREGA` (`COD_ENTREGA`, `COD_PEDIDO`, `COD_FUNCIONARIO`, `DATA_SAIDA`, `DATA_ENTREGA`, `VLR_ENTREGA`, `DCR_ENDERECO`, `DCR_COMPLEM`, `NUM_CEP`, `TXT_REFERENCIA`, `COD_CIDADE`, `COD_BAIRRO`, `COD_LOCALIDADE`, `FLAG_ENCOMENDA`, `FLAG_ENTREGADOR`)
VALUES
(200, 20, 22, STR_TO_DATE('06/06/2024 15:20', '%d/%m/%Y %H:%i'), STR_TO_DATE('06/06/2024 15:35', '%d/%m/%Y %H:%i'), 33.50, 'UESC - CEU', '-', '-', 'Próximo à xerox', 2, 20, 201, 'N', 'S');

DELETE FROM RASTREAMENTO_PEDIDO WHERE cod_RASTREAMENTO_PEDIDO = 4;
SELECT * FROM RASTREAMENTO_PEDIDO;

-- EVENTOs de ENTREGA ---------------------------------------------------------------
INSERT INTO `RASTREAMENTO_PEDIDO` (`COD_RASTREAMENTO_PEDIDO`, `COD_PEDIDO`, `COD_EVENTO_PEDIDO`, `DATA_HORA_EVENTO`)
VALUES
(2001, 20, 1, STR_TO_DATE('06/06/2024 15:12', '%d/%m/%Y %H:%i')),
(2002, 20, 2, STR_TO_DATE('06/06/2024 15:15', '%d/%m/%Y %H:%i')),
(2003, 20, 3, STR_TO_DATE('06/06/2024 15:20', '%d/%m/%Y %H:%i'));