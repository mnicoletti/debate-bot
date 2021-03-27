-- Database
CREATE DATABASE `debatebot` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE debatebot;

-- apex_maps
CREATE TABLE `apex_maps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- apex_pois
CREATE TABLE `apex_pois` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_maps` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `enabled` tinyint(1) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `funciones_frases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `funcion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `string_frases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_funcion` int(11) NOT NULL,
  `mensaje` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `id_funciones_frases_idx` (`id_funcion`),
  CONSTRAINT `id_funciones_frases` FOREIGN KEY (`id_funcion`) REFERENCES `funciones_frases` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `perfect_offline` (
  `id` varchar(20) NOT NULL,
  `nickname` varchar(45) NOT NULL,
  `offline_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `nickname_UNIQUE` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
