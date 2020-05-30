CREATE DATABASE  IF NOT EXISTS `bot_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bot_db`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bot_db
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `bot_addreses`
--

DROP TABLE IF EXISTS `bot_addreses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_addreses` (
  `ID` int DEFAULT NULL,
  `NAME` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_addreses`
--

LOCK TABLES `bot_addreses` WRITE;
/*!40000 ALTER TABLE `bot_addreses` DISABLE KEYS */;
INSERT INTO `bot_addreses` VALUES (1,'Парковая 22'),(2,'Заводская 7'),(3,'Набережная 50'),(4,'Набережная 46'),(5,'Парковая 16'),(6,'Парковая 18'),(7,'Парковая 48'),(8,'Парковая 52'),(9,'Парковая 46'),(10,'Парковая 44'),(11,'Набережная 71'),(12,'Набережная 73'),(13,'Набережная 74'),(14,'Набережная 75'),(15,'Парковая 62'),(16,'Парковая 54'),(17,'Парковая 66'),(18,'Парковая 68'),(19,'Парковая 17'),(20,'Молодёжная 4'),(21,'Парковая 19'),(22,'Молодёжная 2'),(23,'Заводская 3'),(24,'Парковая 15'),(25,'Парковая 13'),(26,'Парковая 3'),(27,'Парковая 11'),(28,'Парковая 7'),(29,'Парковая 9'),(30,'Парковая 8'),(31,'Парковая 10'),(32,'Набережная 40'),(33,'Парковая 14'),(34,'Парковая 2'),(35,'Парковая 4'),(36,'Энергетиков 14'),(37,'Энергетиков 10'),(38,'Энергетиков 8'),(39,'Энергетиков 12'),(40,'Набережная 38'),(41,'Набережная 34'),(42,'Набережная 30'),(43,'Набережная 26'),(44,'Энергетиков 4'),(45,'Ленина 20'),(46,'Строителей 2А'),(47,'Строителей 2Б'),(48,'Мира 58'),(49,'Мира 60'),(50,'Строителей 6'),(51,'Строителей 6Б'),(52,'Строителей 5А'),(53,'Мира 56А'),(54,'Ленина 12'),(55,'Ленина 8'),(56,'Ленина 4'),(57,'Ленина 2'),(58,'Энергетиков 1Б'),(59,'Энергетиков 1А'),(60,'Энергетиков 3А'),(61,'Энергетиков 3'),(62,'Заводская 10А'),(63,'Заводская 10'),(64,'Энергетиков 5'),(65,'Энергетиков 1'),(66,'Мира 65'),(67,'Мира 47'),(68,'Мира 63'),(69,'Первомайская 11'),(70,'Дзержинского 6'),(71,'Мира 57'),(72,'Дзержинского 2'),(73,'Мира 59'),(74,'Мира 43А'),(75,'Первомайская 13'),(76,'Калинина 9А'),(77,'Первомайская 14'),(78,'Мира 61'),(79,'Мира 45'),(80,'Первомайская 12В'),(81,'Калинина 13Б'),(82,'Калинина 13'),(83,'Первомайская 12А'),(84,'Комсомольская 24'),(85,'Мира 53'),(86,'Калинина 13А'),(87,'Калинина 11'),(88,'Калинина 9'),(89,'Калинина 3'),(90,'Калинина 11А'),(91,'Комсомольская 34А'),(92,'Комсомольская 30Б'),(93,'Калинина 5'),(94,'Первомайская 8'),(95,'Комсомольская 28'),(96,'Калинина 7А'),(97,'Комсомольская 36'),(98,'Первомайская 8Б'),(99,'Комсомольская 26'),(100,'Калинина 7'),(101,'Комсомольская 30'),(102,'Калинина 7Б'),(103,'Комсомольская 34'),(104,'Комсомольская 38'),(105,'Калинина 7В'),(106,'Заводская 4'),(107,'Заводская 6'),(108,'Первомайская 8В'),(109,'Комсомольская 34Б'),(110,'Комсомольская 30А'),(111,'Заводская 8'),(112,'Мира 51'),(113,'Мира 49'),(114,'Мира 41А'),(115,'Первомайская 16'),(116,'Калинина 15'),(117,'Первомайская 12Б'),(118,'Мира 43'),(119,'Мира 39А'),(120,'Калинина 17'),(121,'Мира 33'),(122,'Мира 39'),(123,'Мира 35'),(124,'Мира 37'),(125,'Калинина 13В'),(126,'Мира 43Б'),(127,'Мира 39Б'),(128,'Мира 46'),(129,'Мира 48'),(130,'Мира 50'),(131,'Гагарина 27'),(132,'Мира 44'),(133,'Гагарина 25'),(134,'Молодёжная 9'),(135,'Гагарина 17'),(136,'Мира 38'),(137,'Молодёжная 7'),(138,'Мира 36'),(139,'Калинина 23'),(140,'Молодёжная 3'),(141,'Молодёжная 5'),(142,'Мира 34'),(143,'Калинина 19'),(144,'Строителей 10'),(145,'Калинина 6'),(146,'Калинина 12'),(147,'Калинина 4'),(148,'Мира 27'),(149,'Мира 25'),(150,'Калинина 10'),(151,'Мира 19'),(152,'Мира 27А'),(153,'Мира 21А'),(154,'Мира 29'),(155,'Мира 23'),(156,'Мира 21'),(157,'Набережная 6А'),(158,'Комсомольская 8А'),(159,'Советская 1'),(160,'Советская 3'),(161,'Советская 7'),(162,'Комсомольская 10Б'),(163,'Комсомольская 10А'),(164,'Комсомольская 6'),(165,'Комсомольская 14'),(166,'Комсомольская 12'),(167,'Советская 6Б'),(168,'Мира 3'),(169,'Мира 11'),(170,'Набережная 2Б'),(171,'Набережная 4А'),(172,'Советская 4'),(173,'Советская 4А'),(174,'Советская 10'),(175,'Советская 2'),(176,'Комсомольская 14А'),(177,'Набережная 6'),(178,'Набережная 2'),(179,'Комсомольская 10'),(180,'Комсомольская 4'),(181,'Набережная 1'),(182,'Набережная 2А'),(183,'Советская 8'),(184,'Советская 8А'),(185,'Комсомольская 12А'),(186,'Ленина 13'),(187,'Ленина 23'),(188,'Ленина 39'),(189,'Ленина 5'),(190,'Ленина 31'),(191,'Строителей 4'),(192,'Бортникова 36'),(193,'Бортникова 44'),(194,'Строителей 17'),(195,'Бортникова 20'),(196,'Бортникова 30'),(197,'Бортникова 26'),(198,'Строителей 21А'),(199,'Бортникова 22'),(200,'Строителей 5'),(201,'Строителей 6А'),(202,'Строителей 9'),(203,'Строителей 15'),(204,'Строителей 13'),(205,'Строителей 7'),(206,'Строителей 25'),(207,'Бортникова 46'),(208,'Бортникова 18'),(209,'Строителей 14'),(210,'Строителей 16'),(211,'Строителей 18'),(212,'Строителей 20'),(213,'Строителей 24'),(214,'Песчаная 3'),(215,'Набережная 16'),(216,'Ленина 3'),(217,'Ленина 7'),(218,'Набережная 18'),(219,'Ленина 15'),(220,'Ленина 19'),(221,'Ленина 11'),(222,'Бортникова 2'),(223,'Ленина 21'),(224,'Мира 10Б'),(225,'Бортникова 12'),(226,'Ленина 35'),(227,'Бортникова 8'),(228,'Ленина 37'),(229,'Мира 10В'),(230,'Мира 4А'),(231,'Ленина 27'),(232,'Мира 8А'),(233,'Мира 4'),(234,'Мира 8'),(235,'Набережная 12'),(236,'Набережная 10'),(237,'Бортникова 10'),(238,'Бортникова 4'),(239,'Мира 10А'),(240,'Мира 8Б'),(241,'Ленина 9'),(242,'Набережная 12А'),(243,'Ленина 25'),(244,'Набережная 10А'),(245,'Набережная 16А'),(246,'Бортникова 7'),(247,'Гагарина 7'),(248,'Бортникова 11'),(249,'Гагарина 3'),(250,'Бортникова 5'),(251,'Гагарина 9'),(252,'Гагарина 1'),(253,'Мира 18А'),(254,'Гагарина 15'),(255,'Мира 16А'),(256,'Мира 20А'),(257,'Калинина 20'),(258,'Гагарина 13'),(259,'Мира 20'),(260,'Мира 16'),(261,'Мира 18'),(262,'Мира 24'),(263,'Мира 28'),(264,'Мира 24А'),(265,'Мира 26'),(266,'Калинина 18'),(267,'Бортникова 15'),(268,'Бортникова 21'),(269,'Бортникова 19'),(270,'Бортникова 16'),(271,'Строителей 11'),(272,'Строителей 27'),(273,'Строителей 23'),(274,'Бортникова 48'),(275,'Строителей 21'),(276,'Бортникова 38'),(277,'Бортникова 42'),(278,'Бортникова 32'),(279,'Первомайская 12'),(280,'Первомайская 14А'),(281,'Первомайская 2'),(282,'Первомайская 6'),(283,'Первомайская 4'),(284,'Первомайская 10А'),(285,'Гагарина 20'),(286,'Гагарина 24'),(287,'Гагарина 22'),(288,'Гагарина 16'),(289,'Набережная 66'),(290,'Набережная 70'),(291,'Набережная 72'),(292,'Набережная 68'),(293,'Набережная 52'),(294,'Парковая 32'),(295,'Парковая 38'),(296,'Парковая 28'),(297,'Парковая 34'),(298,'Мира 55'),(299,'Дзержинского 6А'),(300,'Мира 75'),(301,'Дзержинского 14'),(302,'Дзержинского 12'),(303,'Дзержинского 10'),(304,'Мира 67'),(305,'Мира 73'),(306,'Мира 62'),(307,'Лазо 2А'),(308,'Дзержинского 8'),(309,'Дзержинского 16'),(310,'Набережная 48'),(311,'Строителей 3'),(312,'Парковая 64'),(313,'Парковая 58'),(314,'Парковая 56'),(315,'Парковая 60'),(316,'Набережная 78'),(317,'Набережная 76'),(318,'Мира 69'),(319,'Советская 6'),(320,'Набережная 58'),(321,'Набережная 8'),(322,'Парковая 26'),(323,'Калинина 17А'),(324,'Парковая 72'),(325,'Парковая 74'),(326,'Энергетиков 2'),(327,'Бортникова 9'),(328,'Строителей 8');
/*!40000 ALTER TABLE `bot_addreses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_admins`
--

DROP TABLE IF EXISTS `bot_admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_admins` (
  `ID` int DEFAULT NULL,
  `Name` text,
  `TelegrammID` int DEFAULT NULL,
  `OrgID` int DEFAULT NULL,
  `RulesID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_admins`
--

LOCK TABLES `bot_admins` WRITE;
/*!40000 ALTER TABLE `bot_admins` DISABLE KEYS */;
INSERT INTO `bot_admins` VALUES (1,'admin',0,1,1);
/*!40000 ALTER TABLE `bot_admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_elog`
--

DROP TABLE IF EXISTS `bot_elog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_elog` (
  `ID` int DEFAULT NULL,
  `EventID` int DEFAULT NULL,
  `OperatorID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_elog`
--

LOCK TABLES `bot_elog` WRITE;
/*!40000 ALTER TABLE `bot_elog` DISABLE KEYS */;
/*!40000 ALTER TABLE `bot_elog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_estatus`
--

DROP TABLE IF EXISTS `bot_estatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_estatus` (
  `Id` int DEFAULT NULL,
  `Name` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_estatus`
--

LOCK TABLES `bot_estatus` WRITE;
/*!40000 ALTER TABLE `bot_estatus` DISABLE KEYS */;
INSERT INTO `bot_estatus` VALUES (1,'Выполняется');
/*!40000 ALTER TABLE `bot_estatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_etimer`
--

DROP TABLE IF EXISTS `bot_etimer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_etimer` (
  `ID` int DEFAULT NULL,
  `Name` text,
  `StartTime` datetime DEFAULT NULL,
  `StopTime` datetime DEFAULT NULL,
  `SendTime` datetime DEFAULT NULL,
  `Repeat` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_etimer`
--

LOCK TABLES `bot_etimer` WRITE;
/*!40000 ALTER TABLE `bot_etimer` DISABLE KEYS */;
INSERT INTO `bot_etimer` VALUES (1,'Сутки','2020-05-31 12:00:05','2020-05-31 13:04:16','2020-05-30 13:04:22',0);
/*!40000 ALTER TABLE `bot_etimer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_events`
--

DROP TABLE IF EXISTS `bot_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_events` (
  `ID` int DEFAULT NULL,
  `Name` text,
  `UserID` int DEFAULT NULL,
  `EventID` int DEFAULT NULL,
  `TimerID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_events`
--

LOCK TABLES `bot_events` WRITE;
/*!40000 ALTER TABLE `bot_events` DISABLE KEYS */;
INSERT INTO `bot_events` VALUES (1,'Обычная подписка',1,1,1);
/*!40000 ALTER TABLE `bot_events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_eweight`
--

DROP TABLE IF EXISTS `bot_eweight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_eweight` (
  `Id` int DEFAULT NULL,
  `Name` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_eweight`
--

LOCK TABLES `bot_eweight` WRITE;
/*!40000 ALTER TABLE `bot_eweight` DISABLE KEYS */;
INSERT INTO `bot_eweight` VALUES (1,'Важное');
/*!40000 ALTER TABLE `bot_eweight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_idevents`
--

DROP TABLE IF EXISTS `bot_idevents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_idevents` (
  `Id` int DEFAULT NULL,
  `Name` text,
  `AlertID` int DEFAULT NULL,
  `StatusID` int DEFAULT NULL,
  `AdrID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_idevents`
--

LOCK TABLES `bot_idevents` WRITE;
/*!40000 ALTER TABLE `bot_idevents` DISABLE KEYS */;
INSERT INTO `bot_idevents` VALUES (1,'Отключение воды',1,1,1);
/*!40000 ALTER TABLE `bot_idevents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_msglog`
--

DROP TABLE IF EXISTS `bot_msglog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_msglog` (
  `ID` int NOT NULL,
  `UserID` int DEFAULT NULL,
  `MagText` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_msglog`
--

LOCK TABLES `bot_msglog` WRITE;
/*!40000 ALTER TABLE `bot_msglog` DISABLE KEYS */;
/*!40000 ALTER TABLE `bot_msglog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_org`
--

DROP TABLE IF EXISTS `bot_org`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_org` (
  `Id` int DEFAULT NULL,
  `Name` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_org`
--

LOCK TABLES `bot_org` WRITE;
/*!40000 ALTER TABLE `bot_org` DISABLE KEYS */;
/*!40000 ALTER TABLE `bot_org` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_rules`
--

DROP TABLE IF EXISTS `bot_rules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_rules` (
  `Id` int DEFAULT NULL,
  `EventId` int DEFAULT NULL,
  `OrgID` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_rules`
--

LOCK TABLES `bot_rules` WRITE;
/*!40000 ALTER TABLE `bot_rules` DISABLE KEYS */;
/*!40000 ALTER TABLE `bot_rules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bot_users`
--

DROP TABLE IF EXISTS `bot_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_users` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` text,
  `TelegrammID` int DEFAULT NULL,
  `AddressID` int DEFAULT NULL,
  `Subscribe` tinyint(1) DEFAULT '0',
  `Phone` text,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `bot_users_TelegrammID_uindex` (`TelegrammID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_users`
--

LOCK TABLES `bot_users` WRITE;
/*!40000 ALTER TABLE `bot_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `bot_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-30 14:48:05
