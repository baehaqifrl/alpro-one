# --------------- input -----------------
member = input("Apakah Anda anggota? (ya/tidak): ").lower()
total_belanja = float(input("Masukkan total belanja: "))
diskon = int()

# --------------- proses -----------------
if member == "ya":
    if total_belanja >= 200000:
        diskon = 15
    else:
        diskon = 10
else:
    if total_belanja >= 200000:
        diskon = 5
    else:
        diskon = 0

nominal_diskon = total_belanja * diskon / 100
total_bayar = total_belanja - nominal_diskon

# --------------- output ---------------
print(f"Diskon: {diskon}%")
print(f"Nominal diskon: Rp{nominal_diskon:,.0f}")
print(f"Total pembayaran: Rp{total_bayar:,.0f}")