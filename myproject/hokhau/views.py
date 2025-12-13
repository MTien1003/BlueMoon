from django.shortcuts import render
from users.decorators import totruong_required

# Create your views here.

@totruong_required
def hokhau(request):
    """Quản lý hộ khẩu - Chỉ tổ trưởng/tổ phó (admin/canbo)"""
    return render(request, 'hokhau.html')
