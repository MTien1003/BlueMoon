from django.shortcuts import render
from .models import NopTien


def hoadon(request):
    """
    Trang danh sách hóa đơn (nộp tiền) cho các khoản thu.
    """
    hoadons = NopTien.objects.select_related('hokhau', 'khoanthu').order_by('-id')
    return render(request, 'hoadon.html', {'hoadons': hoadons})
