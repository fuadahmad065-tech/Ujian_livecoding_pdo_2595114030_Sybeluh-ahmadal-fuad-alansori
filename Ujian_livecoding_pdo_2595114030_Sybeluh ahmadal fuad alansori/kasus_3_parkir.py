class KendaraanParkir:
    def __init__(self, jenis, durasi):
        if durasi <= 0: raise ValueError("Durasi harus lebih dari 0")
        self.jenis = jenis.lower()
        self.durasi = durasi
        self.tarif_dasar = 3000 if self.jenis == "motor" else 5000
        
    def hitung_biaya(self):
        return self.tarif_dasar * self.durasi
        
    def hitung_denda(self):
        return 10000 if self.durasi > 5 else 0
        
    def tampilkan_struk(self):
        biaya = self.hitung_biaya()
        denda = self.hitung_denda()
        admin = 2000
        total = biaya + denda + admin
        print(f"=== STRUK PARKIR ===\nJenis       : {self.jenis.capitalize()}\nDurasi      : {self.durasi} jam")
        print(f"Biaya Dasar : Rp{biaya:,.0f}\nDenda       : Rp{denda:,.0f}\nBiaya Admin : Rp{admin:,.0f}")
        print(f"Total bayar : Rp{total:,.0f}\n====================")

print("=== SISTEM PARKIR ===")
try:
    jenis = input("Jenis kendaraan (motor/mobil) : ")
    if jenis.lower() not in ["motor", "mobil"]: raise ValueError("Jenis tidak valid")
    k = KendaraanParkir(jenis, int(input("Durasi parkir (jam) : ")))
    k.tampilkan_struk()
except ValueError as e: print(f"Error: {e}")
        

