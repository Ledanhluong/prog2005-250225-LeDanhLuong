class SinhVien:
    dem = 0

    def __init__(self, name):
        self.name = name
        SinhVien.dem += 1

    @classmethod
    def so_luong(cls):
        return cls.dem


sv1 = SinhVien("Luong")
sv2 = SinhVien("Long")
sv3 = SinhVien("Tu")

print