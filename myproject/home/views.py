from django.shortcuts import render
from nhankhau.services import get_total_nhankhau

def home(request):
    total_nhankhau = get_total_nhankhau()
    return render(request, 'index.html', {'total_nhankhau': total_nhankhau})

def firstpage(request):
    return render(request, 'firstpage.html')