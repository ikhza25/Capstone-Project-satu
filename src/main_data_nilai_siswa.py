from tabulate import tabulate

# List database siswa
list_data_siswa = [
    {
        'NIS': 11001,
        'Nama': 'Amelia Rahmawati',
        'Jenis Kelamin': 'Perempuan',
        'Avg Ulangan Harian': 88,
        'MID': 92,
        'UAS': 90,
        'Nilai Akhir': '',
        'Ket': ''
    },

    {
        'NIS': 11002,
        'Nama': 'Andi Wardana',
        'Jenis Kelamin': 'Laki-laki',
        'Avg Ulangan Harian': 90,
        'MID': 85,
        'UAS': 87,
        'Nilai Akhir': '',
        'Ket': ''
    },

    {
        'NIS': 11003,
        'Nama': 'Anggreni Jamila',
        'Jenis Kelamin': 'Perempuan',
        'Avg Ulangan Harian': 93,
        'MID': 84,
        'UAS': 90,
        'Nilai Akhir': '',
        'Ket': ''
    },

    {
        'NIS': 11004,
        'Nama': 'Bagus Jatmika',
        'Jenis Kelamin': 'Laki-laki',
        'Avg Ulangan Harian': 80,
        'MID': 90,
        'UAS': 87,
        'Nilai Akhir': '',
        'Ket': ''
    },

    {
        'NIS': 11005,
        'Nama': 'Cornelia Devina',
        'Jenis Kelamin': 'Perempuan',
        'Avg Ulangan Harian': 90,
        'MID': 95,
        'UAS': 85,
        'Nilai Akhir': '',
        'Ket': ''
    },

    {
        'NIS': 11006,
        'Nama': 'Ikhza Syafa Muis',
        'Jenis Kelamin': 'Laki-laki',
        'Avg Ulangan Harian': 100,
        'MID': 95,
        'UAS': 100,
        'Nilai Akhir': '',
        'Ket': ''
    }

]

# Menghitung dan memperbarui hasil dari nilai akhir
for siswa in list_data_siswa:
    siswa['Nilai Akhir'] = round((siswa['Avg Ulangan Harian'] * 0.3) + (siswa['MID'] * 0.3) + (siswa['UAS'] * 0.4), 2)

# Menyatakan keterangan untuk siswa apakah lulus atau tidak
for i in list_data_siswa:
    if i['Nilai Akhir'] >= 80:
        i['Ket'] = 'Lulus'
    else:
        i['Ket'] = 'Tidak Lulus'

# Membuat fungsi untuk menampilkan data siswa
def data_siswa(list_data_siswa, header=['No', 'NIS', 'Nama', 'Jenis Kelamin', 'Avg Ulangan Harian', 'MID', 'UAS', 'Nilai Akhir', 'Ket']):
    if len(list_data_siswa)== 0:
        print('Tidak ada data yang ditampilkan. Silahkan tambahkan data terlebih dahulu!')
    else:
    # membuat table kosong
        table1 = []
    
        # looping untuk menampilkan table dengan rapi menggunakan tabulate library
        for i, siswa in enumerate(list_data_siswa, start=1):
            table1.append([i] + list(siswa.values()))
        print(tabulate(table1, headers=header, tablefmt='grid'))

# Membuat fungsi untuk menampilkan filter data siswa
def search_siswa(list_data_siswa, header=['NIS', 'Nama', 'Jenis Kelamin', 'Avg Ulangan Harian', 'MID', 'UAS', 'Nilai Akhir', 'Ket']):
    # Validasi Input search
    while True:
        try:
            # Memasukkan input NIS Siswa
            search = int(input('Masukkan NIS yang ingin di cari: '))

            # Menjalankan fungsi untuk validasi jenis kelamin
            if 10000 <= search <= 19999:
                
                # Membuat table kosong
                table2 = []

                # Membuat tabel untuk hasil filter
                for siswa in list_data_siswa:
                    if search == siswa['NIS']:
                        table2.append(list(siswa.values()))

                # Menampilkan tabel hasil search
                if table2:
                    print(tabulate(table2, headers=header, tablefmt='grid'))
                    break
                else:
                    print("Tidak ada siswa dengan NIS tersebut.")
            else:
                print('Silahkan masukkan NIS yang ingin dicari dengan benar!')
        except ValueError:
            print('Silahkan inputkan angka!')    

