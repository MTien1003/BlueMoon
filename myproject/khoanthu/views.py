from django.shortcuts import render, redirect
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
