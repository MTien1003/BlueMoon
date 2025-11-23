from django.db import models

from nhankhau.models import NhanKhau

# Create your models here.
class HoKhau(models.Model):
    sohokhau = models.CharField(max_length=20, unique=True)
    sonha = models.CharField(max_length=100)
    duong = models.CharField(max_length=100)
    phuong = models.CharField(max_length=100)
    quan = models.CharField(max_length=100)
    ngaylamhokhau = models.DateField()
    chuhokhau = models.OneToOneField(NhanKhau, on_delete=models.PROTECT)
    sothanhvien = models.IntegerField()
    
    def __str__(self):
        return f"Hokhau {self.sohokhau} - Chu ho: {self.chuhokhau.hoten}"

class ThanhVienHoKhau(models.Model):
    hokhau = models.ForeignKey(HoKhau, on_delete=models.CASCADE)
    nhankhau = models.ForeignKey(NhanKhau, on_delete=models.PROTECT)
    quanhevoichuho = models.CharField(max_length=100)
    ngaythemnhankhau = models.DateField()
    
    def __str__(self):
        return f"Thanh vien: {self.nhankhau.hoten} - Quan he voi chu ho: {self.quanhevoichuho}"
    
class LichSuThayDoiHoKhau(models.Model):
    hokhau = models.ForeignKey(HoKhau, on_delete=models.CASCADE)
    nhankhau = models.ForeignKey(NhanKhau, on_delete=models.PROTECT)
    loaithaydoi = models.IntegerField(choices=[(1, 'Them thanh vien'),(2, 'Xoa thanh vien')])
    ngaythaydoi = models.DateTimeField()
    
    def __str__(self):
        return f"Lich su thay doi hokhau {self.hokhau.sohokhau} ngay {self.ngaythaydoi}"