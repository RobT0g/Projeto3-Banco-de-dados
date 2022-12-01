DROP TABLE IF EXISTS `carros`;
CREATE TABLE IF NOT EXISTS `carros` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `modelo` varchar(50) NOT NULL,
  `ano` int(11) NOT NULL,
  `fabricante` tinyint NOT NULL,
  FOREIGN KEY (`fabricante`) REFERENCES `fabricante`(`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nome` varchar(100) NOT NULL UNIQUE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `cor`;
CREATE TABLE IF NOT EXISTS `cor` (
  `id` tinyint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `cor` varchar(30) NOT NULL UNIQUE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `fabricante`;
CREATE TABLE IF NOT EXISTS `fabricante` (
  `id` tinyint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `fabricante` varchar(100) NOT NULL UNIQUE
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `venda`;
CREATE TABLE IF NOT EXISTS `venda` (
  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `estado` varchar(50) NOT NULL,
  `valor` double NOT NULL,
  `custo` double NOT NULL,
  `desconto` double NOT NULL,
  `entrega` double NOT NULL,
  `mao` double NOT NULL,
  `data` date NOT NULL,
  `cliente` int(11) DEFAULT NULL,
  `carro` int(11) DEFAULT NULL,
  `cor` tinyint DEFAULT NULL,
  FOREIGN KEY (`cliente`) REFERENCES `cliente`(`id`),
  FOREIGN KEY (`carro`) REFERENCES `carros`(`id`),
  FOREIGN KEY (`cor`) REFERENCES `cor`(`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;