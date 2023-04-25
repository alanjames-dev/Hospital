/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.24-MariaDB : Database - heal_hospitalsss
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`heal_hospitalsss` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `heal_hospitalsss`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_group` */

LOCK TABLES `auth_group` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_group_permissions` */

LOCK TABLES `auth_group_permissions` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_permission` */

LOCK TABLES `auth_permission` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user` */

LOCK TABLES `auth_user` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user_groups` */

LOCK TABLES `auth_user_groups` WRITE;

UNLOCK TABLES;

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `auth_user_user_permissions` */

LOCK TABLES `auth_user_user_permissions` WRITE;

UNLOCK TABLES;

/*Table structure for table `captcha_captchastore` */

DROP TABLE IF EXISTS `captcha_captchastore`;

CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4;

/*Data for the table `captcha_captchastore` */

LOCK TABLES `captcha_captchastore` WRITE;

UNLOCK TABLES;

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_admin_log` */

LOCK TABLES `django_admin_log` WRITE;

UNLOCK TABLES;

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_content_type` */

LOCK TABLES `django_content_type` WRITE;

UNLOCK TABLES;

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_migrations` */

LOCK TABLES `django_migrations` WRITE;

UNLOCK TABLES;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `django_session` */

LOCK TABLES `django_session` WRITE;

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('41i5fcuvcmus8lnycd1uwnjg7165di4s','eyJsaWQiOjUsInBpZCI6MSwiZG9pZCI6MX0:1pmA6L:h7lCxsd-EMKLS2P8ywuPFfExMwKkLn6WJPz8z1GhG3k','2023-04-25 09:15:45.593041'),('bhsciz562jikkj9jfpfeht64dj5gq8u3','eyJsaWQiOjF9:1pjG7Y:KTQntrl6r74nyjy2RszqrkvvZggUwv375B0ta949wXA','2023-04-17 09:05:00.029256'),('g7rtfr1txjqarw5vr3nrormp84qvmpvr','eyJsaWQiOjF9:1pjHil:sGNqPfqa8ZH317JxuCGIof1TUqADoSt--QeboQmXnJo','2023-04-17 10:47:31.803753'),('kjtp4eua1qbz84fsmcgtiaiplgkhdsdr','eyJsaWQiOjEsImRvaWQiOjEsImxhYmlkIjoxfQ:1plvxV:QfmRAPyTuO_KwaKANXNidHK6RFWPMPfANCrxQN94cIQ','2023-04-24 18:09:41.341687'),('lfg3uonzd3hk7k1uh66cjqo72q7lnxfk','.eJyrVsrJTFGyMtFRKgDRhjpKKflQRk5iEphVCwC91wpO:1pkJW1:uGfAWbbk7i5b12s-DIP4DuoUecZ5DiJqIRfK5ItnkI4','2023-04-20 06:54:37.933127'),('rr42prigulivk20mkdzd5cn81yi7p602','.eJyrVsrJTFGyMtJRKgDRhjpKKflQRjGIVrJQqgUAu4oJ2w:1poHMF:Y-x7jQzqkNW8YWrobi2dTg5okbasCFLs5TV1NaPTn_s','2023-05-01 05:24:55.875553'),('tqll6viac7ms0kor8fbv1rez0afkzvxm','.eJyrVsrJTFGyMtRRKoDRGYlFuYnJlVBuSj6UUQyilYyUdJSSQCwjHaW01FSgiKGBAVAsJxEsalgLALSZFmI:1phYae:RXCMsKHaazaYEjoL8__YbzeU9gJYTB4bDxdGhoi9qvY','2023-04-12 16:24:00.109895'),('ys2vaei2080imetbru41wzsi6227npbs','eyJsaWQiOjF9:1pjD4h:VjQIGBLVqZcPZGWlmxlUDJUnGEq2Wz0FTaD5k4NOF8o','2023-04-17 05:49:51.124306');

