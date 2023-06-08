# file : model.py
# definisi class untuk user dalam session
from flask import Flask
import pymysql
from datetime import datetime

# Konfigurasi koneksi database
db_host = 'localhost'
db_user = 'root'
db_password = 'password' #kosongkan jika tidak ada password pada phpmyadmin kalian
db_name = 'pmb' #Nama Database kalian

# Fungsi untuk melakukan koneksi ke database
def connect_db():
    conn = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name)
    return conn


# fungsi untuk menampilkan tabel Biodata
def get_data_from_db(Username):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Query untuk mendapatkan data Biodata berdasarkan Username
    query = "SELECT * FROM Biodata WHERE Username = %s"
    cursor.execute(query, (Username,))
    
    # Mendapatkan semua baris hasil query
    rows = cursor.fetchall()
    
    # Menutup kursor dan koneksi ke database
    cursor.close()
    conn.close()
    
    return rows

# Fungsi untuk mengupdate data pada tabel Biodata
def update_biodata(Username, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Sekolah_Asal, Tahun_Lulus, Jenis_Kelamin, Agama, Email, No_Hp):
    conn = connect_db()
    cursor = conn.cursor()

    query = "UPDATE Biodata SET Nama_Lengkap=%s, Alamat=%s, Tempat_Lahir=%s, Tanggal_Lahir=%s, Sekolah_Asal=%s, Tahun_Lulus=%s, Jenis_Kelamin=%s, Agama=%s, Email=%s, No_Hp=%s WHERE Username=%s"
    cursor.execute(query, (Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Sekolah_Asal, Tahun_Lulus, Jenis_Kelamin, Agama, Email, No_Hp, Username))
    conn.commit()

    cursor.close()
    conn.close()

# Fungsi untuk menghapus data pada tabel Biodata
def delete_biodata(Username):
    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM Biodata WHERE Username=%s"
    cursor.execute(query, (Username,))
    conn.commit()

    cursor.close()
    conn.close()



#fungsi mengambil semua tabel biodata
def get_all_from_db_biodata():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Biodata"
    cursor.execute(query,)

    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows


# # fungsi untuk menginsert pada tabel Biodata
def add_biodata(Username,Nama_Lengkap,Alamat,Tempat_Lahir,Tanggal_Lahir,Sekolah_Asal,Tahun_Lulus,Jenis_Kelamin,Agama,Email,No_Hp):
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO Biodata (Username,Nama_Lengkap,Alamat,Tempat_Lahir,Tanggal_Lahir,Sekolah_Asal,Tahun_Lulus,Jenis_Kelamin,Agama,Email,No_Hp) VALUES (%s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)"
    cursor.execute(query, (Username,Nama_Lengkap,Alamat,Tempat_Lahir,Tanggal_Lahir,Sekolah_Asal,Tahun_Lulus,Jenis_Kelamin,Agama,Email,No_Hp))
    conn.commit()

    cursor.close()
    conn.close()

#fungsi untuk menginsert pada tabel Mahasiswa
def add_mahasiswa_db_admin(Nim, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Tinggi_Badan, Berat_Badan, Jenis_Kelamin, Agama, Email, No_Hp):
    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO Mahasiswa (Nim, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Tinggi_Badan, Berat_Badan, Jenis_Kelamin, Agama, Email, No_Hp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (Nim, Nama_Lengkap, Alamat, Tempat_Lahir, datetime.strptime(Tanggal_Lahir, "%Y-%m-%d"), Tinggi_Badan, Berat_Badan, Jenis_Kelamin, Agama, Email, No_Hp))
    conn.commit()

    cursor.close()
    conn.close()

# Fungsi untuk mengambil semua nilai pada tabel Mahasiswa
def get_all_mahasiswa():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Mahasiswa"
    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# Fungsi untuk mengupdate data pada tabel Mahasiswa
def update_mahasiswa(Nim, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Tinggi_Badan, Berat_Badan, Jenis_Kelamin, Agama, Email, No_Hp):
    conn = connect_db()
    cursor = conn.cursor()

    query = "UPDATE Mahasiswa SET Nama_Lengkap=%s, Alamat=%s, Tempat_Lahir=%s, Tanggal_Lahir=%s, Tinggi_Badan=%s, Berat_Badan=%s, Jenis_Kelamin=%s, Agama=%s, Email=%s, No_Hp=%s WHERE Nim=%s"
    cursor.execute(query, (Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Tinggi_Badan, Berat_Badan, Jenis_Kelamin, Agama, Email, No_Hp, Nim))
    conn.commit()

    cursor.close()
    conn.close()