# Membuat fungsi untuk menampilkan filter data siswa
def filter_siswa(list_data_siswa, header=['No', 'NIS', 'Nama', 'Jenis Kelamin', 'Avg Ulangan Harian', 'MID', 'UAS', 'Nilai Akhir', 'Ket']):
    while True:
        try:
            # Memasukkan input jenis kelamin yang ingin di filter
            jenis_kelamin = input('5Masukkan kategori jenis kelamin yang ingin ditampilkan (Laki-laki/Perempuan):')

            # Membuat table kosong
            table3 = []

            # Membuat tabel untuk hasil filter
            for i, siswa in enumerate(list_data_siswa, start=1):
                if jenis_kelamin.lower() == siswa['Jenis Kelamin'].lower():
                    table3.append(list(siswa.values()))

            # Menampilkan tabel hasil filter
            if table3:
                table3 = [[i] + row for i, row in enumerate(table3, start=1)]
                print(tabulate(table3, headers=header, tablefmt='grid'))
                break
            else:
                pass
        except:
            print('Silahkan masukkan kategori jenis kelamin (Laki-laki/Perempuan)!')

# Membuat fungsi untuk menambah data siswa
def tambah_siswa():
    while True:
        # Memasukkan nama untuk menambah data siswa 
        name = input('Masukkan Nama Siswa: ').title()
        
        # Validasi Input Nama Siswa  
        if name.replace(' ','').isalpha() == True:
            break
        else:
            print('Silahkan masukkan nama yang benar')

    # Validasi Input Jenis Kelamin
    while True:
    # Memasukkan input jenis kelamin
        jenis_kelamin = input('Masukkan Jenis Kelamin Siswa(Laki-laki/Perempuan): ').capitalize()

        # Menjalankan fungsi untuk validasi jenis kelamin
        if jenis_kelamin.lower() in ['laki-laki', 'perempuan']:
            break
        else:
            print('Silahkan masukkan jenis kelamin yang benar!')

    # Validasi Input Nilai Avg Ulangan Harian
    while True:
        try:
            # Memasukkan input mengenai nilai dari siswa
            avg_ulangan_harian = float(input('Masukkan Nilai Avg Ulangan Harian Siswa: '))

            # Menjalankan fungsi untuk validasi nilai ulangan harian siswa
            if 0 <= avg_ulangan_harian <= 100:
                break
            else:
                print('Silahkan masukkan angka antara 0 sampai 100!')
        except:
            print('Silahkan inputkan angka!')

    # Validasi Input Nilai MID
    while True:
        try:
            # Memasukkan input mengenai nilai dari siswa
            mid = float(input('Masukkan Nilai MID Siswa: '))

            # Menjalankan fungsi untuk validasi nilai mid siswa
            if 0 <= mid <= 100:
                break
            else: 
                print('Silahkan masukkan angka antara 0 sampai 100!')
        except:
            print('Silahkan inputkan angka!')

    # Validasi Input Nilai UAS
    while True:
        try:
            # Memasukkan input mengenai nilai dari siswa
            uas = float(input('Masukkan Nilai UAS Siswa: '))

            # Menjalankan fungsi untuk validasi nilai uas siswa
            if 0 <= uas <= 100:
                break
            else:
                print('Silahkan masukkan angka antara 0 sampai 100!')
        except:
            print('Silahkan inputkan angka!')

    # data NIS dibuatkan secara langsung
    nissiswa = list_data_siswa[-1]['NIS'] + 1

    # Menghitung hasil dari nilai akhir
    nilai_akhir = (avg_ulangan_harian * 0.3) + (mid * 0.3) + (uas * 0.4)

    # Menjalankan fungsi untuk menyatakan keterangan lulus atau tidak
    if nilai_akhir >= 80:
        ket = 'Lulus'
    else:
        ket = 'Tidak Lulus'

    # Menambah data dengan fungsi append
    list_data_siswa.append({
        'NIS' : nissiswa,
        'Nama' : name,
        'Jenis Kelamin' : jenis_kelamin,
        'Avg Ulangan Harian' : avg_ulangan_harian,
        'MID': mid,
        'UAS' : uas,
        'Nilai Akhir' : nilai_akhir,
        'Ket' : ket 
    }) 


    while True:
        # Memvalidasi apakah user ingin menyimpan data siswa yang telah ditambahkan
        cek_tambah_siswa = input('Apakah Anda yakin ingin menyimpan data tersebut? ya/tidak: ')

        # Menjalankan fungsi untuk memvalidasi apakah user ingin menyimpan data siswa yang telah ditambahkan
        if cek_tambah_siswa.lower() in ['tidak', 'no']:
            list_data_siswa.pop()
            print('Data siswa tidak disimpan.')
            break
        elif cek_tambah_siswa.lower() in ['ya', 'y', 'yes']:
            # Menampilkan data setelah data ditambah
            data_siswa(list_data_siswa)
            print(f'Data siswa atas nama {name} dengan NIS {nissiswa} telah disimpan.')
            break
        else:
            print('Input tidak tersedia.')

