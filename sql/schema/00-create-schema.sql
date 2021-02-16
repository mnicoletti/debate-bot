-- Database
CREATE DATABASE `debatebot` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

-- apex_maps
CREATE TABLE `apex_maps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- apex_pois
CREATE TABLE `apex_pois` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- apex_map_poi
CREATE TABLE `apex_map_poi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_maps` int(11) NOT NULL,
  `id_pois` int(11) NOT NULL,
  `enabled` tinyint(1) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `id_maps_tbl_idx` (`id_maps`),
  KEY `id_pois_tbl_idx` (`id_pois`),
  CONSTRAINT `id_maps_tbl` FOREIGN KEY (`id_maps`) REFERENCES `apex_maps` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `id_pois_tbl` FOREIGN KEY (`id_pois`) REFERENCES `apex_pois` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4;
