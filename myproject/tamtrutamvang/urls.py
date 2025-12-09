from django.urls import path
from . import views

urlpatterns = [
    # Đường dẫn xem danh sách
    path('tam-tru-tam-vang/', views.danh_sach_tam_tru_tam_vang, name='danh_sach_tttv'),
    
    # Đường dẫn thêm mới
    path('tam-tru-tam-vang/them/', views.them_moi_tttv, name='them_moi_tttv'),
    
    # Đường dẫn sửa
    path('tam-tru-tam-vang/sua/<int:id>/', views.sua_tttv, name='sua_tttv'),
]