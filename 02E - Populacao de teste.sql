--Inserts na tabela CIDADE--
INSERT INTO CIDADE (cod_cidade, dcr_cidade) VALUES (4, 'São Paulo');
INSERT INTO CIDADE (cod_cidade, dcr_cidade) VALUES (5, 'Rio de Janeiro');
INSERT INTO CIDADE (cod_cidade, dcr_cidade) VALUES (6, 'Belo Horizonte');

--Inserts na tabela BAIRRO--
-- Inserindo bairros na cidade Sao Paulo
INSERT INTO BAIRRO (cod_bairro, dcr_bairro, cod_cidade) VALUES (40, 'Jardins', 4);
INSERT INTO BAIRRO (cod_bairro, dcr_bairro, cod_cidade) VALUES (41, 'Moema', 4);

-- Inserindo bairros na cidade Rio de Janeiro
INSERT INTO BAIRRO (cod_bairro, dcr_bairro, cod_cidade) VALUES (42, 'Copacabana', 5);
INSERT INTO BAIRRO (cod_bairro, dcr_bairro, cod_cidade) VALUES (43, 'Ipanema', 5);

-- Inserindo bairros na cidade Belo Horizonte
INSERT INTO BAIRRO (cod_bairro, dcr_bairro, cod_cidade) VALUES (44, 'Savassi', 6);
INSERT INTO BAIRRO (cod_bairro, dcr_bairro, cod_cidade) VALUES (45, 'Lourdes', 6);

--Inserts na tabela LOCALIDADE--
-- Localidades para a cidade 1 (São Paulo)
INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (400, 'Avenida Paulista', 40, 400);

INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (401, 'Parque Ibirapuera', 40, 401);

INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (402, 'Estádio do Morumbi', 41, 402);

-- Localidades para a cidade 2 (Rio de Janeiro)
INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (500, 'Praia de Copacabana', 42, 500);

INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (501, 'Pão de Açúcar', 43, 501);

INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (502, 'Jardim Botânico', 43, 502);

-- Localidades para a cidade 3 (Belo Horizonte)
INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (600, 'Praça da Liberdade', 44, 600);

INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (601, 'Mercado Central', 44, 601);

INSERT INTO LOCALIDADE (cod_localidade, dcr_localidade, cod_bairro, localidade_cod_localidade)
VALUES (602, 'Lagoa da Pampulha', 45, 602);

--Inserts na tabela CLIENTE--
INSERT INTO CLIENTE (cod_cliente, nome_cliente, dcr_endereco, dcr_complemento, num_cep, cod_cidade, cod_bairro, cod_localidade)
VALUES (4, 'Otacilio Jose Pereira', 'Rua das Flores, 123', 'Apto 101', '01234-567', 4, 40, 400);

INSERT INTO CLIENTE (cod_cliente, nome_cliente, dcr_endereco, dcr_complemento, num_cep, cod_cidade, cod_bairro, cod_localidade)
VALUES (5, 'Marta Magda Dornelles', 'Av. Principal, 456', 'Casa', '89012-345', 5, 43, 501);

INSERT INTO CLIENTE (cod_cliente, nome_cliente, dcr_endereco, dcr_complemento, num_cep, cod_cidade, cod_bairro, cod_localidade)
VALUES (6, 'Lilia Cabral', 'Rua das Palmeiras, 789', 'Bloco C', '34567-890', 6, 44, 602);

--Inserts na tabela EMPREENDIMENTO--
INSERT INTO EMPREENDIMENTO (COD_EMPREEDIMENTO, DCR_EMPREENDIMENTO, DCR_NOME_FANTASIA, DCR_ENDERECO, DCR_COMPLEMENTO, NUM_CEP, COD_CIDADE, BAIRRO_COD_BAIRRO, COD_LOCALIDADE, IMG_EMPREENDIMENTO)
VALUES (3, 'Cabana de Acarajé', 'As Baianas', 'Rua Principal, 70','-', '45322-000', 5, 43, 500, NULL);

INSERT INTO EMPREENDIMENTO (COD_EMPREEDIMENTO, DCR_EMPREENDIMENTO, DCR_NOME_FANTASIA, DCR_ENDERECO, DCR_COMPLEMENTO, NUM_CEP, COD_CIDADE, BAIRRO_COD_BAIRRO, COD_LOCALIDADE, IMG_EMPREENDIMENTO)
VALUES (4, 'Bolos Doces', 'Doce Sonho', 'Rua da Mangueira, 120','-', '41642-000', 4, 41, 400, NULL);

