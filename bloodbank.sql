-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 26, 2023 at 12:42 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bloodbank`
--

-- --------------------------------------------------------

--
-- Table structure for table `adddonors`
--

CREATE TABLE `adddonors` (
  `dname` varchar(256) NOT NULL,
  `dphone` int(100) NOT NULL,
  `daddress` varchar(256) NOT NULL,
  `dmed` varchar(5000) NOT NULL,
  `ddob` varchar(255) NOT NULL,
  `dgen` varchar(256) NOT NULL,
  `dblood` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adddonors`
--

INSERT INTO `adddonors` (`dname`, `dphone`, `daddress`, `dmed`, `ddob`, `dgen`, `dblood`) VALUES
('romi', 1234565678, 'hoshiarpur', 'no', '11-09-17', 'Female', 'ab-'),
('rahul', 987657890, 'phagwara', 'no', '30-08-98', 'Male', 'a-');

-- --------------------------------------------------------

--
-- Table structure for table `addpatients`
--

CREATE TABLE `addpatients` (
  `id` int(11) NOT NULL,
  `PatientName` varchar(255) NOT NULL,
  `PatientPhoneNo` bigint(255) NOT NULL,
  `PatientAddress` varchar(255) NOT NULL,
  `PatientIssue` varchar(255) NOT NULL,
  `PatientDob` varchar(255) NOT NULL,
  `PatientGender` varchar(255) NOT NULL,
  `PatientBloodGroup` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addpatients`
--

INSERT INTO `addpatients` (`id`, `PatientName`, `PatientPhoneNo`, `PatientAddress`, `PatientIssue`, `PatientDob`, `PatientGender`, `PatientBloodGroup`) VALUES
(1, 'rudra', 1234567890, 'jalandhar', 'typhoid', '12', 'Male', 'o+'),
(2, 'aditya', 2345678909, 'jalandhar', 'typhoid', '12-12-22', 'Male', 'b+'),
(3, 'rohini', 3456789098, 'amritsar', 'jaundice', '23-06-18', 'Male', 'b-'),
(4, 'riya', 1345678908, 'jalandhar', 'typhoid', '12-06-2002', 'Female', 'o+'),
(7, 'priyanjali', 8907654326, 'indore', 'fever', '02-02-22', 'Female', 'o+');

-- --------------------------------------------------------

--
-- Table structure for table `blood_stocks`
--

CREATE TABLE `blood_stocks` (
  `id` int(11) NOT NULL,
  `bgroup` varchar(255) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blood_stocks`
--

INSERT INTO `blood_stocks` (`id`, `bgroup`, `qty`) VALUES
(1, 'O+', 10),
(2, 'O-', 10),
(3, 'A+', 20),
(4, 'A-', 15),
(5, 'B+', 25),
(6, 'B-', 10),
(7, 'AB+', 25),
(8, 'AB-', 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addpatients`
--
ALTER TABLE `addpatients`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `blood_stocks`
--
ALTER TABLE `blood_stocks`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addpatients`
--
ALTER TABLE `addpatients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `blood_stocks`
--
ALTER TABLE `blood_stocks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
