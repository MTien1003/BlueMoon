from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime
from nhankhau.services import get_total_nhankhau
from noptien.models import NopTien


def get_doanhthu_thang_nay():
    """
    Tính tổng doanh thu tháng này từ các hóa đơn đã thanh toán trong tháng hiện tại.
    """
    from datetime import date
    today = date.today()
    start_of_month = date(today.year, today.month, 1)
    
    # Tính ngày đầu tháng sau để làm end date
    if today.month == 12:
        end_of_month = date(today.year + 1, 1, 1)
    else:
        end_of_month = date(today.year, today.month + 1, 1)
    
    total = NopTien.objects.filter(
        ngaynop__isnull=False,
        ngaynop__gte=start_of_month,
        ngaynop__lt=end_of_month
    ).aggregate(
        total=Sum('sotien')
    )['total'] or 0
    return total


def format_currency(value):
    """
    Format số tiền với dấu chấm phân cách hàng nghìn.
    Ví dụ: 1450100 -> 1.450.100
    """
    if value is None:
        return "0"
    try:
        num = int(float(value))
        return f"{num:,}".replace(",", ".")
    except (ValueError, TypeError):
        return "0"


def home(request):
    total_nhankhau = get_total_nhankhau()
    doanhthu_thang_nay = get_doanhthu_thang_nay()
    doanhthu_formatted = format_currency(doanhthu_thang_nay)
    
    return render(request, 'index.html', {
        'total_nhankhau': total_nhankhau,
        'doanhthu_thang_nay': doanhthu_thang_nay,
        'doanhthu_formatted': doanhthu_formatted
    })
