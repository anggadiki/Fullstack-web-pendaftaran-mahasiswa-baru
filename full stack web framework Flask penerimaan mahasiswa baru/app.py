from flask import Flask, render_template, session, request, redirect
from model import get_data_from_db,get_data_from_db_Pendaftar,get_data_from_db_pengumuman,get_all_mahasiswa,get_all_from_db_biodata,count_form_biodata,count_form_mahasiswa,count_form_pengumuman,register_user,authenticate_user,add_biodata,add_mahasiswa_db_admin,add_pendaftaran,add_pengumuman,update_biodata,update_mahasiswa,update_pengumuman_db,delete_biodata,delete_mahasiswa_db,delete_pengumuman_db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aku ganteng 123 sekali' #bisa di ubah sesuai keinginan tidak boleh kosong

# route untuk mengarahka ke halaman utama
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


#Route untuk mengisi form pendaftaran jalur kuliah
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

#route untuk update biodata
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

