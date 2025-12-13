from django.shortcuts import render
from users.decorators import ketoan_required

# Create your views here.

@ketoan_required
def khoanthu(request):
    """Quản lý khoản thu - Chỉ kế toán"""
    return render(request, 'khoanthu.html')
