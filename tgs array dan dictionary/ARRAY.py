# NAMA : Nopal
# NIM : D0425005
# SISTEM INFORMASI B

mahasiswa = {
    "nama": "Nopal",
    "nim": "D0425005",
    "jurusan": "Teknik Sistem Informasi",
    "kelas": " B ",
    "angkatan": 2025,
    "alamat": "kalumammang, Sulawesi Barat",

    "nilai": {
        "algoritma_pemrograman": 98,
        "struktur_data": 78,
        "basis_data": 80,
        "pemrograman_python": 90
    },

    "mata_kuliah_diambil": [
        "Algoritma Pemrograman",
        "Basis Data",
        "Pemrograman Python",
        "Kalkulus Informatika"
    ]
}

# Menampilkan seluruh data
print("\nData Mahasiswa:", mahasiswa)

# Mengakses data
print("Nama:", mahasiswa["nama"])
print("Kelas:", mahasiswa["kelas"])
print("Nilai Python:", mahasiswa["nilai"]["pemrograman_python"])

# Update nilai
mahasiswa["nilai"]["pemrograman_python"] = 98
print("Nilai Python Setelah Update:", mahasiswa["nilai"]["pemrograman_python"])