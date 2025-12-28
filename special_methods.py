class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    def __len__(self):
        return len(self.nama)

    def __eq__(self, other):
        return self.nilai == other.nilai


# Contoh penggunaan

m1 = Mahasiswa("Adi", 80)
m2 = Mahasiswa("Suci", 90)
m3 = Mahasiswa("Dina", 90)   

print("=== Representasi String ===")
print(m1)
print(m2)
print(m3)

print("\n=== Panjang Nama ===")
print(f"len(m1) = {len(m1)}")
print(f"len(m2) = {len(m2)}")

print("\n=== Perbandingan Kesetaraan Nilai (==) ===")
print("m2 == m3 ?", m2 == m3)  
print("m1 == m2 ?", m1 == m2)

print("\n=== Operasi Matematika ===")
print("m1 + m2 =", m1 + m2)
print("m2 * 2  =", m2 * 2)

print("\n=== Mengurutkan Mahasiswa Berdasarkan Nilai ===")
list_mhs = [m1, m2, m3]
sorted_list = sorted(list_mhs, key=lambda x: x.nilai)

for m in sorted_list:
    print(m)
