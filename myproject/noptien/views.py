from django.shortcuts import render
from users.decorators import ketoan_required

# Create your views here.

@ketoan_required
def noptien(request):
    """Quản lý nộp tiền - Chỉ kế toán"""
    return render(request, 'noptien.html')
