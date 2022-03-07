
class originalCharacter:
    jumlahOC = 0

    def __init__(self, nama, ras):
        self.nama = nama
        self.ras = ras
        originalCharacter.jumlahOC += 1

    def menampilkan():
        print("Jumlah OC : {}".format(originalCharacter.jumlahOC))
