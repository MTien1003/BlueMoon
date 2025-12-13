from django import forms
from .models import User


class LoginForm(forms.Form):
    """Form đăng nhập"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'uname',
            'placeholder': 'Nhập tên đăng nhập',
            'required': True
        }),
        label='Tên đăng nhập'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'pwd',
            'placeholder': 'Nhập mật khẩu',
            'required': True
        }),
        label='Mật khẩu'
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    raise forms.ValidationError('Tên đăng nhập hoặc mật khẩu không đúng.')
                if not user.is_active:
                    raise forms.ValidationError('Tài khoản này đã bị khóa.')
            except User.DoesNotExist:
                raise forms.ValidationError('Tên đăng nhập hoặc mật khẩu không đúng.')

        return cleaned_data


class UserForm(forms.ModelForm):
    """Form tạo/chỉnh sửa user"""
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nhập mật khẩu (để trống nếu không đổi)'
        }),
        required=False,
        label='Mật khẩu'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Xác nhận mật khẩu'
        }),
        required=False,
        label='Xác nhận mật khẩu'
    )

    class Meta:
        model = User
        fields = ['username', 'vaitro', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên đăng nhập'
            }),
            'vaitro': forms.Select(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'username': 'Tên đăng nhập',
            'vaitro': 'Vai trò',
            'is_active': 'Kích hoạt',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password or password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Mật khẩu xác nhận không khớp.')
            if len(password) < 6:
                raise forms.ValidationError('Mật khẩu phải có ít nhất 6 ký tự.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

