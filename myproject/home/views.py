from django.shortcuts import render
from nhankhau.services import get_total_nhankhau
from tamtrutamvang.views import dem_tam_tru_tam_vang

def home(request):
    total_nhankhau = get_total_nhankhau()
    so_luong_tam_tru, so_luong_tam_vang = dem_tam_tru_tam_vang()
    username = request.user.username
    return render(request, 'index.html', {'total_nhankhau': total_nhankhau, 'username': username, 'so_luong_tam_tru': so_luong_tam_tru, 'so_luong_tam_vang': so_luong_tam_vang})

def firstpage(request):
    return render(request, 'firstpage.html')