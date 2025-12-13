from django.shortcuts import render
from users.decorators import totruong_required

@totruong_required
def nhankhau(request):
    """Quản lý nhân khẩu - Chỉ tổ trưởng/tổ phó (admin/canbo)"""
    return render(request, 'nhankhau.html')
