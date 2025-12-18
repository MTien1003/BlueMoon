from django.shortcuts import render
from .models import KhoanThu

# Create your views here.
def khoanthu(request):
    khoanthus = KhoanThu.objects.order_by("-id")
    return render(request, 'khoanthu.html', {'khoanthus': khoanthus})
