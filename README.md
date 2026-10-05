# MINPRO_2_DDP_SISTEM-PENGELOLAAN-DATA-GAJI-KARYAWAN
**NAMA : SALWA ANNISA NUR FADHILA**

**NIM : 2609116010**

Sistem Pengelolaan Data Gaji Karyawan adalah aplikasi berbasis CLI (Command Line Interface) yang dibuat menggunakan bahasa Python. Program ini berfungsi untuk mengelola data gaji karyawan yang mencakup proses menambah, menampilkan, mengubah, dan menghapus data (CRUD).

Program menerapkan sistem login multi-user dengan dua peran (role):

Admin → dapat menambah, menampilkan, mengubah, dan menghapus data.

User → hanya dapat menampilkan data.

Setiap data karyawan terdiri dari nama, golongan (A/B/C/D/E), dan gaji. Fitur keamanan meliputi penyamaran password saat diketik (pwinput) dan pembatasan login maksimal 3 kali percobaan. Tampilan data disajikan dalam bentuk tabel rapi menggunakan library prettytable.

**BERIKUT GAMBAR FLOWCHART SERTA PENJELASAN ALURNYA**
<img width="1167" height="1843" alt="SALWA 010 Untitled Diagram drawio" src="https://github.com/user-attachments/assets/aa55843e-2db7-491a-9136-bbac5d80658b" />
<br>
1. LOGIN (atas ke bawah)

Program mulai → tampilkan form login → user input username & password

Jika kosong → tampilkan pesan error → kembali ke form login

Jika salah → tambah hitungan percobaan → sudah 3x? → Ya: program selesai | Tidak: kembali ke form login

Jika benar → cek role pengguna

2. PEMILIHAN ROLE (bercabang kiri-kanan)

Role Admin (hijau) → dapat menu: Tambah, Tampilkan, Ubah, Hapus Data, Logout

Role User (hijau) → hanya bisa: Tampilkan Data, Logout

3. MENU UTAMA (loop)
   
Tambah Data: input & validasi nama/golongan/gaji → simpan

Tampilkan Data: cetak tabel

Ubah Data: cari nama → input data baru → update

Hapus Data: cari nama → hapus dari list

Logout: keluar dari menu

5. SETELAH LOGOUT

Mau login lagi? → Ya: kembali ke form login | Tidak: program selesai

<br>

**LOGIN BERHASIL MENGGUNAKAN MENU ADMIN**
<br>
<img width="230" height="52" alt="Screenshot 2026-10-05 215403" src="https://github.com/user-attachments/assets/b3c4f42c-80fe-4775-9999-4d3a1126fffc" />
<br>
Password disamarkan dengan pwinput. Jika username & password cocok dengan data di menu, program menampilkan pesan berhasil.

<br>

**MENAMBAHKAN DATA**
<br>
<img width="195" height="313" alt="Screenshot 2026-10-05 215438" src="https://github.com/user-attachments/assets/ae363fa3-6559-4f7b-b22d-d16225ef0710" />
<br>
<img width="186" height="157" alt="Screenshot 2026-10-05 215525" src="https://github.com/user-attachments/assets/ba5ed47c-4c90-49d0-9bfa-344f161a95e1" />
<br>
Menambahkan 3 data kedalam output dengan nama yang berbeda, golongan berbeda, dan gaji juga berbeda

<br>

**MENAMPILKAN DATA**
<br>
<img width="229" height="197" alt="Screenshot 2026-10-05 215542" src="https://github.com/user-attachments/assets/9fee586d-e4ac-44ed-8286-8b7fb76a1421" />
<br>
Data yang di tambahkan akan muncul setelah klik menampilkan data

<br>

**MENGUBAH DATA**
<br>
<img width="229" height="362" alt="Screenshot 2026-10-05 215612" src="https://github.com/user-attachments/assets/8a91a8b0-97b2-4d1f-85cc-e82eac005106" />
<br>
Data yang sudah di ubah akan menghasilkan data  baru

<br>

**MENGHAPUS DATA**
<br>
<img width="224" height="311" alt="Screenshot 2026-10-05 215629" src="https://github.com/user-attachments/assets/33a783eb-5e6e-4c0a-a2aa-56a5aa8a607d" />
<br>
Data yang di hapus tidak akan di tampilkan lagi

<br>

**LOGOUT**
<br>
<img width="193" height="125" alt="Screenshot 2026-10-05 225724" src="https://github.com/user-attachments/assets/26c14100-d1da-4074-80dd-4a2d6ee3cb88" />
<br>
Setelah logout dari menu admin lalu melanjutkan ke menu user

<br>

**LOGIN BERHASIL MENGGUNAKAN MENU USER**
<br>
<img width="209" height="50" alt="Screenshot 2026-10-05 225940" src="https://github.com/user-attachments/assets/f3a320d2-869c-4927-a137-edaee9570bbc" />
<br>
Password disamarkan dengan pwinput. Jika username & password cocok dengan data di menu, program menampilkan pesan berhasil.

<br>

**MENAMPILKAN DATA**
<br>
<img width="242" height="142" alt="Screenshot 2026-10-05 230011" src="https://github.com/user-attachments/assets/d9f50a04-272e-4866-afee-93bba8b63dbc" />
<br>
Menu user hanya bisa melihat data, hanya menu admin saja yang bisa menambahkan data, mengubah data, menghapus data, dan menampilkan data.

<br>

**LOGOUT**
<br>
<img width="242" height="95" alt="Screenshot 2026-10-05 230023" src="https://github.com/user-attachments/assets/537862c7-d5ad-42dc-99f2-cf1a511e07cb" />
<br>
Program Selesai 