# Fungsi untuk menghapus data pada tabel Mahasiswa
def delete_mahasiswa_db(Nim):
    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM Mahasiswa WHERE Nim=%s"
    cursor.execute(query, (Nim,))
    conn.commit()

    cursor.close()
    conn.close()


# fungsi untuk menginsert pada tabel Pendaftaran
def add_pendaftaran(Username,Nama_Jalur,Tanggal_Pendaftaran,Prodi):
    conn = connect_db()
    cursor = conn.cursor()

    query ="INSERT INTO Pendaftaran(Username,Nama_jalur,Tanggal_Pendaftaran,Prodi) VALUES (%s,%s,%s,%s)"
    cursor.execute(query,(Username,Nama_Jalur,Tanggal_Pendaftaran,Prodi))
    conn.commit()
    
    cursor.close()
    conn.close()

#fungsi untuk menginsert pada tabel pengumuman

def add_pengumuman(Nama_Lengkap,Tanggal_Pengumuman,Status):
    conn = connect_db()
    cursor = conn.cursor()

    query ="INSERT INTO Pengumuman(Nama_Lengkap,Tanggal_Pengumuman,Status) VALUES(%s,%s,%s)"
    cursor.execute(query,(Nama_Lengkap,Tanggal_Pengumuman,Status))
    conn.commit()

    cursor.close()
    conn.close()

# Fungsi untuk mendapatkan data dari database
def get_data_from_db_pengumuman():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Contoh query untuk mendapatkan data dari tabel 'biodata'
    query = "SELECT * FROM Pengumuman"
    cursor.execute(query,)
    
    # Mendapatkan semua baris hasil query
    rows = cursor.fetchall()
    
    # Menutup kursor dan koneksi ke database
    cursor.close()
    conn.close()
    
    return rows

# Fungsi untuk menghapus data pada tabel Pengumuman
def delete_pengumuman_db(ID):
    conn = connect_db()
    cursor = conn.cursor()

    query = "DELETE FROM Pengumuman WHERE ID=%s"
    cursor.execute(query, (ID,))
    conn.commit()

    cursor.close()
    conn.close()

#fungsi untuk update pengumuman
def update_pengumuman_db(ID,Nama_Lengkap,Tanggal_Pengumuman,Status):
    conn = connect_db()
    cursor = conn.cursor()

    query = "UPDATE Pengumuman SET Nama_Lengkap=%s , Tanggal_Pengumuman=%s , Status =%s WHERE ID=%s"
    cursor.execute(query,(Nama_Lengkap,Tanggal_Pengumuman,Status,ID))
    conn.commit()

    cursor.close()
    conn.close()

#fungsi untuk menampilkan tabel Pendaftaran
def get_data_from_db_Pendaftar(Username):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Query untuk mendapatkan data Pendaftaran berdasarkan Username
    query = "SELECT * FROM Pendaftaran WHERE Username = %s"
    cursor.execute(query, (Username,))
    
    # Mendapatkan semua baris hasil query
    rows = cursor.fetchall()
    
    # Menutup kursor dan koneksi ke database
    cursor.close()
    conn.close()
    
    return rows

#fungsi untuk menghitung jumlah pendaftar
def count_form_biodata():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT COUNT(ID) from Biodata"
    cursor.execute(query,)

    rows =cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
#fungsi untuk menghitung jumlah Mahasiswa Baru
def count_form_mahasiswa():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT COUNT(ID) from Mahasiswa"
    cursor.execute(query,)

    rows =cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
#fungsi untuk menghitung jumlah Pengumuman Akhir Seleksi
def count_form_pengumuman():
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT COUNT(ID) from Pengumuman"
    cursor.execute(query,)

    rows =cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# Fungsi untuk mendaftarkan pengguna baru
def register_user(Username,Email,Password,Role):
    conn = connect_db()
    cursor = conn.cursor()

    # Periksa apakah username sudah ada
    query = "SELECT * FROM Register WHERE Username = %s"
    cursor.execute(query, (Username,))

    if cursor.fetchone():
        # Username sudah ada
        cursor.close()
        conn.close()
        return False

    # Masukkan pengguna baru ke dalam database
    query = "INSERT INTO Register (Username,Email,Password,Role) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (Username,Email,Password,Role))
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Fungsi untuk mengotentikasi pengguna
def authenticate_user(Username,Password):
    conn = connect_db()
    cursor = conn.cursor()

    # Periksa apakah username dan password cocok
    query = "SELECT Role FROM Register WHERE Username = %s AND Password = %s"
    cursor.execute(query, (Username, Password))
    result =cursor.fetchone()

    if result:
        # Username dan password benar
        role =result[0]
        cursor.close()
        conn.close()
        return role

    # Username atau password salah
    cursor.close()
    conn.close()
    return False