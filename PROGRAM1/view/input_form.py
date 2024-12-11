

class InputForm:
    def __init__(self):
        self.nim = ""
        self.nama = ""
        self.jurusan = ""

    def input_data(self):
        self.nim = input("Masukkan NIM: ")
        self.nama = input("Masukkan Nama: ")
        self.jurusan = input("Masukkan Jurusan: ")
        return self.nim, self.nama, self.jurusan