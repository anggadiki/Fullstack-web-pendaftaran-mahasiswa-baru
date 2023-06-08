-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 08 Jun 2023 pada 07.10
-- Versi server: 8.0.33-0ubuntu0.22.04.2
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pmb`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `Biodata`
--

CREATE TABLE `Biodata` (
  `ID` int NOT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Nama_Lengkap` varchar(255) NOT NULL,
  `Alamat` varchar(255) DEFAULT NULL,
  `Tempat_Lahir` varchar(255) DEFAULT NULL,
  `Tanggal_Lahir` date DEFAULT NULL,
  `Sekolah_Asal` varchar(255) DEFAULT NULL,
  `Tahun_Lulus` date DEFAULT NULL,
  `Jenis_Kelamin` enum('L','P') DEFAULT NULL,
  `Agama` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `No_Hp` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `Biodata`
--

INSERT INTO `Biodata` (`ID`, `Username`, `Nama_Lengkap`, `Alamat`, `Tempat_Lahir`, `Tanggal_Lahir`, `Sekolah_Asal`, `Tahun_Lulus`, `Jenis_Kelamin`, `Agama`, `Email`, `No_Hp`) VALUES
(8, 'angga', 'Angga diki saputra', 'jember', 'jember', '2003-06-02', 'sman 2 jakarta', '2023-06-02', 'L', 'islam', 'anggadiki@gmail.com', '088123321451'),
(9, 'yongki', 'Danil Saputra', 'Cihanjuang', 'Sukabumi', '2003-10-04', 'SMA Negeri 1 Beber', '2021-05-02', 'L', 'Islam', 'ydsaputra@gmail.com', '085794070012'),
(10, 'binta', 'Binta Alaiyah', 'Magelang', 'Magelang', '2002-02-21', 'sman 2 jakarta', '2021-07-06', 'P', 'islam', 'binta@gmail.com', '082234213444'),
(12, 'yuha', 'Yuha Nazif', 'banjar', 'jember', '2003-06-07', 'sman 2 jakarta', '2023-06-07', 'L', 'islam', 'yuha@gmail.com', '088123321451');

-- --------------------------------------------------------

--
-- Struktur dari tabel `Mahasiswa`
--

