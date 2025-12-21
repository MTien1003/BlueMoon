from django.shortcuts import render, redirect, get_object_or_404
from .models import KhoanThu

# Create your views here.
def khoanthu(request):
    khoanthus = KhoanThu.objects.order_by("-id")
    return render(request, 'khoanthu.html', {'khoanthus': khoanthus})


def create_khoanthu(request):
    """
    Trang tạo mới KhoanThu.
    Nhận dữ liệu từ form và lưu vào database, sau đó quay lại danh sách khoản thu.
    """
    if request.method == 'POST':
        khoanthu = KhoanThu(
            tenkhoanthu=request.POST['tenkhoanthu'],
            ngaytao=request.POST['ngaytao'],
            thoihan=request.POST['thoihan'],
            batbuoc=bool(request.POST.get('batbuoc')),
            ghichu=request.POST.get('ghichu', ''),
            sotien=request.POST['sotien'],
        )
        khoanthu.save()
        return redirect('khoanthu')

    return render(request, 'create_khoanthu.html')


def xem_khoanthu(request, id):
    """Xem chi tiết một khoản thu."""
    khoanthu = get_object_or_404(KhoanThu, id=id)
    return render(request, 'xem_khoanthu.html', {'khoanthu': khoanthu})


def update_khoanthu(request, id):
    """Cập nhật thông tin một khoản thu."""
    khoanthu = get_object_or_404(KhoanThu, id=id)

    if request.method == 'POST':
        khoanthu.tenkhoanthu = request.POST['tenkhoanthu']
        khoanthu.ngaytao = request.POST['ngaytao']
        khoanthu.thoihan = request.POST['thoihan']
        khoanthu.batbuoc = bool(request.POST.get('batbuoc'))
        khoanthu.ghichu = request.POST.get('ghichu', '')
        khoanthu.sotien = request.POST['sotien']
        khoanthu.save()
        return redirect('khoanthu')

    return render(request, 'update_khoanthu.html', {'khoanthu': khoanthu})
