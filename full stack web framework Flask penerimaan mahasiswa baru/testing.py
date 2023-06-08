from flask import Flask, render_template, request, redirect, session
import pymysql
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aku ganteng 123'

# Konfigurasi koneksi database
db_host = 'localhost'
db_user = 'root'
db_password = 'password'
db_name = 'pmb'

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

# ...
@app.route('/')
def index():
    if 'Username' in session:
        Username = session['Username']
        Role = session['Role']
        if 'is_data_filled' in session:
            data_filled = True
        else:
            data_filled = False
        data = get_data_from_db(Username) # Mengirim data ke template untuk ditampilkan
        data2= get_data_from_db_Pendaftar(Username)
        data3= get_data_from_db_pengumuman()
        count= count_form_biodata()
        count2=count_form_mahasiswa()
        count3=count_form_pengumuman()
        if Role =='user':
            return render_template('dasboard.html', data=data ,data2=data2, data3=data3,Username=Username,Role=Role, data_filled=data_filled)
        elif Role =='admin':
            return render_template('dashboard_admin.html',Username=Username,Role=Role,count=count,count2=count2,count3=count3)
    else:
        return redirect('/login')


# Route untuk halaman registrasi
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        Username = request.form['Username']
        Email = request.form['Email']
        Password = request.form['Password']
        Role = request.form['Role']

        if register_user(Username, Email,Password,Role):
            return redirect('/login')
        else:
            return render_template('register.html', message='Username sudah ada')

    return render_template('daftar.html')

# Route untuk halaman login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Username = request.form['Username']
        Password = request.form['Password']

        Role = authenticate_user(Username,Password)

        if Role =='admin' or Role=='user':
            session['Username'] = Username
            session['Role'] = Role
            return redirect('/')
        else:
            return render_template('login.html', message='Username atau password salah')

    return render_template('login.html')

# Route untuk halaman tambah biodata
# Route untuk halaman tambah_data
@app.route('/tambah_data', methods=['GET', 'POST'])
def tambah_data():
    if 'Username' in session:
        if request.method == 'POST':
            # Mengambil data dari form
            Username = request.form['Username']
            Nama_Lengkap = request.form['Nama_Lengkap']
            Alamat = request.form['Alamat']
            Tempat_Lahir = request.form['Tempat_Lahir']
            Tanggal_Lahir = request.form['Tanggal_Lahir']
            Sekolah_Asal = request.form['Sekolah_Asal']
            Tahun_Lulus = request.form['Tahun_Lulus']
            Jenis_Kelamin = request.form['Jenis_Kelamin']
            Agama = request.form['Agama']
            Email = request.form['Email']
            No_Hp = request.form['No_Hp']

            # Panggil fungsi add_biodata untuk menyimpan data ke database
            add_biodata(Username, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Sekolah_Asal, Tahun_Lulus, Jenis_Kelamin, Agama, Email, No_Hp)

            # Redirect ke halaman utama setelah berhasil menambahkan data
            return redirect('/')
        else:
            # Halaman tambah_data akan dirender jika metode HTTP adalah GET
            return render_template('tambah_data_user.html')
    else:
        # Jika pengguna tidak masuk, redirect ke halaman login
        return redirect('/login')


@app.route('/form_pendaftaran', methods=['GET','POST'])
def daftar_kuliah():
    if 'Username' in session:
        if request.method == 'POST':
            Username = request.form['Username']
            Nama_Jalur = request.form['Nama_Jalur']
            Tanggal_Pendaftaran = request.form['Tanggal_Pendaftaran']
            Prodi = request.form['Prodi']
            add_pendaftaran(Username,Nama_Jalur,Tanggal_Pendaftaran,Prodi)
            return redirect('/')
        else:
            return render_template('form_pendaftaran_user.html')
    return redirect('/login')

@app.route('/daftar_pendaftar', methods=['GET', 'POST'])
def daftar_pendaftar():
    if "Username" in session:
        if request.method == 'POST':
            Username = request.form['Username']
            Nama_Lengkap = request.form['Nama_Lengkap']
            Alamat = request.form['Alamat']
            Tempat_Lahir = request.form['Tempat_Lahir']
            Tanggal_Lahir = request.form['Tanggal_Lahir']
            Sekolah_Asal = request.form['Sekolah_Asal']
            Tahun_Lulus = request.form['Tahun_Lulus']
            Jenis_Kelamin = request.form['Jenis_Kelamin']
            Agama = request.form['Agama']
            Email = request.form['Email']
            No_Hp = request.form['No_Hp']
            update_biodata(
                Username, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir,
                Sekolah_Asal, Tahun_Lulus, Jenis_Kelamin, Agama, Email, No_Hp
            )
            return redirect('/daftar_pendaftar')
        else:
            data4 = get_all_from_db_biodata()
            return render_template('daftar_pendaftar_admin.html', data4=data4)
    return redirect('/login')