CREATE TABLE `Mahasiswa` (
  `ID` int NOT NULL,
  `Nim` varchar(255) DEFAULT NULL,
  `Nama_Lengkap` varchar(255) DEFAULT NULL,
  `Alamat` varchar(255) DEFAULT NULL,
  `Tempat_Lahir` varchar(255) DEFAULT NULL,
  `Tanggal_Lahir` date DEFAULT NULL,
  `Tinggi_Badan` varchar(255) DEFAULT NULL,
  `Berat_Badan` varchar(255) DEFAULT NULL,
  `Jenis_Kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  `Agama` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `No_Hp` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `Mahasiswa`
--

INSERT INTO `Mahasiswa` (`ID`, `Nim`, `Nama_Lengkap`, `Alamat`, `Tempat_Lahir`, `Tanggal_Lahir`, `Tinggi_Badan`, `Berat_Badan`, `Jenis_Kelamin`, `Agama`, `Email`, `No_Hp`) VALUES
(1, '212104001', 'Angga Diki', 'jember', 'jember', '2002-06-30', '170', '65', 'Laki-Laki', 'islam', 'anggadiki@gmail.com', '082234213444'),
(2, '212104002', 'Fajar', 'tasik', 'banjar', '1999-08-12', '180', '65', 'Laki-Laki', 'islam', 'fajar@gmail.com', '088123321451'),
(4, '212104003', 'Nur Kholis', 'pekalongan', 'pekalongan', '2004-06-16', '170', '65', 'Laki-Laki', 'Konghucu', 'kholis@gmail.com', '088123321450'),
(5, '212104005', 'Yuha Nazif', 'banjar', 'banjar', '2023-06-07', '180', '50', 'Laki-Laki', 'islam', 'yuha@gmail.com', '082234213444');

-- --------------------------------------------------------

--
-- Struktur dari tabel `Pendaftaran`
--

CREATE TABLE `Pendaftaran` (
  `ID` int NOT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Nama_Jalur` varchar(255) DEFAULT NULL,
  `Tanggal_Pendaftaran` date DEFAULT NULL,
  `Prodi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `Pendaftaran`
--

INSERT INTO `Pendaftaran` (`ID`, `Username`, `Nama_Jalur`, `Tanggal_Pendaftaran`, `Prodi`) VALUES
(5, 'angga', 'Mandiri', '2023-06-02', 'S-1 Sistem Informasi'),
(6, 'yongki', 'Kip Kuliah', '2023-06-02', 'S-1 Teknologi Informasi'),
(7, 'binta', 'Kip Kuliah', '2023-06-06', 'S-1 Teknik Informatika'),
(8, 'yuha', 'Mandiri', '2023-06-07', 'S-1 Sistem Informasi');

-- --------------------------------------------------------

--
-- Struktur dari tabel `Pengumuman`
--

CREATE TABLE `Pengumuman` (
  `ID` int NOT NULL,
  `Nama_Lengkap` varchar(255) DEFAULT NULL,
  `Tanggal_Pengumuman` date DEFAULT NULL,
  `Status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `Pengumuman`
--

INSERT INTO `Pengumuman` (`ID`, `Nama_Lengkap`, `Tanggal_Pengumuman`, `Status`) VALUES
(10, 'Binta Alaiyah', '2023-06-08', 'Di Tolak');

-- --------------------------------------------------------

--
-- Struktur dari tabel `Register`
--

CREATE TABLE `Register` (
  `ID` int NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Role` enum('user','admin') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `Register`
--

INSERT INTO `Register` (`ID`, `Username`, `Email`, `Password`, `Role`) VALUES
(5, 'admin', 'admin@gmail.com', 'admin', 'admin'),
(9, 'angga', 'anggadiki@gmail.com', 'angga', 'user'),
(12, 'binta', 'binta@gmail.com', 'binta', 'user'),
(11, 'naufal', 'nopal@gmail.com', 'npl123', 'user'),
(14, 'superadmin', 'superadmin@gmail.com', 'superadmin', 'admin'),
(10, 'yongki', 'yongki@gmail.com', 'yongki', 'user'),
(13, 'yuha', 'yuha@gmail.com', 'yuha', 'user');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `Biodata`
--
ALTER TABLE `Biodata`
  ADD UNIQUE KEY `ID` (`ID`),
  ADD UNIQUE KEY `ID_2` (`ID`),
  ADD KEY `Username` (`Username`);

--
-- Indeks untuk tabel `Mahasiswa`
--
ALTER TABLE `Mahasiswa`
  ADD PRIMARY KEY (`ID`);

--
-- Indeks untuk tabel `Pendaftaran`
--
ALTER TABLE `Pendaftaran`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Username` (`Username`);

--
-- Indeks untuk tabel `Pengumuman`
--
ALTER TABLE `Pengumuman`
  ADD PRIMARY KEY (`ID`);

--
-- Indeks untuk tabel `Register`
--
ALTER TABLE `Register`
  ADD PRIMARY KEY (`Username`),
  ADD UNIQUE KEY `ID` (`ID`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `Biodata`
--
ALTER TABLE `Biodata`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `Mahasiswa`
--
ALTER TABLE `Mahasiswa`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `Pendaftaran`
--
ALTER TABLE `Pendaftaran`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `Pengumuman`
--
ALTER TABLE `Pengumuman`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `Register`
--
ALTER TABLE `Register`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `Biodata`
--
ALTER TABLE `Biodata`
  ADD CONSTRAINT `Biodata_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `Register` (`Username`);

--
-- Ketidakleluasaan untuk tabel `Pendaftaran`
--
ALTER TABLE `Pendaftaran`
  ADD CONSTRAINT `Pendaftaran_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `Register` (`Username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
