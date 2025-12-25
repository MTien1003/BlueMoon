from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, date
from calendar import month_abbr
import json
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


def get_doanhthu_theo_thang():
    """
    Tính doanh thu theo từng tháng trong 6 tháng gần nhất.
    Trả về dict với key là tên tháng (Jan, Feb, ...) và value là doanh thu.
    """
    today = date.today()
    doanhthu_thang = {}
    
    # Lấy 6 tháng gần nhất
    for i in range(5, -1, -1):  # 5 tháng trước đến tháng hiện tại
        month = today.month - i
        year = today.year
        
        # Xử lý trường hợp tháng < 1 (lùi về năm trước)
        while month < 1:
            month += 12
            year -= 1
        
        # Tính ngày đầu và cuối tháng
        start_of_month = date(year, month, 1)
        if month == 12:
            end_of_month = date(year + 1, 1, 1)
        else:
            end_of_month = date(year, month + 1, 1)
        
        # Tính doanh thu tháng này
        total = NopTien.objects.filter(
            ngaynop__isnull=False,
            ngaynop__gte=start_of_month,
            ngaynop__lt=end_of_month
        ).aggregate(
            total=Sum('sotien')
        )['total'] or 0
        
        # Lấy tên tháng (Jan, Feb, ...)
        month_name = month_abbr[month]
        doanhthu_thang[month_name] = float(total)
    
    return doanhthu_thang


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
    doanhthu_theo_thang = get_doanhthu_theo_thang()
    
    # Chuyển đổi sang format cho biểu đồ: labels và series
    labels = list(doanhthu_theo_thang.keys())
    # Chuyển doanh thu sang đơn vị triệu VND để dễ hiển thị (chia cho 1,000,000)
    series = [[value / 1000000 for value in doanhthu_theo_thang.values()]]
    
    return render(request, 'index.html', {
        'total_nhankhau': total_nhankhau,
        'doanhthu_thang_nay': doanhthu_thang_nay,
        'doanhthu_formatted': doanhthu_formatted,
        'chart_labels': json.dumps(labels),
        'chart_series': json.dumps(series)
    })
