from abc import ABC, abstractmethod

# Abstraksi

class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


class PoinTidakValidError(Exception):
    """Custom exception untuk poin negatif."""
    pass


class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        return "Hak akses: Member dapat mengakses fitur premium."

    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# PROGRAM UTAMA

def input_poin():
    """Meminta input poin dari user dengan validasi dan exception."""
    while True:
        try:
            nilai = input("Masukkan poin: ").strip()

            if nilai == "":
                raise ValueError("Input tidak boleh kosong!")

            if not nilai.isdigit() and not (nilai.startswith('-') and nilai[1:].isdigit()):
                raise ValueError("Input harus berupa angka!")

            angka = int(nilai)

            if angka < 0:
                raise PoinTidakValidError("Poin tidak boleh negatif!")

            return angka

        except ValueError as ve:
            print("Kesalahan:", ve)

        except PoinTidakValidError as pe:
            print("Kesalahan:", pe)


if __name__ == "__main__":

    print("=== Input Member 1 ===")
    nama1 = input("Masukkan nama: ")
    poin1 = input_poin()

    print("\n=== Input Member 2 ===")
    nama2 = input("Masukkan nama: ")
    poin2 = input_poin()

    # Membuat objek
    m1 = Member(nama1, poin1)
    m2 = Member(nama2, poin2)

    print("\n=== HASIL ===")
    print(m1)
    print(m2)

    print("\nJumlah poin (m1 + m2):", m1 + m2)
    print("Panjang nama member 1:", len(m1))