def update_siswa():
    if len(list_data_siswa)== 0:
        print('Tidak ada data yang ditampilkan. Silahkan tambahkan data terlebih dahulu!')
    else:
        # Menampilkan data sebelum diupdate
        data_siswa(list_data_siswa)

        while True:
            try:
                # Memasukkan input NIS Siswa
                no_nis = int(input('Masukkan NIS yang ingin diupdate: '))

                # menjalankan fungsi input nis
                siswa = []
                for i in list_data_siswa:
                    if i['NIS'] == no_nis:
                        siswa = i
                        break

                # Menjalankan fungsi untuk validasi jenis kelamin
                if siswa:
                    break
                else:
                    print('Silahkan masukkan NIS yang benar!')
            except ValueError:
                print('Silahkan inputkan angka!')    

        while True:
            update_siswa_kategori = input('''
+==============================+
|  Masukkan kategori update    |                     
+==============================+
| 1. Update Nama               |
| 2. Update Nilai              |
| 3. Update Keseluruhan        |
| 4. Kembali Sub Menu          |
+==============================+                  
Masukkan angka yang ingin dipilih:''')
    
            if update_siswa_kategori == '1':
                while True:
                    nama_update = input('Masukkan nama yang baru: ').title()

                    # Validasi Input Nama Siswa  
                    if nama_update.replace(' ','').isalpha() == True:
                        break
                    else:
                        print('Silahkan masukkan nama yang benar')
                        

                while True:
                    # Memasukkan input untuk memastikan apakah yakin user ingin menyimpan update nama tersebut atau tidak
                    cek_update_nama =  input('Apakah Anda yakin akan menyimpan update nama tersebut? Ya/Tidak: ')
                    
                    # Menjalankan fungsi ketika ingin menimpan hasil update
                    if cek_update_nama.lower() in ['ya', 'yes','y']:
                        siswa['Nama'] = nama_update
                        data_siswa(list_data_siswa)
                        print(f'data  dengan NIS {no_nis} berhasil diupdate')
                        break
                    elif cek_update_nama.lower() in ['tidak', 'no']:
                        data_siswa(list_data_siswa)
                        print('data nama tidak diupdate')
                        break
                    else:
                        print('Silahkan masukkan kata (Ya/Tidak)')

            elif update_siswa_kategori == '2':
                while True:
                    try:
                        nilai_siswa_avg = float(input('Masukkan nilai avg ulangan harian yang terbaru: '))
                        if 0 <= nilai_siswa_avg <= 100:
                            break
                        else:
                            print('Silahkan masukkan angka antara 0 sampai 100!')
                    except:
                        print('Silahkan inputkan angka!')
                
                while True:
                    try:
                        nilai_siswa_mid = float(input('Masukkan nilai mid yang terbaru: '))
                        if 0 <= nilai_siswa_mid <= 100:
                            break
                        else:
                            print('Silahkan masukkan angka antara 0 sampai 100!')
                    except:
                        print('Silahkan inputkan angka!')
                
                while True:
                    try:
                        nilai_siswa_uas = float(input('Masukkan nilai uas yang terbaru: '))
                        if 0 <= nilai_siswa_uas <= 100:
                            break
                        else:
                            print('Silahkan masukkan angka antara 0 sampai 100!')
                    except:
                        print('Silahkan inputkan angka!')

                # Menghitung nilai akhir 
                nilai_siswa_nilai_akhir = (nilai_siswa_avg * 0.3) + (nilai_siswa_mid * 0.3) + (nilai_siswa_uas * 0.4)

                # Menjalankan fungsi untuk menyatakan keterangan lulus atau tidak
                if nilai_siswa_nilai_akhir >= 80:
                    nilai_siswa_ket = 'Lulus'
                else:
                    nilai_siswa_ket = 'Tidak Lulus' 
                    
                while True:
                    # Memasukkan input untuk memastikan data ingin diupdate atau tidak
                    cek_update_nilai = input('Apakah anda yakin ingin mengupdate nilai siswa tersebut? [ya/tidak] : ')
                    # Menjalankan fungsi untuk memastikan data diupdate atau tidak
                    if cek_update_nilai.lower() in ['ya', 'yes', 'y']:
                        # Menambahkan data nilai siswa yang sudah di input ke list data siswa
                        siswa['Avg Ulangan Harian'] = nilai_siswa_avg
                        siswa['MID'] = nilai_siswa_mid
                        siswa['UAS'] = nilai_siswa_uas
                        siswa['Nilai Akhir'] = nilai_siswa_nilai_akhir
                        siswa['Ket'] = nilai_siswa_ket

                        # Menampilkan data siswa setelah mengupdate nilai
                        data_siswa(list_data_siswa)
                        print(f'Data siswa nomor {no_nis} telah diupdate.')
                        break

                    elif cek_update_nilai.lower() in ['tidak', 'no','n','t']:
                        data_siswa(list_data_siswa)
                        print('data nilai tidak diupdate')
                        break
            elif update_siswa_kategori == '3':
                while True:
                    nama_update = input('Masukkan nama yang baru: ').title()

                    # Validasi Input Nama Siswa  
                    if nama_update.replace(' ','').isalpha() == True:
                        break
                    else:
                        print('Silahkan masukkan nama yang benar')
                    # Validasi Input Jenis Kelamin
                while True:
                # Memasukkan input jenis kelamin
                    jenis_kelamin = input('Masukkan Jenis Kelamin Siswa(Laki-laki/Perempuan): ').capitalize()

                    # Menjalankan fungsi untuk validasi jenis kelamin
                    if jenis_kelamin.lower() in ['laki-laki', 'perempuan']:
                        break
                    else:
                        print('Silahkan masukkan jenis kelamin yang benar!')
                while True:
                    try:
                        nilai_siswa_avg = float(input('Masukkan nilai avg ulangan harian yang terbaru: '))
                        if 0 <= nilai_siswa_avg <= 100:
                            break
                        else:
                            print('Silahkan masukkan angka antara 0 sampai 100!')
                    except:
                        print('Silahkan inputkan angka!')
                
                while True:
                    try:
                        nilai_siswa_mid = float(input('Masukkan nilai mid yang terbaru: '))
                        if 0 <= nilai_siswa_mid <= 100:
                            break
                        else:
                            print('Silahkan masukkan angka antara 0 sampai 100!')
                    except:
                        print('Silahkan inputkan angka!')
                
                while True:
                    try:
                        nilai_siswa_uas = float(input('Masukkan nilai uas yang terbaru: '))
                        if 0 <= nilai_siswa_uas <= 100:
                            break
                        else:
                            print('Silahkan masukkan angka antara 0 sampai 100!')
                    except:
                        print('Silahkan inputkan angka!')

                # Menghitung nilai akhir 
                nilai_siswa_nilai_akhir = (nilai_siswa_avg * 0.3) + (nilai_siswa_mid * 0.3) + (nilai_siswa_uas * 0.4)

                # Menjalankan fungsi untuk menyatakan keterangan lulus atau tidak
                if nilai_siswa_nilai_akhir >= 80:
                    nilai_siswa_ket = 'Lulus'
                else:
                    nilai_siswa_ket = 'Tidak Lulus' 
                    
                while True:
                    # Memasukkan input untuk memastikan data ingin diupdate atau tidak
                    cek_update_nilai = input('Apakah anda yakin ingin mengupdate nilai siswa tersebut? [ya/tidak] : ')
                    # Menjalankan fungsi untuk memastikan data diupdate atau tidak
                    if cek_update_nilai.lower() in ['ya', 'yes', 'y']:
                        # Menambahkan data nilai siswa yang sudah di input ke list data siswa
                        siswa['Nama'] = nama_update
                        siswa['Jenis Kelamin'] = jenis_kelamin
                        siswa['Avg Ulangan Harian'] = nilai_siswa_avg
                        siswa['MID'] = nilai_siswa_mid
                        siswa['UAS'] = nilai_siswa_uas
                        siswa['Nilai Akhir'] = nilai_siswa_nilai_akhir
                        siswa['Ket'] = nilai_siswa_ket

                        # Menampilkan data siswa setelah mengupdate nilai
                        data_siswa(list_data_siswa)
                        print(f'Data siswa nomor {no_nis} telah diupdate.')
                        break

                    elif cek_update_nilai.lower() in ['tidak', 'no','n','t']:
                        data_siswa(list_data_siswa)
                        print('data nilai tidak diupdate')
                        break
            elif update_siswa_kategori == '4':
                break

            else:
                print('Pilihan yang Anda masukkan tidak tersedia')     


def hapus_siswa():
    # Menampilkan data sebelum dihapus
    data_siswa(list_data_siswa)

    while True:
        try:
            # Memasukkan input NIS Siswa
            no_nis = int(input('Masukkan NIS yang ingin dihapus: '))

            # Mencari siswa berdasarkan NIS
            siswa = next((i for i in list_data_siswa if i['NIS'] == no_nis), None)
            if not siswa:
                print('Silahkan masukkan NIS yang benar!')
                continue

            print(f'Anda akan menghapus data siswa {siswa["Nama"]} dengan NIS {siswa["NIS"]}')
            # mengkonfirmasi kepada user apakah data ingin dihapus atau tidak
            cek_hapus_siswa = input('Apakah Anda yakin ingin menghapus data siswa tersebut? ya/tidak: ').lower()

            # Menjalankan fungsi untuk memastikan data ingin dihapus atau tidak
            if cek_hapus_siswa in ['ya', 'y', 'yes']:
                list_data_siswa.remove(siswa)
                # Menampilkan data setelah data dihapus
                data_siswa(list_data_siswa)
                print('Data siswa berhasil dihapus')
                break
            elif cek_hapus_siswa in ['tidak', 'no']:
                print('Data siswa tidak dihapus')
                break
            else:
                print('Input tidak tersedia')
                
        except ValueError:
            print('Silahkan inputkan angka!')

# Menampilkan sub menu data siswa
def sub_menu_data_siswa():
    while True:
        sub_menu1 = input('''
+=============================================+
|        List Menampilkan Data Nilai Siswa    |      
+=============================================+
| 1. Menampilkan Data Nilai Siswa             |
| 2. Search Data Nilai Siswa                  |
| 3. Filter Data Nilai Siswa                  |
| 4. Kembali ke main menu                     |
+=============================================+
Masukkan pilihan list menu: ''')
        
        if sub_menu1 == '1':
            data_siswa(list_data_siswa)
        elif sub_menu1 == '2':
            search_siswa(list_data_siswa)
        elif sub_menu1 == '3':
            filter_siswa(list_data_siswa)
        elif sub_menu1 == '4':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia')

# Menampilkan sub menu tambah siswa
def sub_menu_tambah_siswa():
    while True:
        sub_menu2 = input('''
+===================================+
|    List Tambah Data Nilai Siswa   |       
+===================================+
| 1. Menambahkan Data Nilai Siswa   |
| 2. Kembali ke main menu           |
+===================================+
Masukkan pilihan list menu: ''')
        
        # Meminta user memasukkan input nomor sesuai dengan pilihan sub menu tambah
        if sub_menu2 == '1':
            tambah_siswa()
        elif sub_menu2 == '2':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia')

# sub menu 3
def sub_menu_update_siswa():
    while True:
        sub_menu3 = input('''
+==============================+
| List Update Data Nilai Siswa |      
+==============================+
| 1. Update Data Nilai Siswa   |
| 2. Kembali ke main menu      |
+==============================+
Masukkan pilihan list menu:''')
        
        # Meminta user memasukkan input nomor sesuai dengan pilihan sub menu update
        if sub_menu3 == '1':
            update_siswa()
        elif sub_menu3 == '2':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia')

# sub menu 4
def sub_menu_hapus_siswa():
    while True:
        # Meminta user memasukkan input nomor sesuai dengan pilihan sub menu hapus 
        sub_menu4 = input('''
+===================================+
|   List Hapus Data Nilai Siswa     |  
+===================================+
| 1. Menghapus Data Nilai Siswa     |
| 2. Kembali ke main menu           |
+===================================+
Masukkan pilihan list menu:''')
        
        # Menjalankan fungsi sesuai pilihan sub menu hapus
        if sub_menu4 == '1':
            hapus_siswa()
        elif sub_menu4 == '2':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia')

# Menu utama daftar nilai siswa
def main_menu():
    while True:
        # Meminta user memasukkan input sesuai nomor 
        pilihan_menu = input('''
+==============================================+
|   Selamat Datang di Menu Daftar Nilai Siswa  |
+==============================================+
| 1. Menampilkan Data Nilai Siswa              |
| 2. Menambah Data Nilai Siswa                 |
| 3. Update Data Nilai Siswa                   |
| 4. Menghapus Data Nilai Siswa                |
| 5. Keluar                                    |
+==============================================+
Masukkan pilihan menu :''')
        
        # Menjalankan fungsi sesuai pilihan menu
        if pilihan_menu == '1':
            sub_menu_data_siswa()
        elif pilihan_menu == '2':
            sub_menu_tambah_siswa()
        elif pilihan_menu == '3':
            sub_menu_update_siswa()
        elif pilihan_menu == '4':
            sub_menu_hapus_siswa()
        elif pilihan_menu == '5':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia' )

# Menjalankan program utama
main_menu()