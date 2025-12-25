from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import TamTruTamVang
from .forms import TamTruTamVangForm
from django.utils import timezone

# 1. Hàm xem danh sách
def danh_sach_tam_tru_tam_vang(request):
    # Lấy từ khóa, mặc định là rỗng nếu không có
    search_query = request.GET.get('q', '').strip() 
    
    # Bắt đầu với toàn bộ danh sách
    danh_sach = TamTruTamVang.objects.all().order_by('-thoigian')

    if search_query:
        # THUẬT TOÁN: Tìm xâu con không phân biệt hoa thường (icontains)
        # Quét trên 3 trường: Họ tên, Số CCCD, Địa chỉ tạm trú
        danh_sach = danh_sach.filter(
            Q(nhankhau__hoten__icontains=search_query) |       # Tìm theo Tên (VD: gõ 'H' ra 'Hoàng', 'Huy')
            Q(nhankhau__cccd__icontains=search_query) |        # Tìm theo CCCD (VD: gõ '1' ra CCCD có số 1)
            Q(diachitamtrutamvang__icontains=search_query)     # Tìm theo Địa chỉ
        )
    
    filter_type = request.GET.get('filter', '') 
    if filter_type == 'tam_tru':
        # Lọc lấy danh sách Tạm Trú (Ví dụ: trangthai = 'TAM_TRU')
        danh_sach = danh_sach.filter(trangthai='tam tru')
        
    elif filter_type == 'tam_vang':
        # Lọc lấy danh sách Tạm Vắng (Ví dụ: trangthai = 'TAM_VANG')
        danh_sach = danh_sach.filter(trangthai='tam vang')
    # 4. Xử lý tìm kiếm (Nếu có nhập từ khóa)
    if search_query:
        danh_sach = danh_sach.filter(nhankhau__hoten__icontains=search_query)
    context = {
        'danh_sach': danh_sach,
        'current_filter': filter_type,
        'search_query': search_query
    }

    return render(request, 'tam_tru_tam_vang/index.html', context)

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

def in_phieu_tttv(request, id):
    # Lấy hồ sơ theo ID
    ho_so = get_object_or_404(TamTruTamVang, pk=id)
    
    # Trả về giao diện in riêng biệt
    return render(request, 'tam_tru_tam_vang/print.html', {'item': ho_so})

