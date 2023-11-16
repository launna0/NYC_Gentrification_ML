CREATE DATABASE  IF NOT EXISTS `gentrification` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gentrification`;
-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: gentrification
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `neighborhoodDemographics`
--

DROP TABLE IF EXISTS `neighborhoodDemographics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `neighborhoodDemographics` (
  `borough` text,
  `neighborhood` varchar(36) NOT NULL,
  `year` int NOT NULL,
  `disability_prop` float DEFAULT NULL,
  `population` int DEFAULT NULL,
  `asian_prop` float DEFAULT NULL,
  `black_prop` float DEFAULT NULL,
  `hispanic_prop` float DEFAULT NULL,
  `white_prop` float DEFAULT NULL,
  `diversity_index` float DEFAULT NULL,
  `median_household_inc` float DEFAULT NULL,
  `poverty_prop` float DEFAULT NULL,
  `nohsdiploma_prop` float DEFAULT NULL,
  `unemployment_prop` float DEFAULT NULL,
  `singleunitbuilding_price` int DEFAULT NULL,
  `condo_price` int DEFAULT NULL,
  PRIMARY KEY (`neighborhood`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `neighborhoodDemographics`
--

LOCK TABLES `neighborhoodDemographics` WRITE;
/*!40000 ALTER TABLE `neighborhoodDemographics` DISABLE KEYS */;
INSERT INTO `neighborhoodDemographics` VALUES ('Queens','Astoria',2010,0.058,166666,0.145,0.069,0.292,0.466,0.67,56460,0.19,0.194,0.13,667460,430810),('Queens','Astoria',2019,0.057,166069,0.147,0.052,0.274,0.495,0.66,83200,0.116,0.115,0.0337,978590,650460),('Brooklyn','Bay Ridge',2010,0.065,137599,0.248,0.008,0.14,0.568,0.6,58700,0.153,0.23,0.0915,788810,436880),('Brooklyn','Bay Ridge',2019,0.056,121925,0.236,0.021,0.178,0.536,0.63,80460,0.142,0.159,0.0359,1029810,683040),('Bronx','Baychester',2010,0.1,137233,0.018,0.64,0.25,0.076,0.52,53370,0.212,0.206,0.1582,394710,317460),('Bronx','Baychester',2019,0.103,149128,0.016,0.602,0.282,0.057,0.55,63290,0.171,0.187,0.0827,483380,130830),('Queens','Bayside',2010,0.05,120428,0.382,0.009,0.128,0.462,0.62,85550,0.073,0.107,0.0965,764540,540030),('Queens','Bayside',2019,0.068,114562,0.411,0.06,0.134,0.379,0.67,97390,0.064,0.131,0.0389,945750,686600),('Bronx','Bedford',2010,0.109,124826,0.05,0.207,0.66,0.072,0.51,33030,0.327,0.356,0.1762,322560,439920),('Bronx','Bedford',2019,0.081,151684,0.065,0.127,0.732,0.062,0.44,43440,0.226,0.317,0.1173,630500,262710),('Brooklyn','Bedford Stuyvesant',2010,0.079,133302,0.039,0.601,0.2,0.146,0.58,44880,0.307,0.236,0.1282,396830,443610),('Brooklyn','Bedford Stuyvesant',2019,0.074,144306,0.03,0.456,0.195,0.294,0.67,64300,0.23,0.147,0.0663,1077100,753290),('Bronx','Belmont',2010,0.152,160651,0.007,0.302,0.636,0.041,0.5,24970,0.435,0.401,0.1709,355330,354970),('Bronx','Belmont',2019,0.184,172930,0.006,0.361,0.589,0.032,0.52,24800,0.403,0.324,0.1149,408250,254830),('Brooklyn','Bensonhurst',2010,0.061,164506,0.337,0.001,0.134,0.507,0.61,46410,0.14,0.301,0.086,685660,502060),('Brooklyn','Bensonhurst',2019,0.058,186959,0.41,0.011,0.16,0.384,0.66,60040,0.146,0.25,0.0453,903710,604230),('Brooklyn','Borough Park',2010,0.081,168915,0.163,0.015,0.1,0.71,0.46,43860,0.322,0.273,0.0805,697800,542670),('Brooklyn','Borough Park',2019,0.046,153470,0.127,0.015,0.105,0.721,0.45,57870,0.268,0.212,0.0399,1261000,802510),('Queens','Broad Channel',2010,0.09,124031,0.01,0.379,0.235,0.358,0.67,58160,0.224,0.219,0.1424,505910,460230),('Queens','Broad Channel',2019,0.159,121740,0.027,0.374,0.26,0.323,0.69,57830,0.181,0.206,0.0627,567450,367790),('Bronx','Bronxdale',2010,0.091,123655,0.09,0.198,0.424,0.266,0.7,52930,0.211,0.246,0.1385,466310,220870),('Bronx','Bronxdale',2019,0.114,125155,0.098,0.234,0.474,0.166,0.68,61160,0.146,0.191,0.0809,577430,262710),('Brooklyn','Brooklyn Heights',2010,0.069,125468,0.066,0.3,0.167,0.427,0.7,87120,0.181,0.127,0.1038,2709270,741420),('Brooklyn','Brooklyn Heights',2019,0.06,133346,0.113,0.203,0.123,0.521,0.66,117220,0.138,0.093,0.0631,3467740,1313540),('Brooklyn','Brownsville',2010,0.105,115433,0.004,0.74,0.246,0.004,0.39,31840,0.398,0.277,0.1558,345860,395620),('Brooklyn','Brownsville',2019,0.117,128369,0.009,0.684,0.256,0.038,0.47,32940,0.343,0.239,0.0762,498330,520160),('Brooklyn','Bushwick',2010,0.067,140437,0.029,0.193,0.684,0.09,0.49,44960,0.285,0.394,0.1022,294290,358000),('Brooklyn','Bushwick',2019,0.052,127550,0.042,0.153,0.563,0.206,0.61,69640,0.207,0.224,0.0632,914220,620300),('Brooklyn','Canarsie',2010,0.049,202929,0.037,0.617,0.082,0.249,0.55,71390,0.114,0.126,0.0829,513340,436880),('Brooklyn','Canarsie',2019,0.052,196895,0.054,0.625,0.091,0.214,0.55,84560,0.106,0.121,0.0323,646260,420330),('Brooklyn','Carroll Gardens',2010,0.046,119558,0.06,0.086,0.198,0.622,0.56,100650,0.113,0.095,0.0788,1813670,762970),('Brooklyn','Carroll Gardens',2019,0.031,114043,0.085,0.085,0.105,0.678,0.52,163140,0.076,0.054,0.0341,2649540,1434380),('Manhattan','Central Harlem',2010,0.118,126558,0.035,0.586,0.236,0.118,0.59,42880,0.281,0.211,0.1588,1941700,729070),('Manhattan','Central Harlem',2019,0.106,136351,0.036,0.543,0.236,0.155,0.62,57720,0.201,0.139,0.0869,2343350,979900),('Manhattan','Chelsea',2010,0.047,134471,0.139,0.063,0.126,0.636,0.56,94470,0.117,0.077,0.0829,3488990,1334920),('Manhattan','Chelsea',2019,0.064,167290,0.158,0.046,0.174,0.586,0.6,126360,0.111,0.069,0.0264,2545000,2206740),('Manhattan','Chinatown',2010,0.062,159009,0.347,0.064,0.229,0.337,0.71,51350,0.222,0.266,0.101,3762040,1092200),('Manhattan','Chinatown',2019,0.071,167128,0.328,0.076,0.254,0.303,0.73,43400,0.24,0.288,0.0524,8038850,1596210),('Manhattan','Clinton',2010,0.047,134471,0.139,0.063,0.126,0.636,0.56,94470,0.117,0.077,0.0829,3488990,1334920),('Manhattan','Clinton',2019,0.064,167290,0.158,0.046,0.174,0.586,0.6,126360,0.111,0.069,0.0264,2545000,2206740),('Bronx','Co-op City',2010,0.086,109482,0.02,0.275,0.311,0.377,0.69,57310,0.164,0.196,0.1074,473290,367100),('Bronx','Co-op City',2019,0.16,110883,0.038,0.22,0.439,0.278,0.68,64130,0.129,0.201,0.045,551690,440820),('Bronx','Concourse',2010,0.146,146624,0.017,0.328,0.638,0.005,0.49,32440,0.35,0.391,0.1572,523820,242710),('Bronx','Concourse',2019,0.132,140906,0.013,0.327,0.608,0.038,0.52,34210,0.324,0.277,0.0957,543800,173390),('Brooklyn','Coney Island',2010,0.07,103112,0.146,0.122,0.125,0.593,0.6,35330,0.28,0.177,0.1439,479360,605570),('Brooklyn','Coney Island',2019,0.079,115277,0.164,0.11,0.147,0.535,0.65,42780,0.256,0.186,0.0441,607380,577960),('Queens','Corona',2010,0.057,136517,0.353,0.065,0.475,0.081,0.64,50110,0.192,0.3,0.0846,637120,352550),('Queens','Corona',2019,0.054,156074,0.353,0.037,0.535,0.053,0.58,70560,0.102,0.247,0.0355,861680,503650),('Bronx','Crotona',2010,0.152,160651,0.007,0.302,0.636,0.041,0.5,24970,0.435,0.401,0.1709,337370,281790),('Bronx','Crotona',2019,0.184,172930,0.006,0.361,0.589,0.032,0.52,24800,0.403,0.324,0.1149,439460,317880),('Brooklyn','Crown Heights',2010,0.05,119323,0.033,0.616,0.137,0.19,0.56,46810,0.259,0.161,0.1009,423530,528590),('Brooklyn','Crown Heights',2019,0.07,128327,0.032,0.488,0.141,0.308,0.65,78210,0.159,0.111,0.0412,1576240,1195320),('Brooklyn','Dyker Heights',2010,0.065,137599,0.248,0.008,0.14,0.568,0.6,58700,0.153,0.23,0.0915,788810,436880),('Brooklyn','Dyker Heights',2019,0.056,121925,0.236,0.021,0.178,0.536,0.63,80460,0.142,0.159,0.0359,1029810,683040),('Brooklyn','East Flatbush',2010,0.061,140285,0.008,0.892,0.075,0.011,0.2,52580,0.154,0.151,0.1277,412610,367570),('Brooklyn','East Flatbush',2019,0.055,136009,0.023,0.858,0.076,0.025,0.26,63990,0.099,0.141,0.0501,609480,567450),('Manhattan','East Harlem',2010,0.098,114525,0.07,0.321,0.462,0.133,0.66,37100,0.308,0.276,0.1477,121360,529110),('Manhattan','East Harlem',2019,0.125,111452,0.052,0.359,0.43,0.14,0.66,34060,0.34,0.235,0.0608,1628790,862430),('Brooklyn','East New York',2010,0.068,146614,0.029,0.547,0.369,0.047,0.56,38310,0.36,0.252,0.1229,349630,238320),('Brooklyn','East New York',2019,0.088,180811,0.04,0.554,0.349,0.042,0.57,48330,0.233,0.159,0.0385,504400,341520),('Bronx','East Tremont',2010,0.152,160651,0.007,0.302,0.636,0.041,0.5,24970,0.435,0.401,0.1709,355330,354970),('Bronx','East Tremont',2019,0.184,172930,0.006,0.361,0.589,0.032,0.52,24800,0.403,0.324,0.1149,408250,254830),('Queens','Elmhurst',2010,0.057,136517,0.353,0.065,0.475,0.081,0.64,50110,0.192,0.3,0.0846,637120,352550),('Queens','Elmhurst',2019,0.054,156074,0.353,0.037,0.535,0.053,0.58,70560,0.102,0.247,0.0355,861680,503650),('Bronx','Fieldston',2010,0.071,109153,0.052,0.133,0.423,0.377,0.66,60730,0.185,0.152,0.1396,743310,596820),('Bronx','Fieldston',2019,0.079,104149,0.044,0.091,0.513,0.312,0.63,64360,0.165,0.189,0.0562,904760,709310),('Manhattant','Financial District',2010,0.031,144944,0.146,0.024,0.056,0.732,0.44,123930,0.099,0.052,0.0608,15542670,1246930),('Manhattan','Financial District',2019,0.029,164514,0.138,0.034,0.114,0.684,0.5,170330,0.061,0.029,0.0432,5201610,2180470),('Brooklyn','Flatbush',2010,0.057,162715,0.081,0.349,0.127,0.42,0.68,52270,0.224,0.173,0.1112,910170,479360),('Brooklyn','Flatbush',2019,0.052,156866,0.095,0.336,0.138,0.398,0.7,68930,0.12,0.136,0.0362,1132270,636650),('Brooklyn','Flatlands',2010,0.049,202929,0.037,0.617,0.082,0.249,0.55,71390,0.114,0.126,0.0829,513340,436880),('Brooklyn','Flatlands',2019,0.052,196895,0.054,0.625,0.091,0.214,0.55,84560,0.106,0.121,0.0323,646260,420330),('Queens','Flushing',2010,0.056,257327,0.502,0.02,0.15,0.3,0.64,63230,0.143,0.199,0.1157,716000,447800),('Queens','Flushing',2019,0.046,239869,0.564,0.017,0.156,0.243,0.6,57730,0.148,0.219,0.0453,945750,662020),('Queens','Forest Hills',2010,0.053,114462,0.268,0.012,0.14,0.563,0.59,66910,0.097,0.086,0.0886,799130,407760),('Queens','Forest Hills',2019,0.079,105586,0.3,0.02,0.143,0.507,0.63,93690,0.111,0.056,0.0381,998290,727940),('Brooklyn','Fort Greene',2010,0.069,125468,0.066,0.3,0.167,0.427,0.7,87120,0.181,0.127,0.1038,2709270,741420),('Brooklyn','Fort Greene',2019,0.06,133346,0.113,0.203,0.123,0.521,0.66,117220,0.138,0.093,0.0631,3467740,1313540),('Queens','Fresh Meadows',2010,0.077,138004,0.3,0.126,0.205,0.328,0.74,67030,0.137,0.133,0.1272,656380,364070),('Queens','Fresh Meadows',2019,0.066,168471,0.309,0.156,0.211,0.271,0.76,75830,0.115,0.131,0.055,898460,504400),('Staten Island','Great Kills',2010,0.065,164809,0.033,0.013,0.111,0.834,0.29,99120,0.07,0.091,0.0872,508480,339800),('Staten Island','Great Kills',2019,0.065,161358,0.06,0.008,0.107,0.818,0.32,113520,0.041,0.055,0.0305,583210,387760),('Brooklyn','Greenpoint',2010,0.05,146253,0.052,0.026,0.3,0.607,0.54,50820,0.265,0.211,0.082,821580,615280),('Brooklyn','Greenpoint',2019,0.049,151308,0.066,0.045,0.25,0.613,0.56,103280,0.201,0.155,0.0399,1655060,1119130),('Manhattan','Greenwich Village',2010,0.031,144944,0.146,0.024,0.056,0.732,0.44,123930,0.099,0.052,0.0608,8270410,2111600),('Manhattan','Greenwich Village',2019,0.029,164514,0.138,0.034,0.114,0.684,0.5,170330,0.061,0.029,0.0432,11033710,2766310),('Manhattan','Hamilton',2010,0.097,138048,0.074,0.201,0.406,0.275,0.71,45230,0.287,0.217,0.0943,1456270,430690),('Manhattan','Hamilton',2019,0.076,132837,0.089,0.152,0.37,0.357,0.7,71850,0.196,0.184,0.0679,3021140,740510),('Bronx','Highbridge',2010,0.146,146624,0.017,0.328,0.638,0.005,0.49,32440,0.35,0.391,0.1572,523820,242710),('Bronx','Highbridge',2019,0.132,140906,0.013,0.327,0.608,0.038,0.52,34210,0.324,0.277,0.0957,543800,173390),('Queens','Hillcrest',2010,0.077,138004,0.3,0.126,0.205,0.328,0.74,67030,0.137,0.133,0.1272,656380,364070),('Queens','Hillcrest',2019,0.066,168471,0.309,0.156,0.211,0.271,0.76,75830,0.115,0.131,0.055,898460,504400),('Queens','Hollis',2010,0.086,222074,0.092,0.625,0.214,0.016,0.55,60400,0.188,0.211,0.1549,340710,332310),('Queens','Hollis',2019,0.068,241275,0.142,0.586,0.18,0.023,0.6,69090,0.106,0.17,0.0663,526010,306320),('Queens','Howard Beach',2010,0.064,135257,0.188,0.13,0.229,0.254,0.83,68330,0.116,0.241,0.1015,424750,271990),('Queens','Howard Beach',2019,0.089,118568,0.264,0.148,0.249,0.238,0.79,88540,0.075,0.169,0.0449,609480,357280),('Bronx','Hunts Point',2010,0.184,156790,0.01,0.292,0.668,0.02,0.47,25300,0.411,0.431,0.1904,186280,270770),('Bronx','Hunts Point',2019,0.182,146824,0.005,0.277,0.683,0.026,0.46,26350,0.396,0.298,0.1129,493890,223300),('Manhattan','Inwood',2010,0.083,205414,0.02,0.074,0.702,0.189,0.47,49960,0.195,0.333,0.1359,409880,442950),('Queens','Jackson Heights',2010,0.077,170161,0.166,0.062,0.646,0.105,0.54,54470,0.224,0.293,0.1034,521830,341010),('Queens','Jackson Heights',2019,0.086,175275,0.189,0.04,0.649,0.107,0.53,70620,0.15,0.269,0.044,809140,502600),('Queens','Jamaica',2010,0.086,222074,0.092,0.625,0.214,0.016,0.55,60400,0.188,0.211,0.1549,340710,332310),('Queens','Jamaica',2019,0.068,241275,0.142,0.586,0.18,0.023,0.6,69090,0.106,0.17,0.0663,526010,306320),('Queens','Kew Gardens',2010,0.065,135589,0.228,0.094,0.411,0.186,0.74,69360,0.131,0.186,0.1327,406540,392420),('Queens','Kew Gardens',2019,0.079,143756,0.276,0.07,0.394,0.168,0.74,80890,0.101,0.198,0.052,619990,419280),('Bronx','Kingsbridge Heights',2010,0.109,124826,0.05,0.207,0.66,0.072,0.51,33030,0.327,0.356,0.1762,322560,439920),('Bronx','Kingsbridge Heights',2019,0.081,151684,0.065,0.127,0.732,0.062,0.44,43440,0.226,0.317,0.1173,630500,262710),('Brooklyn','Lefferts Gardens',2010,0.07,107419,0.018,0.752,0.065,0.149,0.41,47080,0.256,0.183,0.202,746340,508050),('Brooklyn','Lefferts Gardens',2019,0.045,106258,0.021,0.572,0.122,0.253,0.59,70090,0.179,0.111,0.0446,1366080,651510),('Queens','Little Neck',2010,0.05,120428,0.382,0.009,0.128,0.462,0.62,85550,0.073,0.107,0.0965,764540,540030),('Queens','Little Neck',2019,0.068,114562,0.411,0.06,0.134,0.379,0.67,97390,0.064,0.131,0.0389,945750,686600),('Bronx','Longwood',2010,0.184,156790,0.01,0.292,0.668,0.02,0.47,25300,0.411,0.431,0.1904,186280,270770),('Bronx','Longwood',2019,0.182,146824,0.005,0.277,0.683,0.026,0.46,26350,0.396,0.298,0.1129,493890,223300),('Manhattan','Lower East Side',2010,0.062,159009,0.347,0.064,0.229,0.337,0.71,51350,0.222,0.266,0.101,3762040,1092200),('Manhattan','Lower East Side',2019,0.071,167128,0.328,0.076,0.254,0.303,0.73,43400,0.24,0.288,0.0524,8038850,1596210),('Queens','Maspeth',2010,0.059,180932,0.089,0.011,0.371,0.517,0.59,64630,0.171,0.221,0.0795,594640,414620),('Queens','Maspeth',2019,0.057,165895,0.088,0.022,0.356,0.52,0.59,76480,0.084,0.137,0.0314,766050,513860),('Bronx','Melrose',2010,0.184,156790,0.01,0.292,0.668,0.02,0.47,25300,0.411,0.431,0.1904,375500,263340),('Bronx','Melrose',2019,0.182,146824,0.005,0.277,0.683,0.026,0.46,26350,0.396,0.298,0.1129,483380,332060),('Brooklyn','Midwood',2010,0.057,162715,0.081,0.349,0.127,0.42,0.68,52270,0.224,0.173,0.1112,910170,479360),('Brooklyn','Midwood',2019,0.052,156866,0.095,0.336,0.138,0.398,0.7,68930,0.12,0.136,0.0362,1132270,636650),('Manhattan','Morningside Heights',2010,0.097,138048,0.074,0.201,0.406,0.275,0.71,45230,0.287,0.217,0.0943,1456270,430690),('Manhattan','Morningside Heights',2019,0.076,132837,0.089,0.152,0.37,0.357,0.7,71850,0.196,0.184,0.0679,3021140,740510),('Bronx','Morris Park',2010,0.091,123655,0.09,0.198,0.424,0.266,0.7,52930,0.211,0.246,0.1385,466310,220870),('Bronx','Morris Park',2019,0.114,125155,0.098,0.234,0.474,0.166,0.68,61160,0.146,0.191,0.0809,577430,262710),('Bronx','Morrisania',2010,0.152,160651,0.007,0.302,0.636,0.041,0.5,24970,0.435,0.401,0.1709,337370,281790),('Bronx','Morrisania',2019,0.184,172930,0.006,0.361,0.589,0.032,0.52,24800,0.403,0.324,0.1149,439460,317880),('Bronx','Mott Haven',2010,0.184,156790,0.01,0.292,0.668,0.02,0.47,25300,0.411,0.431,0.1904,375500,263340),('Bronx','Mott Haven',2019,0.182,146824,0.005,0.277,0.683,0.026,0.46,26350,0.396,0.298,0.1129,483380,332060),('Brooklyn','Park Slope',2010,0.046,119558,0.06,0.086,0.198,0.622,0.56,100650,0.113,0.095,0.0788,1813670,762970),('Brooklyn','Park Slope',2019,0.031,114043,0.085,0.085,0.105,0.678,0.52,163140,0.076,0.054,0.0341,2649540,1434380),('Bronx','Parkchester',2010,0.092,182977,0.071,0.32,0.562,0.024,0.58,47680,0.254,0.303,0.1122,391370,179610),('Bronx','Parkchester',2019,0.139,178339,0.07,0.293,0.581,0.028,0.57,46210,0.266,0.243,0.0691,483380,198610),('Brooklyn','Prospect Heights',2010,0.05,119323,0.033,0.616,0.137,0.19,0.56,46810,0.259,0.161,0.1009,423530,528590),('Brooklyn','Prospect Heights',2019,0.07,128327,0.032,0.488,0.141,0.308,0.65,78210,0.159,0.111,0.0412,1576240,1195320),('Queens','Queens Village',2010,0.058,207164,0.148,0.566,0.104,0.133,0.63,92320,0.071,0.147,0.1014,449020,321590),('Queens','Queens Village',2019,0.076,200660,0.168,0.541,0.143,0.09,0.65,99610,0.055,0.139,0.054,593720,415080),('Queens','Rego Park',2010,0.053,114462,0.268,0.012,0.14,0.563,0.59,66910,0.097,0.086,0.0886,799130,407760),('Queens','Rego Park',2019,0.079,105586,0.3,0.02,0.143,0.507,0.63,93690,0.111,0.056,0.0381,998290,727940),('Queens','Ridgewood',2010,0.059,180932,0.089,0.011,0.371,0.517,0.59,64630,0.171,0.221,0.0795,594640,414620),('Queens','Ridgewood',2019,0.057,165895,0.088,0.022,0.356,0.52,0.59,76480,0.084,0.137,0.0314,766050,513860),('Bronx','Riverdale',2010,0.071,109153,0.052,0.133,0.423,0.377,0.66,60730,0.185,0.152,0.1396,743310,596820),('Bronx','Riverdale',2019,0.079,104149,0.044,0.091,0.513,0.312,0.63,64360,0.165,0.189,0.0562,904760,709310),('Queens','Rockaway',2010,0.09,124031,0.01,0.379,0.235,0.358,0.67,58160,0.224,0.219,0.1424,505910,460230),('Queens','Rockaway',2019,0.159,121740,0.027,0.374,0.26,0.323,0.69,57830,0.181,0.206,0.0627,567450,367790),('Brooklyn','Sheepshead Bay',2010,0.076,133282,0.138,0.021,0.066,0.765,0.39,56970,0.137,0.132,0.0901,615880,455090),('Brooklyn','Sheepshead Bay',2019,0.059,147401,0.184,0.038,0.067,0.672,0.51,78950,0.116,0.117,0.0382,844340,499140),('Manhattan','Soho',2010,0.031,144944,0.146,0.024,0.056,0.732,0.44,123930,0.099,0.052,0.0608,8270410,2111600),('Manhattan','Soho',2019,0.029,164514,0.138,0.034,0.114,0.684,0.5,170330,0.061,0.029,0.0432,11033710,2766310),('Bronx','Soundview',2010,0.092,182977,0.071,0.32,0.562,0.024,0.58,47680,0.254,0.303,0.1122,391370,179610),('Bronx','Soundview',2019,0.139,178339,0.07,0.293,0.581,0.028,0.57,46210,0.266,0.243,0.0691,483380,198610),('Staten Island','South Beach',2010,0.083,132502,0.13,0.042,0.125,0.695,0.48,83420,0.097,0.126,0.0816,496350,285190),('Staten Island','South Beach',2019,0.078,138590,0.192,0.039,0.14,0.611,0.57,86260,0.072,0.129,0.0361,604230,364640),('Brooklyn','South Crown Heights',2010,0.07,107419,0.018,0.752,0.065,0.149,0.41,47080,0.256,0.183,0.202,746340,508050),('Brooklyn','South Crown Heights',2019,0.045,106258,0.021,0.572,0.122,0.253,0.59,70090,0.179,0.111,0.0446,1366080,651510),('Queens','South Ozone Park',2010,0.064,135257,0.188,0.13,0.229,0.254,0.83,68330,0.116,0.241,0.1015,424750,271990),('Queens','South Ozone Park',2019,0.089,118568,0.264,0.148,0.249,0.238,0.79,88540,0.075,0.169,0.0449,609480,357280),('Staten Island','St. George',2010,0.067,172052,0.081,0.217,0.272,0.413,0.7,72010,0.179,0.146,0.1009,412610,285400),('Staten Island','St. George',2019,0.072,176195,0.082,0.219,0.295,0.379,0.72,79000,0.13,0.146,0.0513,514910,336270),('Staten Island','Stapleton',2010,0.067,172052,0.081,0.217,0.272,0.413,0.7,72010,0.179,0.146,0.1009,412610,285400),('Staten Island','Stapleton',2019,0.072,176195,0.082,0.219,0.295,0.379,0.72,79000,0.13,0.146,0.0513,514910,336270),('Brooklyn','Starrett City',2010,0.068,146614,0.029,0.547,0.369,0.047,0.56,38310,0.36,0.252,0.1229,349630,238320),('Brooklyn','Starrett City',2019,0.088,180811,0.04,0.554,0.349,0.042,0.57,48330,0.233,0.159,0.0385,504400,341520),('Manhattan','Stuyvesant Town',2010,0.023,145044,0.131,0.054,0.087,0.693,0.49,110580,0.07,0.033,0.0653,4550850,978380),('Manhattan','Stuyvesant Town',2019,0.034,148482,0.155,0.068,0.092,0.661,0.53,162350,0.065,0.033,0.0131,6830390,1313540),('Queens','Sunnyside',2010,0.055,125229,0.348,0.015,0.341,0.274,0.69,63340,0.122,0.198,0.0741,605260,690970),('Queens','Sunnyside',2019,0.042,136058,0.371,0.017,0.293,0.282,0.7,85030,0.092,0.147,0.0392,877440,941810),('Brooklyn','Sunset Park',2010,0.052,141190,0.335,0.02,0.388,0.239,0.68,49030,0.267,0.407,0.1287,810050,449150),('Brooklyn','Sunset Park',2019,0.04,130783,0.348,0.039,0.356,0.237,0.69,71320,0.181,0.31,0.0333,1597260,743660),('Bronx','Throgs Neck',2010,0.086,109482,0.02,0.275,0.311,0.377,0.69,57310,0.164,0.196,0.1074,473290,367100),('Bronx','Throgs Neck',2019,0.16,110883,0.038,0.22,0.439,0.278,0.68,64130,0.129,0.201,0.045,551690,440820),('Staten Island','Tottenville',2010,0.065,164809,0.033,0.013,0.111,0.834,0.29,99120,0.07,0.091,0.0872,508480,339800),('Staten Island','Tottenville',2019,0.065,161358,0.06,0.008,0.107,0.818,0.32,113520,0.041,0.055,0.0305,583210,387760),('Manhattan','Turtle Bay',2010,0.023,145044,0.131,0.054,0.087,0.693,0.49,110580,0.07,0.033,0.0653,4550850,978380),('Manhattan','Turtle Bay',2019,0.034,148482,0.155,0.068,0.092,0.661,0.53,162350,0.065,0.033,0.0131,6830390,1313540),('Manhattan','Upper East Side',2010,0.049,218842,0.092,0.03,0.082,0.776,0.38,115870,0.068,0.031,0.0597,11119250,1451960),('Manhattan','Upper East Side',2019,0.024,216874,0.131,0.023,0.091,0.725,0.45,141090,0.058,0.024,0.0198,10232450,1555230),('Manhattan','Upper West Side',2010,0.05,199843,0.077,0.066,0.153,0.681,0.5,109220,0.104,0.051,0.0746,6629070,1309160),('Manhattan','Upper West Side',2019,0.059,179682,0.101,0.047,0.14,0.687,0.5,143690,0.087,0.047,0.0232,6830390,1610400),('Manhattan','Washington Heights',2010,0.083,205414,0.02,0.074,0.702,0.189,0.47,49960,0.195,0.333,0.1359,409880,442950),('Queens','Whitestone',2010,0.056,257327,0.502,0.02,0.15,0.3,0.64,63230,0.143,0.199,0.1157,716000,447800),('Queens','Whitestone',2019,0.046,239869,0.564,0.017,0.156,0.243,0.6,57730,0.148,0.219,0.0453,945750,662020),('Bronx','Williamsbridge',2010,0.1,137233,0.018,0.64,0.25,0.076,0.52,53370,0.212,0.206,0.1582,394710,317460),('Bronx','Williamsbridge',2019,0.103,149128,0.016,0.602,0.282,0.057,0.55,63290,0.171,0.187,0.0827,483380,130830),('Brooklyn','Williamsburg',2010,0.05,146253,0.052,0.026,0.3,0.607,0.54,50820,0.265,0.211,0.082,821580,615280),('Brooklyn','Williamsburg',2019,0.049,151308,0.066,0.045,0.25,0.613,0.56,103280,0.201,0.155,0.0399,1655060,1119130),('Staten Island','Willowbrook',2010,0.083,132502,0.13,0.042,0.125,0.695,0.48,83420,0.097,0.126,0.0816,496350,285190),('Staten Island','Willowbrook',2019,0.078,138590,0.192,0.039,0.14,0.611,0.57,86260,0.072,0.129,0.0361,604230,364640),('Queens','Woodhaven',2010,0.065,135589,0.228,0.094,0.411,0.186,0.74,69360,0.131,0.186,0.1327,406540,392420),('Queens','Woodhaven',2019,0.079,143756,0.276,0.07,0.394,0.168,0.74,80890,0.101,0.198,0.052,619990,419280),('Queens','Woodside',2010,0.055,125229,0.348,0.015,0.341,0.274,0.69,63340,0.122,0.198,0.0741,605260,690970),('Queens','Woodside',2019,0.042,136058,0.371,0.017,0.293,0.282,0.7,85030,0.092,0.147,0.0392,877440,941810);
/*!40000 ALTER TABLE `neighborhoodDemographics` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-28 13:55:38