--Inserts na tabela PRODUTOS--
-- Produtos para o Empreendimento ID 3
INSERT INTO PRODUTO (cod_produto, dcr_produto, img_produto, vlr_produto, flag_disponivel, cod_categoria, cod_empreedimento)
VALUES (400, 'Feijoada Completa', NULL, 45.90, 'S', 10, 3);

INSERT INTO PRODUTO (cod_produto, dcr_produto, img_produto, vlr_produto, flag_disponivel, cod_categoria, cod_empreedimento)
VALUES (401, 'Lasanha Bolonhesa', NULL, 35.50, 'S', 11, 3);

INSERT INTO PRODUTO (cod_produto, dcr_produto, img_produto, vlr_produto, flag_disponivel, cod_categoria, cod_empreedimento)
VALUES (402, 'Mousse de Chocolate', NULL, 15.00, 'S', 13, 3);

-- Produtos para o Empreendimento ID 4
INSERT INTO PRODUTO (cod_produto, dcr_produto, img_produto, vlr_produto, flag_disponivel, cod_categoria, cod_empreedimento)
VALUES (500, 'Empada de Frango', NULL, 5.50, 'S', 20, 4);

INSERT INTO PRODUTO (cod_produto, dcr_produto, img_produto, vlr_produto, flag_disponivel, cod_categoria, cod_empreedimento)
VALUES (501, 'Empada de Chocolate', NULL, 4.00, 'S', 21, 4);

INSERT INTO PRODUTO (cod_produto, dcr_produto, img_produto, vlr_produto, flag_disponivel, cod_categoria, cod_empreedimento)
VALUES (502, 'Quiche de Queijo', NULL, 12.00, 'S', 22, 4);

--Inserts na tabela PEDIDOS E ITENS_PEDIDOS--
-- Pedido 1
INSERT INTO PEDIDO (cod_pedido, tip_pedido, data_pedido, vlr_pedido, tip_status, cod_cliente, cod_forma_pagto, dcr_dados_pagto)
VALUES (30, 'A', '2024-06-15 10:00:00', 75.90, 'P', 4, 1, 'Dinheiro');

-- Itens do Pedido 1
INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (300, 45.90, 1, 45.90, 30, 400); -- Feijoada Completa

INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (301, 30.00, 1, 30.00, 30, 402); -- Mousse de Chocolate

-- Pedido 2
INSERT INTO PEDIDO (cod_pedido, tip_pedido, data_pedido, vlr_pedido, tip_status, cod_cliente, cod_forma_pagto, dcr_dados_pagto)
VALUES (40, 'B', '2024-06-15 12:30:00', 22.50, 'A', 5, 2, 'PIX');

-- Itens do Pedido 2
INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (400, 5.50, 2, 11.00, 40, 500); -- Empada de Frango

INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (401, 4.00, 1, 4.00, 40, 501); -- Empada de Chocolate

-- Pedido 3
INSERT INTO PEDIDO (cod_pedido, tip_pedido, data_pedido, vlr_pedido, tip_status, cod_cliente, cod_forma_pagto, dcr_dados_pagto)
VALUES (50, 'A', '2024-06-15 15:45:00', 50.00, 'E', 6, 4, 'Cartão de Débito');

-- Itens do Pedido 3
INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (500, 12.00, 2, 24.00, 50, 502); -- Quiche de Queijo

-- Pedido 4
INSERT INTO PEDIDO (cod_pedido, tip_pedido, data_pedido, vlr_pedido, tip_status, cod_cliente, cod_forma_pagto, dcr_dados_pagto)
VALUES (60, 'B', '2024-06-16 09:15:00', 65.00, 'P', 5, 1, 'Cartão de Crédito');

-- Itens do Pedido 4
INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (602, 35.50, 1, 35.50, 60, 401); -- Lasanha Bolonhesa

INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (601, 29.50, 1, 29.50, 60, 501); -- Empada de Chocolate

-- Pedido 5
INSERT INTO PEDIDO (cod_pedido, tip_pedido, data_pedido, vlr_pedido, tip_status, cod_cliente, cod_forma_pagto, dcr_dados_pagto)
VALUES (70, 'A', '2024-06-16 13:30:00', 38.00, 'E', 4, 2, 'PIX');

-- Itens do Pedido 5
INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (701, 5.50, 1, 5.50, 70, 500); -- Empada de Frango

INSERT INTO ITEM_PEDIDO (cod_item_pedido, vlr_produto, qtd_produto, vlr_total, cod_pedido, cod_produto)
VALUES (702, 12.00, 1, 12.00, 70, 502); -- Quiche de Queijo

