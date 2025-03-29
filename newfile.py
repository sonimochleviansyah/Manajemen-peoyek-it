# Aplikasi Manajemen Proyek IT

# Membuat dictionary untuk menyimpan data proyek
proyek = {}

def tambah_proyek(nama_proyek, anggota_tim, status):
    """Menambahkan proyek baru ke dalam dictionary."""
    proyek[nama_proyek] = {
        "anggota_tim": anggota_tim,
        "status": status
    }
    print(f'Proyek "{nama_proyek}" berhasil ditambahkan.')

def ubah_status_proyek(nama_proyek, status_baru):
    """Mengubah status proyek yang sudah ada."""
    if nama_proyek in proyek:
        proyek[nama_proyek]["status"] = status_baru
        print(f'Status proyek "{nama_proyek}" berhasil diubah menjadi "{status_baru}".')
    else:
        print(f'Proyek "{nama_proyek}" tidak ditemukan.')

def tampilkan_proyek():
    """Menampilkan daftar proyek yang sedang berjalan dan statusnya."""
    print("\nDaftar Proyek:")
    for nama_proyek, info in proyek.items():
        print(f'- Proyek: {nama_proyek}, Anggota Tim: {info["anggota_tim"]}, Status: {info["status"]}')

def laporan_proyek():
    """Menampilkan laporan proyek yang sudah selesai dan yang sedang dalam progres."""
    selesai = [nama for nama, info in proyek.items() if info["status"] == "selesai"]
    progres = [nama for nama, info in proyek.items() if info["status"] != "selesai"]

    print("\nLaporan Proyek:")
    print("Proyek yang sudah selesai:", selesai)
    print("Proyek yang sedang dalam progres:", progres)

# Interaksi dengan pengguna
while True:
    print("\n=== Aplikasi Manajemen Proyek ===")
    print("1. Tambah Proyek")
    print("2. Ubah Status Proyek")
    print("3. Tampilkan Daftar Proyek")
    print("4. Laporan Proyek")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama proyek: ")
        anggota = input("Masukkan nama anggota tim: ")
        status = input("Masukkan status proyek (selesai/progres): ")
        tambah_proyek(nama, anggota, status)
    elif pilihan == "2":
        nama = input("Masukkan nama proyek yang statusnya ingin diubah: ")
        status_baru = input("Masukkan status baru proyek: ")
        ubah_status_proyek(nama, status_baru)
    elif pilihan == "3":
        tampilkan_proyek()
    elif pilihan == "4":
        laporan_proyek()
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")