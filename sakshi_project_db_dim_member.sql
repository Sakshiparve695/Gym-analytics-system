-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: sakshi_project_db
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `dim_member`
--

DROP TABLE IF EXISTS `dim_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dim_member` (
  `member_key` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  `member_name` varchar(100) NOT NULL,
  `age` int DEFAULT NULL,
  `city_key` int DEFAULT NULL,
  `plan_key` int DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `load_timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `source_system` varchar(50) DEFAULT 'GymPulse',
  PRIMARY KEY (`member_key`),
  UNIQUE KEY `member_id` (`member_id`),
  KEY `city_key` (`city_key`),
  KEY `plan_key` (`plan_key`),
  CONSTRAINT `dim_member_ibfk_1` FOREIGN KEY (`city_key`) REFERENCES `dim_city` (`city_key`),
  CONSTRAINT `dim_member_ibfk_2` FOREIGN KEY (`plan_key`) REFERENCES `dim_plan` (`plan_key`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dim_member`
--

LOCK TABLES `dim_member` WRITE;
/*!40000 ALTER TABLE `dim_member` DISABLE KEYS */;
INSERT INTO `dim_member` VALUES (1,1,'Sakshi',24,5,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(2,2,'Sakshi Parve',25,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(3,3,'Somnath',28,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(4,4,'Rahul Sharma',25,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(5,5,'Priya Patel',28,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(6,6,'Aman Verma',22,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(7,7,'Sneha Gupta',30,3,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(8,8,'Arjun Singh',27,3,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(9,9,'Neha Kulkarni',26,3,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(10,12,'Sakshi',23,3,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(11,13,'Meera Sharma',48,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(12,14,'Arjun Deshmukh',26,4,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(13,15,'Vihaan Verma',38,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(14,16,'Vivaan Deshmukh',52,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(15,17,'Meera Parve',50,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(16,18,'Meera Joshi',31,3,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(17,19,'Ananya Patel',55,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(18,20,'Vivaan Verma',41,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(19,21,'Rohan Joshi',32,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(20,22,'Sai Patil',26,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(21,23,'Aditya Parve',27,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(22,24,'Vivaan Kulkarni',37,3,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(23,25,'Karan Gupta',55,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(24,26,'Pooja Gupta',27,3,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(25,27,'Ishita Joshi',57,3,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(26,28,'Ananya Patel',45,4,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(27,29,'Aisha Deshmukh',27,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(28,30,'Pooja Gupta',24,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(29,31,'Diya Verma',22,2,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(30,32,'Arjun Patel',35,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(31,33,'Aisha Verma',39,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(32,34,'Vivaan Gupta',52,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(33,35,'Ananya Singh',56,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(34,36,'Diya Verma',53,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(35,37,'Karan Kulkarni',57,3,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(36,38,'Pooja Parve',59,3,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(37,39,'Aisha Patil',24,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(38,40,'Vihaan Patil',19,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(39,41,'Aarav Sharma',47,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(40,42,'Sakshi Deshmukh',53,5,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(41,43,'Aditya Joshi',55,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(42,44,'Vihaan Gupta',50,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(43,45,'Ishita Singh',52,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(44,46,'Riya Sharma',31,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(45,47,'Ishita Verma',25,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(46,48,'Diya Kulkarni',41,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(47,49,'Pooja Verma',33,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(48,50,'Sneha Deshmukh',52,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(49,51,'Krishna Sharma',52,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(50,52,'Riya Kulkarni',51,4,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(51,53,'Aditya Verma',22,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(52,54,'Diya Joshi',34,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(53,55,'Karan Sharma',19,5,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(54,56,'Diya Kulkarni',54,3,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(55,57,'Karan Deshmukh',58,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(56,58,'Vivaan Patel',25,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(57,59,'Karan Kulkarni',31,5,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(58,60,'Aarav Verma',39,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(59,61,'Ananya Sharma',22,3,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(60,62,'Aisha Parve',53,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(61,63,'Priya Deshmukh',44,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(62,64,'Diya Parve',21,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(63,65,'Rahul Patel',19,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(64,66,'Sakshi Sharma',22,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(65,67,'Vihaan Patil',46,2,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(66,68,'Vihaan Verma',31,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(67,69,'Rahul Patel',41,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(68,70,'Ishita Kulkarni',48,3,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(69,71,'Rohan Sharma',53,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(70,72,'Sneha Sharma',50,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(71,73,'Vivaan Singh',37,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(72,74,'Vihaan Verma',23,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(73,75,'Meera Sharma',21,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(74,76,'Ananya Patel',50,4,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(75,77,'Sneha Patel',28,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(76,78,'Sneha Patel',34,1,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(77,79,'Meera Joshi',26,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(78,80,'Pooja Verma',24,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(79,81,'Diya Patel',47,4,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(80,82,'Rahul Kulkarni',38,5,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(81,83,'Sneha Patel',27,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(82,84,'Sai Kulkarni',44,2,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(83,85,'Rahul Patil',42,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(84,86,'Sneha Patel',49,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(85,87,'Vihaan Parve',51,3,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(86,88,'Sneha Gupta',53,2,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(87,89,'Karan Singh',21,3,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(88,90,'Vivaan Joshi',25,2,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(89,91,'Vihaan Joshi',45,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(90,92,'Vihaan Joshi',28,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(91,93,'Aisha Kulkarni',54,4,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(92,94,'Vivaan Parve',51,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(93,95,'Aditya Verma',26,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(94,96,'Aditya Parve',52,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(95,97,'Diya Verma',18,4,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(96,98,'Priya Deshmukh',46,3,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(97,99,'Krishna Joshi',30,4,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(98,100,'Arjun Kulkarni',18,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(99,101,'Karan Singh',23,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(100,102,'Riya Verma',27,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(101,103,'Ananya Patel',48,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(102,104,'Vivaan Patil',25,4,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(103,105,'Priya Deshmukh',29,2,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(104,106,'Meera Singh',37,2,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(105,107,'Aditya Singh',44,5,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(106,108,'Priya Patil',34,3,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(107,109,'Karan Deshmukh',57,1,3,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(108,110,'Karan Verma',22,5,1,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(109,111,'Meera Kulkarni',45,4,2,'2026-07-16','2026-07-16 17:17:22','GymPulse'),(110,112,'Sneha Deshmukh',18,1,1,'2026-07-16','2026-07-16 17:17:22','GymPulse');
/*!40000 ALTER TABLE `dim_member` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-21 23:00:10