UNLOCK TABLES;

/*Table structure for table `main_booking` */

DROP TABLE IF EXISTS `main_booking`;

CREATE TABLE `main_booking` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `bk_date` varchar(100) DEFAULT NULL,
  `patient_id_id` int(11) NOT NULL,
  `schedule_id_id` int(11) NOT NULL,
  PRIMARY KEY (`book_id`),
  KEY `main_booking_patient_id_id_10621e31_fk_main_patient_patient_id` (`patient_id_id`),
  KEY `main_booking_schedule_id_id_d722dd95_fk_main_sche` (`schedule_id_id`),
  CONSTRAINT `main_booking_patient_id_id_10621e31_fk_main_patient_patient_id` FOREIGN KEY (`patient_id_id`) REFERENCES `main_patient` (`patient_id`),
  CONSTRAINT `main_booking_schedule_id_id_d722dd95_fk_main_sche` FOREIGN KEY (`schedule_id_id`) REFERENCES `main_schedule` (`schedule_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_booking` */

LOCK TABLES `main_booking` WRITE;

insert  into `main_booking`(`book_id`,`date`,`time`,`status`,`bk_date`,`patient_id_id`,`schedule_id_id`) values (1,'March 29, 2023','09:30 AM','Paid','2023-03-28',1,1),(2,'March 30, 2023','10:10 AM','Paid','2023-03-29',1,2);

UNLOCK TABLES;

/*Table structure for table `main_departments` */

DROP TABLE IF EXISTS `main_departments`;

CREATE TABLE `main_departments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `department` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_departments` */

LOCK TABLES `main_departments` WRITE;

insert  into `main_departments`(`id`,`department`) values (1,'ENT'),(2,'General');

UNLOCK TABLES;

/*Table structure for table `main_doctor` */

DROP TABLE IF EXISTS `main_doctor`;

CREATE TABLE `main_doctor` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `dstatus` varchar(50) NOT NULL,
  `licence_no` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `login_id_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `qualification` varchar(20) DEFAULT NULL,
  `experience` varchar(20) DEFAULT NULL,
  `departments_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`),
  KEY `main_doctor_login_id_id_699db24f_fk_main_login_login_id` (`login_id_id`),
  CONSTRAINT `main_doctor_login_id_id_699db24f_fk_main_login_login_id` FOREIGN KEY (`login_id_id`) REFERENCES `main_login` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_doctor` */

LOCK TABLES `main_doctor` WRITE;

insert  into `main_doctor`(`doctor_id`,`first_name`,`last_name`,`place`,`phone`,`email`,`dstatus`,`licence_no`,`dob`,`gender`,`login_id_id`,`image`,`qualification`,`experience`,`departments_id`) values (1,'Anna','John','Kochi','9812345678','anna@gmail.com','1','AFD1234987564321','2005-02-28','female',5,'t4.jpg',NULL,NULL,1);

UNLOCK TABLES;

/*Table structure for table `main_feedback` */

DROP TABLE IF EXISTS `main_feedback`;

CREATE TABLE `main_feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback_des` varchar(225) NOT NULL,
  `date` date NOT NULL,
  `patient_id_id` int(11) NOT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `main_feedback_patient_id_id_61ccafd2_fk_main_patient_patient_id` (`patient_id_id`),
  CONSTRAINT `main_feedback_patient_id_id_61ccafd2_fk_main_patient_patient_id` FOREIGN KEY (`patient_id_id`) REFERENCES `main_patient` (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_feedback` */

LOCK TABLES `main_feedback` WRITE;

insert  into `main_feedback`(`feedback_id`,`feedback_des`,`date`,`patient_id_id`) values (1,'good ','2023-03-28',1);

UNLOCK TABLES;

/*Table structure for table `main_lab_tests` */

DROP TABLE IF EXISTS `main_lab_tests`;

CREATE TABLE `main_lab_tests` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `test_item` varchar(50) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `upload_lab_prescription_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_lab_tests` */

LOCK TABLES `main_lab_tests` WRITE;

insert  into `main_lab_tests`(`id`,`test_item`,`details`,`date`,`image`,`upload_lab_prescription_id`) values (1,'Scanning','dsfsdfdfd dgdg','2023-04-10','ACIVITY_DIAGRAM_ADMIN.png',1),(2,'Blood','grgt hello','2023-04-10','',1);

UNLOCK TABLES;

/*Table structure for table `main_labs` */

DROP TABLE IF EXISTS `main_labs`;

CREATE TABLE `main_labs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(1000) NOT NULL,
  `phone` varchar(1000) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `login_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_labs` */

LOCK TABLES `main_labs` WRITE;

insert  into `main_labs`(`id`,`name`,`place`,`phone`,`email`,`login_id`) values (1,'Lab','kochi','9812345600','labss@gmail.com',4);

UNLOCK TABLES;

/*Table structure for table `main_leave` */

DROP TABLE IF EXISTS `main_leave`;

CREATE TABLE `main_leave` (
  `leave_id` int(11) NOT NULL AUTO_INCREMENT,
  `leave_des` varchar(225) NOT NULL,
  `leave_type` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `doctor_id_id` int(11) NOT NULL,
  PRIMARY KEY (`leave_id`),
  KEY `main_leave_doctor_id_id_98ccd517_fk_main_doctor_doctor_id` (`doctor_id_id`),
  CONSTRAINT `main_leave_doctor_id_id_98ccd517_fk_main_doctor_doctor_id` FOREIGN KEY (`doctor_id_id`) REFERENCES `main_doctor` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_leave` */

LOCK TABLES `main_leave` WRITE;

insert  into `main_leave`(`leave_id`,`leave_des`,`leave_type`,`status`,`startdate`,`enddate`,`doctor_id_id`) values (1,'sf sd ddsfdsf','Morning','Approved','2023-03-30','2023-03-30',1);

UNLOCK TABLES;

/*Table structure for table `main_login` */

DROP TABLE IF EXISTS `main_login`;

CREATE TABLE `main_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `usertype` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_login` */

LOCK TABLES `main_login` WRITE;

insert  into `main_login`(`login_id`,`username`,`password`,`usertype`,`status`) values (1,'admin@gmail.com','pbkdf2_sha256$260000$AcBXddOFtbWB6JXxysetkj$q6scCJPPqqo6Uyg/Nohv/xcuD7zm3jHbh5qx0CroNPU=','admin','1'),(2,'fff@gmail.com','pbkdf2_sha256$260000$AcBXddOFtbWB6JXxysetkj$q6scCJPPqqo6Uyg/Nohv/xcuD7zm3jHbh5qx0CroNPU=','user','1'),(3,'wwws@gmail.com','pbkdf2_sha256$260000$AcBXddOFtbWB6JXxysetkj$q6scCJPPqqo6Uyg/Nohv/xcuD7zm3jHbh5qx0CroNPU=','pharmacy','1'),(4,'labss@gmail.com','pbkdf2_sha256$260000$AcBXddOFtbWB6JXxysetkj$q6scCJPPqqo6Uyg/Nohv/xcuD7zm3jHbh5qx0CroNPU=','lab','1'),(5,'anna@gmail.com','pbkdf2_sha256$260000$AcBXddOFtbWB6JXxysetkj$q6scCJPPqqo6Uyg/Nohv/xcuD7zm3jHbh5qx0CroNPU=','doctor','1'),(6,'aleenatresa8@gmail.com','pbkdf2_sha256$260000$B60DDFNszT71eWth56bIwo$qWdvBTZOkw1HpWycbwu9jYa6Qq28PI2rCvQbq6j11M4=','user','1'),(7,'jinu123@gmail.com','pbkdf2_sha256$260000$DWZsyikzm3EJuGzS5hCATw$6A9JMgb1sajONHNFuke8pjL61AnM3LjDHWy+5vf3KfM=','user','1'),(8,'alanbabu8886@gmail.com','pbkdf2_sha256$260000$boX8zL04NkaReqbgwZDl1C$qKQCK5mqmv/KnBLOKn3B5pBh0VV+rVwVKj5oSVFCpI8=','user','1'),(9,'anna666@gmail.com','pbkdf2_sha256$260000$rXGhiOIWS55BxH4BRUvPi3$DbJ/tsvyvJX+340LUlva82n3v8+LQ6s7NvbOSUInAWw=','user','1'),(10,'ammu@gmail.com','pbkdf2_sha256$260000$rDGrcx2VIEb8CoNw4em3Z6$AmVK5xiMBeiEFabw9lWTJK6+sbaGpC2+LNsjQ4WT3JY=','user','1'),(11,'ammu1111@gmail.com','pbkdf2_sha256$260000$UtUrHjcx27k1CmWgyUYHjj$JUV7sdzZ2Y/RUEv7yZheUrEBdpiz9Ph/LmqlCokzb2E=','user','1');

UNLOCK TABLES;

/*Table structure for table `main_medicine` */

DROP TABLE IF EXISTS `main_medicine`;

CREATE TABLE `main_medicine` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `medicine` varchar(1000) NOT NULL,
  `quantity` varchar(1000) NOT NULL,
  `price` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `pharmacy_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_medicine_pharmacy_id_675767fa_fk_main_pharmacy_id` (`pharmacy_id`),
  CONSTRAINT `main_medicine_pharmacy_id_675767fa_fk_main_pharmacy_id` FOREIGN KEY (`pharmacy_id`) REFERENCES `main_pharmacy` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_medicine` */

LOCK TABLES `main_medicine` WRITE;

insert  into `main_medicine`(`id`,`medicine`,`quantity`,`price`,`details`,`pharmacy_id`) values (1,'Paracetamol','95','10','ffdv cgfdegdbv fgrgbf',1),(2,'Amlodipine','100','10','dgtfd ytrfyt  ytu6ytuy',1),(3,'Metformin','500','10','tr gttgreg rtet e',1);

UNLOCK TABLES;

/*Table structure for table `main_medicine_details` */

DROP TABLE IF EXISTS `main_medicine_details`;

CREATE TABLE `main_medicine_details` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(100) NOT NULL,
  `rate` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `medicine_id` bigint(20) NOT NULL,
  `upload_pharmacy_prescription_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_medicine_details_medicine_id_d56cea34_fk_main_medicine_id` (`medicine_id`),
  KEY `main_medicine_detail_upload_pharmacy_pres_151be159_fk_main_uplo` (`upload_pharmacy_prescription_id`),
  CONSTRAINT `main_medicine_detail_upload_pharmacy_pres_151be159_fk_main_uplo` FOREIGN KEY (`upload_pharmacy_prescription_id`) REFERENCES `main_upload_pharmacy_prescription` (`id`),
  CONSTRAINT `main_medicine_details_medicine_id_d56cea34_fk_main_medicine_id` FOREIGN KEY (`medicine_id`) REFERENCES `main_medicine` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_medicine_details` */

LOCK TABLES `main_medicine_details` WRITE;

insert  into `main_medicine_details`(`id`,`quantity`,`rate`,`total`,`medicine_id`,`upload_pharmacy_prescription_id`) values (1,'5','10','50',1,1),(2,'5','10','50',2,2);

UNLOCK TABLES;

/*Table structure for table `main_medicines` */

DROP TABLE IF EXISTS `main_medicines`;

CREATE TABLE `main_medicines` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `medicine` varchar(50) DEFAULT NULL,
  `freequency` varchar(50) DEFAULT NULL,
  `dosage` varchar(50) DEFAULT NULL,
  `med_duration` varchar(50) DEFAULT NULL,
  `prescription_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_medicines` */

LOCK TABLES `main_medicines` WRITE;

insert  into `main_medicines`(`id`,`medicine`,`freequency`,`dosage`,`med_duration`,`prescription_id`) values (1,'Medicine1','1-1-1','1-1-1','7 days',1),(2,'Medicine2','1-1-1','1-1-1','2 week',1);

UNLOCK TABLES;

/*Table structure for table `main_online_consultations` */

DROP TABLE IF EXISTS `main_online_consultations`;

CREATE TABLE `main_online_consultations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `bk_date` varchar(50) DEFAULT NULL,
  `patient_id` bigint(20) DEFAULT NULL,
  `doctor_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_online_consultations` */

LOCK TABLES `main_online_consultations` WRITE;

insert  into `main_online_consultations`(`id`,`date`,`time`,`status`,`bk_date`,`patient_id`,`doctor_id`) values (2,'2023-04-27','15:46','Online','2023-04-17',1,1);

UNLOCK TABLES;

/*Table structure for table `main_patient` */

DROP TABLE IF EXISTS `main_patient`;

CREATE TABLE `main_patient` (
  `patient_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `gender` varchar(225) NOT NULL,
  `blood_group` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `pstatus` varchar(50) NOT NULL,
  `age` varchar(15) DEFAULT NULL,
  `login_id_id` int(11) NOT NULL,
  PRIMARY KEY (`patient_id`),
  KEY `main_patient_login_id_id_2b2a9b0a_fk_main_login_login_id` (`login_id_id`),
  CONSTRAINT `main_patient_login_id_id_2b2a9b0a_fk_main_login_login_id` FOREIGN KEY (`login_id_id`) REFERENCES `main_login` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_patient` */

LOCK TABLES `main_patient` WRITE;

insert  into `main_patient`(`patient_id`,`first_name`,`last_name`,`place`,`phone`,`email`,`gender`,`blood_group`,`dob`,`pstatus`,`age`,`login_id_id`) values (1,'Emelda','John','kochi','9812345678','emelda@gmail.com','male','O+ve','2000-02-28','1','25',2),(2,'Anna','John','kochi','9812345678','aleenatresa8@gmail.com','female','B+ve','2000-02-03','1','23',6),(3,'Jinu','John','kochi','9812345678','jinu123@gmail.com','female','AB+ve','2002-02-03','1','19',7),(4,'alan','Babu','Ekm','9605990815','alanbabu8886@gmail.com','female','O+ve','1998-03-03','1','29',8),(5,'Aleena','Tresa','ekm','8787676767','anna666@gmail.com','female','A+ve','1991-02-03','1','22',9),(6,'ammu','anu','ekm','6235326868','ammu@gmail.com','female','O+ve','2012-02-03','1','19',10),(7,'ammu','anu','kochi','6235326868','ammu1111@gmail.com','male','O+ve','2012-06-03','1','29',11);

UNLOCK TABLES;

/*Table structure for table `main_payment` */

DROP TABLE IF EXISTS `main_payment`;

CREATE TABLE `main_payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(20) NOT NULL,
  `date` varchar(50) NOT NULL,
  `type` varchar(100) NOT NULL,
  `book_id_id` int(11) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `main_payment_book_id_id_df08b21d_fk_main_booking_book_id` (`book_id_id`),
  CONSTRAINT `main_payment_book_id_id_df08b21d_fk_main_booking_book_id` FOREIGN KEY (`book_id_id`) REFERENCES `main_booking` (`book_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_payment` */

LOCK TABLES `main_payment` WRITE;

UNLOCK TABLES;

/*Table structure for table `main_pharmacy` */

DROP TABLE IF EXISTS `main_pharmacy`;

CREATE TABLE `main_pharmacy` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(1000) NOT NULL,
  `phone` varchar(1000) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `floor_no` varchar(50) DEFAULT NULL,
  `login_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_pharmacy` */

LOCK TABLES `main_pharmacy` WRITE;

insert  into `main_pharmacy`(`id`,`name`,`place`,`phone`,`email`,`floor_no`,`login_id`) values (1,'ABC','kochi','9812345888','wwws@gmail.com',NULL,3);

UNLOCK TABLES;

/*Table structure for table `main_prescription` */

DROP TABLE IF EXISTS `main_prescription`;

CREATE TABLE `main_prescription` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `diseases` varchar(100) NOT NULL,
  `alergic` varchar(1000) NOT NULL,
  `prescription` varchar(50) NOT NULL,
  `booking_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_prescription_booking_id_a0a5068d_fk_main_booking_book_id` (`booking_id`),
  KEY `main_prescription_doctor_id_013ebda9_fk_main_doctor_doctor_id` (`doctor_id`),
  CONSTRAINT `main_prescription_booking_id_a0a5068d_fk_main_booking_book_id` FOREIGN KEY (`booking_id`) REFERENCES `main_booking` (`book_id`),
  CONSTRAINT `main_prescription_doctor_id_013ebda9_fk_main_doctor_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `main_doctor` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_prescription` */

LOCK TABLES `main_prescription` WRITE;

insert  into `main_prescription`(`id`,`diseases`,`alergic`,`prescription`,`booking_id`,`doctor_id`) values (1,'A78','no','mmf gyhdgts dhsdjushd ',1,1),(2,'A78','fdf','hjghfn nhgjg',1,1),(3,'T47.0X1S','no','dytfc ytfyt',2,1);

UNLOCK TABLES;

/*Table structure for table `main_schedule` */

DROP TABLE IF EXISTS `main_schedule`;

CREATE TABLE `main_schedule` (
  `schedule_id` int(11) NOT NULL AUTO_INCREMENT,
  `start_time` varchar(50) NOT NULL,
  `end_timne` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `fee_amount` varchar(20) NOT NULL,
  `doctor_id_id` int(11) NOT NULL,
  PRIMARY KEY (`schedule_id`),
  KEY `main_schedule_doctor_id_id_db62bee0_fk_main_doctor_doctor_id` (`doctor_id_id`),
  CONSTRAINT `main_schedule_doctor_id_id_db62bee0_fk_main_doctor_doctor_id` FOREIGN KEY (`doctor_id_id`) REFERENCES `main_doctor` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_schedule` */

LOCK TABLES `main_schedule` WRITE;

insert  into `main_schedule`(`schedule_id`,`start_time`,`end_timne`,`date`,`fee_amount`,`doctor_id_id`) values (1,'09:30','15:30','2023-03-29','100',1),(2,'09:30','18:30','2023-03-30','100',1),(3,'09:30','15:30','2023-04-15','250',1),(4,'09:30','15:30','2023-04-23','250',1),(5,'09:30','15:30','2023-04-24','250',1),(7,'09:30','15:30','2023-04-24','250',1),(8,'06:00','10:07','2023-04-29','250',1);

UNLOCK TABLES;

/*Table structure for table `main_test` */

DROP TABLE IF EXISTS `main_test`;

CREATE TABLE `main_test` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `details` varchar(1000) DEFAULT NULL,
  `prescription_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_test` */

LOCK TABLES `main_test` WRITE;

insert  into `main_test`(`id`,`details`,`prescription_id`) values (1,'Scanning',1);

UNLOCK TABLES;

/*Table structure for table `main_upload_lab_prescription` */

DROP TABLE IF EXISTS `main_upload_lab_prescription`;

CREATE TABLE `main_upload_lab_prescription` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `status` varbinary(50) DEFAULT NULL,
  `labs_id` bigint(20) DEFAULT NULL,
  `patient_id` bigint(20) DEFAULT NULL,
  `test_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_upload_lab_prescription` */

LOCK TABLES `main_upload_lab_prescription` WRITE;

insert  into `main_upload_lab_prescription`(`id`,`date`,`status`,`labs_id`,`patient_id`,`test_id`) values (1,'2023-04-06','pending',1,1,1);

UNLOCK TABLES;

/*Table structure for table `main_upload_pharmacy_prescription` */

DROP TABLE IF EXISTS `main_upload_pharmacy_prescription`;

CREATE TABLE `main_upload_pharmacy_prescription` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `total_amt` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `pharmacy_id` bigint(20) NOT NULL,
  `prescription_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_upload_pharmacy_patient_id_cdc6d364_fk_main_pati` (`patient_id`),
  KEY `main_upload_pharmacy_pharmacy_id_7ee65356_fk_main_phar` (`pharmacy_id`),
  KEY `main_upload_pharmacy_prescription_id_8d75de54_fk_main_pres` (`prescription_id`),
  CONSTRAINT `main_upload_pharmacy_patient_id_cdc6d364_fk_main_pati` FOREIGN KEY (`patient_id`) REFERENCES `main_patient` (`patient_id`),
  CONSTRAINT `main_upload_pharmacy_pharmacy_id_7ee65356_fk_main_phar` FOREIGN KEY (`pharmacy_id`) REFERENCES `main_pharmacy` (`id`),
  CONSTRAINT `main_upload_pharmacy_prescription_id_8d75de54_fk_main_pres` FOREIGN KEY (`prescription_id`) REFERENCES `main_prescription` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_upload_pharmacy_prescription` */

LOCK TABLES `main_upload_pharmacy_prescription` WRITE;

insert  into `main_upload_pharmacy_prescription`(`id`,`total_amt`,`date`,`status`,`patient_id`,`pharmacy_id`,`prescription_id`) values (1,'50','2023-03-28','Paid',1,1,1),(2,'50','2023-03-29','pending',1,1,3);

UNLOCK TABLES;

/*Table structure for table `main_user_image_prescription` */

DROP TABLE IF EXISTS `main_user_image_prescription`;

CREATE TABLE `main_user_image_prescription` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `image` varchar(1000) NOT NULL,
  `status` varchar(100) NOT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `booking_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_user_image_pres_booking_id_8c5aceeb_fk_main_book` (`booking_id`),
  KEY `main_user_image_pres_patient_id_f810aa49_fk_main_pati` (`patient_id`),
  CONSTRAINT `main_user_image_pres_booking_id_8c5aceeb_fk_main_book` FOREIGN KEY (`booking_id`) REFERENCES `main_booking` (`book_id`),
  CONSTRAINT `main_user_image_pres_patient_id_f810aa49_fk_main_pati` FOREIGN KEY (`patient_id`) REFERENCES `main_patient` (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `main_user_image_prescription` */

LOCK TABLES `main_user_image_prescription` WRITE;

insert  into `main_user_image_prescription`(`id`,`image`,`status`,`details`,`booking_id`,`patient_id`) values (2,'dd_Brm4uSo.png','uploaded','(May cause drowsiness. Use care when operat\n‘ror dangerous machnes. Don sn aisoNa)\nston taking th medesna\n\n \n\n \n\nTig has acstarinophen Dantiake win oe\nines fst neve asslaranophen (proscrotion\nrnonpresepton) Too much can cause Wer\"\nmage. Guestons? Ant your doctor or\npharmacist\n\n \n\n“Taking more ofthis medicine than recommended\n‘nay cause serious breathing probleme',1,1),(3,'ACTIVITY_DIAGRAM_USER.png','uploaded','LOGIN\n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\n \n\nNO\nYES\n\ny\nVIEW Classified drugs\nVIEW DISEASES SYMPTOMS SEND ENQUIRY UPLOD IMAGES. based on age an\nd predict output\n\nv\n\nLOGOUT\n\n@',2,1);

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
