# Input
berkas_lengkap = input("Apakah berkas lengkap? (ya/tidak): ").lower()
nilai_tes = float(input("Masukkan nilai tes (0-100): "))
pernah_lomba = input("Pernah mengikuti lomba? (ya/tidak): ").lower()

# Proses & Output
if berkas_lengkap != "ya":
    print("Tidak lolos administrasi")
else:
    if nilai_tes >= 85:
        if pernah_lomba == "ya":
            print("Lolos tim utama")
        else:
            print("Lolos tim pembinaan")
    elif nilai_tes >= 70:
        if pernah_lomba == "ya":
            print("Lolos tim pembinaan")
        else:
            print("Masuk daftar cadangan")
    else:
        print("Tidak lolos seleksi")