DROP TABLE IF EXISTS `carros`;
CREATE TABLE IF NOT EXISTS `carros` (
  `id_carro` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `fabricante` tinyint NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `cor` tinyint NOT NULL,
  `ano` int(11) NOT NULL,
  FOREIGN KEY (`Fabricante`) REFERENCES `fabricante`(`id_fabricante`),
  FOREIGN KEY (`cor`) REFERENCES `cor`(`cor`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nome_cliente` varchar(100) NOT NULL UNIQUE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `cor`;
CREATE TABLE IF NOT EXISTS `cor` (
  `id_cor` tinyint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nome_cor` varchar(30) NOT NULL UNIQUE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `fabricante`;
CREATE TABLE IF NOT EXISTS `fabricante` (
  `id_fabricante` tinyint NOT NULL AUTO_INCREMENT,
  `nome_fabricante` varchar(100) NOT NULL UNIQUE,
  PRIMARY KEY (`id_fabricante`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `venda`;
CREATE TABLE IF NOT EXISTS `venda` (
  `id_Venda` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Estado` varchar(50) NOT NULL,
  `Valor_Venda` double NOT NULL,
  `Valor_Custo` double NOT NULL,
  `Total_Desconto` double NOT NULL,
  `Custo_Entrega` double NOT NULL,
  `Custo_Mao` double NOT NULL,
  `Data_Compra` date NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_carro` int(11) DEFAULT NULL,
  FOREIGN KEY (`id_cliente`) REFERENCES `cliente`(`id_cliente`),
  FOREIGN KEY (`id_carro`) REFERENCES `carros`(`id_carro`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;