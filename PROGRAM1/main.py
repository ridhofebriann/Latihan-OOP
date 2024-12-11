from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def main():
    data_mahasiswa = DataMahasiswa()
    input_form = InputForm()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Cari Data Mahasiswa")
        print("5. Tampilkan Semua Data Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            nim, nama, jurusan = input_form.input_data()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_data(mahasiswa)
            print("Data mahasiswa berhasil ditambahkan.")

        elif pilihan == '2':
            nim = input("Masukkan NIM yang ingin dihapus: ")
            data_mahasiswa.hapus_data(nim)
            print("Data mahasiswa berhasil dihapus.")

        elif pilihan == '3':
            nim = input("Masukkan NIM yang ingin diubah: ")
            nama = input("Masukkan Nama baru (tekan enter jika tidak ingin mengubah): ")
            jurusan = input("Masukkan Jurusan baru (tekan enter jika tidak ingin mengubah): ")
            data_mahasiswa.ubah_data(nim, nama if nama else None, jurusan if jurusan else None)
            print("Data mahasiswa berhasil diubah.")

        elif pilihan == '4':
            nim = input("Masukkan NIM yang ingin dicari: ")
            mahasiswa = data_mahasiswa.cari_data(nim)
            if mahasiswa:
                print("+-----------------+-----------------+-----------------+")
                print("| NIM             | Nama            | Jurusan         |")
                print("+-----------------+-----------------+-----------------+")
                print("| {:15s} | {:15s} | {:15s} |".format(mahasiswa.nim, mahasiswa.nama, mahasiswa.jurusan))
                print("+-----------------+-----------------+-----------------+")
            else:
                print("Data mahasiswa tidak ditemukan.")

        elif pilihan == '5':
            mahasiswa_list = data_mahasiswa.tampilkan_data()
            if mahasiswa_list:
                print("+-----+-----------------+-----------------+-----------------+")
                print("| No. | NIM             | Nama            | Jurusan         |")
                print("+-----+-----------------+-----------------+-----------------+")
                for i, mahasiswa in enumerate(mahasiswa_list, start=1):
                    print("| {:<3} | {:<15s} | {:<15s} | {:<15s} |".format(i, mahasiswa.nim, mahasiswa.nama, mahasiswa.jurusan))
                print("+-----+-----------------+-----------------+-----------------+")
            else:
                print("+-------------------------------------------------------------+")
                print("|                         TIDAK ADA DATA                       |")
                print("+-------------------------------------------------------------+")

        elif pilihan == '6':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()