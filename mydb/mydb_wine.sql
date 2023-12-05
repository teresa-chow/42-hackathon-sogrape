-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `wine`
--

DROP TABLE IF EXISTS `wine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wine` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ean` bigint NOT NULL,
  `name` varchar(200) NOT NULL,
  `store` varchar(200) DEFAULT NULL,
  `year` varchar(10) DEFAULT NULL,
  `capacity` varchar(30) NOT NULL,
  `price` decimal(7,2) NOT NULL,
  `curr` varchar(5) NOT NULL,
  `disc` varchar(20) DEFAULT 'NO',
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `loc` varchar(100) DEFAULT NULL,
  `img` varchar(300) DEFAULT NULL,
  `descr` mediumtext,
  `pair` mediumtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wine`
--

LOCK TABLES `wine` WRITE;
/*!40000 ALTER TABLE `wine` DISABLE KEYS */;
INSERT INTO `wine` VALUES (100,5601012011500,'Mateus Vinho Rosé','Continente','N/A','750ml',2.79,'€','NO','2023-10-25 15:38:17','pt','./img/Mateus Rosé Original.jpg',NULL,NULL),(101,5601012001310,'Mateus Sparkling Espumante Rosé Bruto','Continente','N/A','750ml',6.99,'€','NO','2023-10-25 15:38:18','pt','./img/Mateus Sparkling Rosé.jpg',NULL,NULL),(102,5601012004427,'Trinca Bolotas Regional Alentejano Vinho Tinto','Continente','N/A','750ml',6.99,'€','NO','2023-10-25 15:38:19','pt','./img/Herdade do Peso Trinca Bolotas Tinto.jpg',NULL,NULL),(103,5601012011920,'Papa Figos DOC Douro Vinho Branco','Continente','N/A','750ml',7.99,'€','NO','2023-10-25 15:38:20','pt','./img/Casa Ferreirinha Papa Figos Branco.jpg',NULL,NULL),(104,5601012011500,'Mateus Vinho Rosé','El Corte Inglés','N/A','750ml',4.49,'€','NO','2023-10-25 15:38:21','pt','./img/Mateus Rosé Original.jpg',NULL,NULL),(105,5601012001310,'Mateus Espumante Sparkling Rosé Bruto','El Corte Inglés','N/A','750ml',6.99,'€','NO','2023-10-25 15:38:21','pt','./img/Mateus Sparkling Rosé.jpg',NULL,NULL),(106,5601012004427,'Trinca Bolotas Vinho Tinto Regional do Alentejo','El Corte Inglés','N/A','750ml',6.99,'€','NO','2023-10-25 15:38:22','pt','./img/Herdade do Peso Trinca Bolotas Tinto.jpg',NULL,NULL),(107,5601012011920,'Papa Figos Vinho Branco do Douro','El Corte Inglés','N/A','750ml',7.99,'€','NO','2023-10-25 15:38:23','pt','./img/Casa Ferreirinha Papa Figos Branco.jpg',NULL,NULL),(108,5601012011500,'Vinho Rosé Mateus','Garrafeira Soares','N/A','750ml',3.59,'€','NO','2023-10-25 15:38:24','pt','./img/Mateus Rosé Original.jpg',NULL,NULL),(109,5601012001310,'Espumante Mateus Rosé','Garrafeira Soares','N/A','750ml',6.69,'€','NO','2023-10-25 15:38:24','pt','./img/Mateus Sparkling Rosé.jpg',NULL,NULL),(110,5601012004427,'Vinho Tinto Trinca Bolotas','Garrafeira Soares','N/A','750ml',6.19,'€','NO','2023-10-25 15:38:24','pt','./img/Herdade do Peso Trinca Bolotas Tinto.jpg',NULL,NULL),(111,5601012011920,'Vinho Branco Douro Papa Figos','Garrafeira Soares','N/A','750ml',7.29,'€','NO','2023-10-25 15:38:25','pt','./img/Casa Ferreirinha Papa Figos Branco.jpg',NULL,NULL),(112,5601012011500,'MATEUS Rosé vino rosado de Portugal','El Corte Inglés_Es','N/A','750ml',4.49,'€','NO','2023-10-25 15:38:26','es','./img/Mateus Rosé Original.jpg',NULL,NULL),(113,5601012004427,'TRINCA BOLOTAS vino tinto Alentejo de Portugal','El Corte Inglés_Es','N/A','750ml',7.02,'€','NO','2023-10-25 15:38:26','es','./img/Herdade do Peso Trinca Bolotas Tinto.jpg',NULL,NULL);
/*!40000 ALTER TABLE `wine` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-25 15:56:52
