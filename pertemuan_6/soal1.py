# --------------- input -----------------
status_mahasigma = input("Apakah Anda mahasiswa aktif? (ya/tidak): ").lower()
reservasi = input("Apakah Anda memiliki reservasi? (ya/tidak): ").lower()

# --------------- proses & output ---------------
if status_mahasigma == "ya":
    if reservasi == "ya":
        print("Diizinkan masuk")
    else:
        print("Silakan melakukan reservasi")
else:
   print("Akses ditolak")