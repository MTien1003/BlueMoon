from django.shortcuts import render, redirect
from .models import NopTien
from hokhau.models import HoKhau
from khoanthu.models import KhoanThu


def hoadon(request):
    """
    Trang danh sách hóa đơn (nộp tiền) cho các khoản thu.
    """
    hoadons = NopTien.objects.select_related('hokhau', 'khoanthu').order_by('-id')
    return render(request, 'hoadon.html', {'hoadons': hoadons})


def create_hoadon(request):
    """
    Trang tạo mới hóa đơn (NopTien).
    Chọn hộ khẩu, khoản thu từ dropdown, nhập người nộp, số tiền, ngày nộp.
    """
    hokhaus = HoKhau.objects.order_by('sohokhau')
    khoanthus = KhoanThu.objects.order_by('tenkhoanthu')

    if request.method == 'POST':
        ho_khau = HoKhau.objects.get(id=request.POST['hokhau'])
        khoan_thu = KhoanThu.objects.get(id=request.POST['khoanthu'])
        hoadon = NopTien(
            hokhau=ho_khau,
            khoanthu=khoan_thu,
            nguoinoptien=request.POST['nguoinoptien'],
            sotien=request.POST['sotien'],
            ngaynop=request.POST['ngaynop'],
        )
        hoadon.save()
        return redirect('hoadon')

    context = {
        'hokhaus': hokhaus,
        'khoanthus': khoanthus,
    }
    return render(request, 'create_hoadon.html', context)
