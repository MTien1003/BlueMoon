from django import forms
from .models import TamTruTamVang

class TamTruTamVangForm(forms.ModelForm):
    class Meta:
        model = TamTruTamVang
        fields = ['nhankhau', 'trangthai', 'diachitamtrutamvang', 'thoigian', 'noidungdenghi']
        
        widgets = {
            # Tạo giao diện đẹp cho các ô nhập liệu
            'nhankhau': forms.Select(attrs={'class': 'form-control'}),
            'trangthai': forms.Select(choices=[('tam tru', 'Tạm trú'), ('tam vang', 'Tạm vắng')], attrs={'class': 'form-control'}),
            'diachitamtrutamvang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập địa chỉ...'}),
            'thoigian': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'noidungdenghi': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }