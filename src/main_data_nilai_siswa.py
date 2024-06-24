# mengimpor modul tabulate yang diperlukan untuk membuat tabel
from tabulate import tabulate

# List database siswa
list_data_siswa = [
    {
        'Nama' : 'Amelia Rahmawati',
        'NIS' : 11001,
        'Jenis Kelamin' : 'Perempuan',
        'Avg Ulangan Harian' : 88,
        'MID': 92,
        'UAS' : 90,
        'Nilai Akhir' : '',
        'Ket' : ''
    },

    {
        'Nama' : 'Andi Wardana',
        'NIS' : 11002,
        'Jenis Kelamin' : 'Laki-laki',
        'Avg Ulangan Harian' : 90,
        'MID': 85,
        'UAS' : 87,
        'Nilai Akhir' : '',
        'Ket' : ''
    },

    {
        'Nama' : 'Anggreni Jamila',
        'NIS' : 11003,
        'Jenis Kelamin' : 'Perempuan',
        'Avg Ulangan Harian' : 93,
        'MID': 84,
        'UAS' : 90,
        'Nilai Akhir' : '',
        'Ket' : ''
    },

    {
        'Nama' : 'Bagus Jatmika',
        'NIS' : 11004,
        'Jenis Kelamin' : 'Laki-laki',
        'Avg Ulangan Harian' : 80,
        'MID': 90,
        'UAS' : 87,
        'Nilai Akhir' : '',
        'Ket' : ''
    },

    {
        'Nama' : 'Cornelia Devina',
        'NIS' : 11005,
        'Jenis Kelamin' : 'Perempuan',
        'Avg Ulangan Harian' : 90,
        'MID': 95,
        'UAS' : 85,
        'Nilai Akhir' : '',
        'Ket' : ''
    },

    {
        'Nama' : 'Ikhza Syafa Muis',
        'NIS' : 11006,
        'Jenis Kelamin' : 'Laki-laki',
        'Avg Ulangan Harian' : 100,
        'MID': 95,
        'UAS' : 100,
        'Nilai Akhir' : '',
        'Ket' : ''
    }

]

# Menghitung dan memperbarui hasil dari nilai akhir
for siswa in list_data_siswa:
    siswa['Nilai Akhir'] = (siswa['Avg Ulangan Harian'] * 0.3) + (siswa['MID'] * 0.3) + (siswa['UAS'] * 0.4)

# Menyatakan keterangan untuk siswa apakah lulus atau tidak
for i in list_data_siswa:
    if i['Nilai Akhir'] >= 80:
        i['Ket'] = 'Lulus'
    else:
        i['Ket'] = 'Tidak Lulus'

# Membuat fungsi untuk menampilkan data siswa
def data_siswa(list_data_siswa, header=['No', 'Nama', 'NIS', 'Jenis Kelamin', 'Avg Ulangan Harian', 'MID', 'UAS', 'Nilai Akhir', 'Ket']):
   
    # membuat table kosong
    table1 = []
   
    # looping untuk menampilkan table dengan rapi menggunakan tabulate library
    for i, siswa in enumerate(list_data_siswa, start=1):
        table1.append([i] + list(siswa.values()))
    print(tabulate(table1, headers=header, tablefmt='grid'))

# Membuat fungsi untuk menampilkan filter data siswa
def filter_siswa(list_data_siswa, header=['No', 'Nama', 'NIS', 'Jenis Kelamin', 'Avg Ulangan Harian', 'MID', 'UAS', 'Nilai Akhir', 'Ket']):

    # Memasukkan input jenis kelamin yang ingin di filter
    jenis_kelamin = input('Masukkan jenis kelamin yang ingin di filter(Laki-laki/Perempuan): ')

    # Membuat table kosong
    table2 = []

    # Membuat tabel untuk hasil filter
    for i, siswa in enumerate(list_data_siswa, start=1):
        if jenis_kelamin.lower() == siswa['Jenis Kelamin'].lower():
            table2.append([i] + list(siswa.values()))

    # Menampilkan tabel hasil filter
    if table2:
        print(tabulate(table2, headers=header, tablefmt='grid'))
    else:
        print("Tidak ada siswa dengan jenis kelamin tersebut.")

# Membuat fungsi untuk menambah data siswa
def tambah_siswa():
    while True:
        # Memasukkan nama untuk menambah data siswa 
        name = input('Masukkan Nama Siswa: ').title()
        
        # Validasi Input Nama Siswa  
        if name.replace(' ','').isalpha() == True :
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
        'Nama' : name,
        'NIS' : nissiswa,
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
    # Menampilkan data sebelum diupdate
    data_siswa(list_data_siswa)

    while True:
        # Memasukkan input angka yang ingin diupdate
        no_siswa = int(input('Masukkan nomor urut yang ingin diupdate nilainya: ')) - 1
        
        # Menjalankan fungsi untuk validasi apakah data tersedia atau tidak
        if no_siswa > 0 or no_siswa < len(list_data_siswa):
            break
        else:
            print('Nomor tidak tersedia')
            continue

    while True:
        update_siswa_kategori = input('''
================================
   Masukkan kategori update                          
================================
 1. Update Nama
 2. Update Nilai
 3. Kembali Sub Menu
================================                   
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
                    list_data_siswa[no_siswa]['Nama'] = nama_update
                    data_siswa(list_data_siswa)
                    print(f'data  dengan nomor {no_siswa + 1} berhasil diupdate')
                    break
                elif cek_update_nama.lower() in ['tidak', 'no']:
                    data_siswa(list_data_siswa)
                    print('data nama tidak diupdate')
                    break
                else:
                    print('Silahkan masukkan kata Ya/Tidak')

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
                    list_data_siswa[no_siswa]['Avg Ulangan Harian'] = nilai_siswa_avg
                    list_data_siswa[no_siswa]['MID'] = nilai_siswa_mid
                    list_data_siswa[no_siswa]['UAS'] = nilai_siswa_uas
                    list_data_siswa[no_siswa]['Nilai Akhir'] = nilai_siswa_nilai_akhir
                    list_data_siswa[no_siswa]['Ket'] = nilai_siswa_ket

                    # Menampilkan data siswa setelah mengupdate nilai
                    data_siswa(list_data_siswa)
                    print(f'Data siswa nomor {no_siswa + 1} telah diupdate.')
                    break

                elif cek_update_nilai.lower() in ['tidak', 'no','n','t5']:
                    data_siswa(list_data_siswa)
                    print('data nilai tidak diupdate')
                    break
        elif update_siswa_kategori == '3':
            break

        else:
            print('Pilihan yang Anda masukkan tidak tersedia')     


def hapus_siswa():
    
    # Menampilkan data sebelum dihapus
    data_siswa(list_data_siswa)

    while True:
        try:
            # Memasukkan input nomor berapa data yang ingin dihapus
            no_siswa = int(input('Masukkan nomor yang ingin dihapus:')) - 1

            # Menjalankan fungsi untuk memastikan apakah data tersedia tau tidak
            if no_siswa < 0 or no_siswa > len(list_data_siswa):
                print('Nomor tidak tersedia')
                continue

            # Menampilkan data yang akan dihapus
            print(f'Anda akan menghapus data siswa {list_data_siswa[no_siswa]["Nama"]} dengan NIS {list_data_siswa[no_siswa]["NIS"]}')

            # mengkonfirmasi kepada user apakah data ingin dihapus atau tidak
            cek_hapus_siswa = input('Apakah Anda yakin ingin menghapus data siswa tersebut? ya/tidak: ')
            
            # Menjalankan fungsi untuk memastikan data ingin dihapus atau tidak
            if cek_hapus_siswa.lower() in ['ya', 'y', 'yes']:
                list_data_siswa.pop(no_siswa)
                # Menampilkan data setelah data dihapus
                data_siswa(list_data_siswa)
                print('Data siswa berhasil dihapus')
                break
            elif cek_hapus_siswa.lower() in ['tidak', 'no', 'n']:
                print('data siswa tidak dihapus')
                break
            else:
                print('input tidak tersedia')
                continue
        except:
            print('Silahkan inputkan angka!')

# Menampilkan sub menu data siswa
def sub_menu_data_siswa():
    while True:
        sub_menu1 = input('''
===============================================
        List Menampilkan Data Nilai Siswa           
===============================================
 1. Menampilkan Data Nilai Siswa 
 2. Filter Data Siswa            
 3. Kembali ke main menu         
===============================================
Masukkan pilihan list menu: ''')
        
        if sub_menu1 == '1':
            data_siswa(list_data_siswa)
        elif sub_menu1 == '2':
            filter_siswa(list_data_siswa)
        elif sub_menu1 == '3':
            break
        else:
            print('Pilihan menu yang Anda masukkan tidak tersedia')

# Menampilkan sub menu tambah siswa
def sub_menu_tambah_siswa():
    while True:
        sub_menu2 = input('''
=====================================
     List Tambah Data Nilai Siswa           
=====================================
 1. Menambahkan Data Nilai Siswa   
 2. Kembali ke main menu           
=====================================
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
================================
  List Update Data Nilai Siswa        
================================
 1. Update Data Nilai Siswa    
 2. Kembali ke main menu       
================================
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
=====================================
   List Hapus Data Nilai Siswa       
=====================================
 1. Menghapus Data Nilai Siswa 
 2. Kembali ke main menu       
=====================================
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
================================================
    Selamat Datang di Menu Daftar Nilai Siswa   
================================================
 1. Menampilkan Data Nilai Siswa               
 2. Menambah Data Nilai Siswa                  
 3. Update Data Nilai Siswa                    
 4. Menghapus Data Nilai Siswa                 
 5. Keluar                                     
================================================
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