# Route untuk menghapus biodata
@app.route('/delete_biodata/<string:Username>', methods=['GET','POST'])
def delete_biodata_route(Username):
    if 'Username' in session and session['Role'] == 'admin':
        delete_biodata(Username)
        return redirect('/daftar_pendaftar')
    return redirect('/login')

#Route untuk halaman admin daftar mahasiswa
@app.route('/daftar_mahasiswa', methods=['GET', 'POST'])
def daftar_mahasiswa():
    if 'Username' in session:
        if request.method == 'POST':
            Nim = request.form['Nim']
            Nama_Lengkap = request.form['Nama_Lengkap']
            Alamat = request.form['Alamat']
            Tempat_Lahir = request.form['Tempat_Lahir']
            Tanggal_Lahir = request.form['Tanggal_Lahir']
            Tinggi_Badan = request.form['Tinggi_Badan']
            Berat_Badan = request.form['Berat_Badan']
            Jenis_Kelamin = request.form['Jenis_Kelamin']
            Agama = request.form['Agama']
            Email = request.form['Email']
            No_Hp = request.form['No_Hp']
            add_mahasiswa_db_admin(
                Nim, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir,
                Tinggi_Badan, Berat_Badan, Jenis_Kelamin, Agama, Email, No_Hp
            )
            return redirect('/daftar_mahasiswa')

        else:
            data_mahasiswa=get_all_mahasiswa()
            return render_template('daftar_mahasiswa_admin.html',data_mahasiswa=data_mahasiswa)
    return redirect('/login')


# Route untuk halaman update mahasiswa
@app.route('/update_mahasiswa', methods=['GET', 'POST'])
def update_mahasiswa_route():
    if request.method == 'POST':
        Nim = request.form['Nim']
        Nama_Lengkap = request.form['Nama_Lengkap']
        Alamat = request.form['Alamat']
        Tempat_Lahir = request.form['Tempat_Lahir']
        Tanggal_Lahir = request.form['Tanggal_Lahir']
        Tinggi_Badan = request.form['Tinggi_Badan']
        Berat_Badan = request.form['Berat_Badan']
        Jenis_Kelamin = request.form['Jenis_Kelamin']
        Agama = request.form['Agama']
        Email = request.form['Email']
        No_Hp = request.form['No_Hp']
        update_mahasiswa(Nim, Nama_Lengkap, Alamat, Tempat_Lahir, Tanggal_Lahir, Tinggi_Badan, Berat_Badan, Jenis_Kelamin, Agama, Email, No_Hp)
        return redirect('/daftar_mahasiswa')
    else:
        return render_template('daftar_mahasiswa_admin.html')

#Route untuk menghapus data pada tabel mahasiswa
@app.route('/delete_mahasiswa/<string:Nim>',methods=['GET','POST'])
def delete_mahasiswa(Nim):
    delete_mahasiswa_db(Nim)
    return redirect('/daftar_mahasiswa')

#route pengumuman admin
@app.route('/pengumuman_admin',methods =['GET','POST'])
def tambah_pengumuman():
    if request.method == 'POST':
        Nama_Lengkap = request.form['Nama_Lengkap']
        Tanggal_Pengumuman = request.form['Tanggal_Pengumuman']
        Status = request.form['Status']
        add_pengumuman(Nama_Lengkap,Tanggal_Pengumuman,Status)
        return redirect('/pengumuman_admin')
    else:
        data_pengumuman = get_data_from_db_pengumuman()
        return render_template('/pengumuman_admin.html',data_pengumuman=data_pengumuman)

#utang fungsi update di pengumuman kerjakan

@app.route('/update_pengumuman',methods=['GET','POST'])
def update_pengumuman():
    if request.method == 'POST':
        ID = request.form['ID']
        Nama_Lengkap = request.form['Nama_Lengkap']
        Tanggal_Pengumuman = request.form['Tanggal_Pengumuman']
        Status = request.form['Status']
        update_pengumuman_db(ID,Nama_Lengkap,Tanggal_Pengumuman,Status)
        return redirect('/pengumuman_admin')
    else:
        return render_template('pengumuman_admin.html')

#Route untuk menghapus data pada tabel mahasiswa
@app.route('/delete_pengumuman/<string:ID>',methods=['GET','POST'])
def delete_pengumuman(ID):
    delete_pengumuman_db(ID)
    return redirect('/pengumuman_admin')

#route untuk developer
@app.route('/developer')
def dev():
    return render_template('developer.html')

# Route untuk halaman logout
@app.route('/logout')
def logout():
    session.pop('Username', None)
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
