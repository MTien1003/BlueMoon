from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TamTruTamVang
from .forms import TamTruTamVangForm

# 1. Hàm xem danh sách (Đây chính là hàm mà Django đang tìm kiếm)
def danh_sach_tam_tru_tam_vang(request):
    # Lấy tất cả hồ sơ, sắp xếp mới nhất lên đầu
    danh_sach = TamTruTamVang.objects.all().order_by('-thoigian')
    return render(request, 'tam_tru_tam_vang/index.html', {'danh_sach': danh_sach})

# 2. Hàm thêm mới
def them_moi_tttv(request):
    if request.method == 'POST':
        form = TamTruTamVangForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đã thêm hồ sơ thành công!')
            return redirect('danh_sach_tttv')
    else:
        form = TamTruTamVangForm()
    
    return render(request, 'tam_tru_tam_vang/form.html', {'form': form, 'title': 'Đăng ký mới'})

# 3. Hàm sửa
def sua_tttv(request, id):
    ho_so = get_object_or_404(TamTruTamVang, pk=id)
    if request.method == 'POST':
        form = TamTruTamVangForm(request.POST, instance=ho_so)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật thành công!')
            return redirect('danh_sach_tttv')
    else:
        form = TamTruTamVangForm(instance=ho_so)
        
    return render(request, 'tam_tru_tam_vang/form.html', {'form': form, 'title': 'Cập nhật hồ sơ'})