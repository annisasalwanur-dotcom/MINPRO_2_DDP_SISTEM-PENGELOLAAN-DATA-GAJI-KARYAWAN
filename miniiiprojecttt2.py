import pwinput
from prettytable import PrettyTable

#SISTEM PENGELOLAAN DATA GAJI KARYAWAN

# data user
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

# list
data_gaji_karyawan = []

# function login
def login():
    for percobaan in range(3):
        print("=== LOGIN ===")
        username = input("username: ")
        password = pwinput.pwinput(prompt="password: ")

        if username == "" or password == "":
            print("username dan password tidak boleh kosong")
        elif username in users and users[username]["password"] == password:
            print("login berhasil, selamat datang", username)
            return username, users[username]["role"]
        else:
            print("username atau password salah, sisa percobaan:", 2 - percobaan)

    print("gagal login 3 kali, program berhenti")
    return None

# penambahan data
def tambah_data():
    print("=== TAMBAH DATA ===")
    nama = input("nama karyawan: ")

    if nama == "":
        print("nama tidak boleh kosong")
        return

    if any(data["nama"] == nama for data in data_gaji_karyawan):
        print("nama sudah terdaftar")
        return

    golongan = input("golongan (A/B/C/D/E): ").upper()
    if golongan not in ["A", "B", "C", "D", "E"]:
        print("golongan tidak valid")
        return

    gaji = input("gaji: ")
    if not gaji.isdigit() or int(gaji) <= 0:
        print("gaji harus angka lebih dari 0")
        return

    data_gaji_karyawan.append({"nama": nama, "golongan": golongan, "gaji": int(gaji)})
    print("data berhasil ditambahkan")

# menampilkan data
def tampilkan_data():
    print("=== DATA GAJI KARYAWAN ===")

    if not data_gaji_karyawan:
        print("belum ada data karyawan")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Golongan", "Gaji"]
    for no, data in enumerate(data_gaji_karyawan, 1):
        tabel.add_row([no, data["nama"], data["golongan"], data["gaji"]])
    print(tabel)

# mengubah data
def ubah_data():
    print("=== UBAH DATA ===")
    nama = input("nama yang ingin diubah: ")

    if nama == "":
        print("nama tidak boleh kosong")
        return

    for data in data_gaji_karyawan:
        if data["nama"] == nama:
            nama_baru = input("nama baru: ")
            golongan_baru = input("golongan baru (A/B/C/D/E): ").upper()
            gaji_baru = input("gaji baru: ")

            if nama_baru:
                data["nama"] = nama_baru
            else:
                print("nama baru tidak boleh kosong")

            if golongan_baru in ["A", "B", "C", "D", "E"]:
                data["golongan"] = golongan_baru
            else:
                print("golongan tidak valid, golongan tidak diubah")

            if gaji_baru.isdigit():
                data["gaji"] = int(gaji_baru)
            else:
                print("gaji tidak valid, gaji tidak diubah")

            print("data berhasil diubah")
            return

    print("data tidak ditemukan")

# menghapus data
def hapus_data():
    print("=== HAPUS DATA ===")
    nama = input("nama yang ingin dihapus: ")

    if nama == "":
        print("nama tidak boleh kosong")
        return

    for data in data_gaji_karyawan:
        if data["nama"] == nama:
            data_gaji_karyawan.remove(data)
            print("data berhasil dihapus")
            return

    print("data tidak ditemukan")

# menu admin & user
menu_admin = {
    "1": ("tambah data", tambah_data),
    "2": ("tampilkan data", tampilkan_data),
    "3": ("ubah data", ubah_data),
    "4": ("hapus data", hapus_data),
    "5": ("logout", None)
}

menu_user = {
    "1": ("tampilkan data", tampilkan_data),
    "2": ("logout", None)
}

# menu utama
while True:
    hasil_login = login()
    if not hasil_login:
        break

    username, role = hasil_login
    menu = menu_admin if role == "admin" else menu_user

    while True:
        print(f"=== MENU {role.upper()} ===")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")

        pilihan = input("pilih menu: ")
        if pilihan in menu:
            label, fungsi = menu[pilihan]
            if fungsi is None:
                print("logout berhasil")
                break
            fungsi()
        else:
            print("pilihan tidak tersedia")

    if input("login lagi? (y/n): ") != "y":
        print("program selesai")
        break