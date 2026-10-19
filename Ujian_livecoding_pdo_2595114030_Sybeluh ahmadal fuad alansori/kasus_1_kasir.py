class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga, jumlah):
        if harga <= 0 or jumlah <= 0: raise ValueError("Harga & jumlah harus > 0")
        self.pelanggan, self.barang, self.harga, self.jumlah = pelanggan, barang, harga, jumlah
    
    def hitung_subtotal(self): return self.harga * self.jumlah
        
    def hitung_diskon(self):
        sub = self.hitung_subtotal()
        if sub >= 500000: return 0.15
        elif sub >= 250000: return 0.10
        elif sub >= 100000: return 0.05
        return 0
        
    def tampilkan_struk(self):
        sub = self.hitung_subtotal()
        diskon = self.hitung_diskon()
        potongan = sub * diskon
        total = sub - potongan
        print(f"=== STRUK PEMBAYARAN ===\nPelanggan : {self.pelanggan}\nBarang    : {self.barang}")
        print(f"Subtotal  : Rp{sub:,.0f}\nDiskon    : {int(diskon*100)}%\nPotongan  : Rp{potongan:,.0f}")
        print(f"Total bayar : Rp{total:,.0f}\n====================")

print("=== KASIR MINIMARKET ===")
try:
    t = TransaksiKasir(input("Nama pelanggan : "), input("Nama barang    : "), int(input("Harga barang   : ")), int(input("Jumlah barang  : ")))
    t.tampilkan_struk()
except ValueError as e: print(f"Error: {e}")

        
