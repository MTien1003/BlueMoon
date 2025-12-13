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
            'placeholder': 'Nhập mật khẩu'
        }),
        required=False,  # Sẽ validate trong clean() method
        label='Mật khẩu',
        help_text='Bắt buộc khi tạo user mới. Để trống nếu không muốn đổi mật khẩu khi chỉnh sửa.'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Xác nhận mật khẩu'
        }),
        required=False,  # Sẽ validate trong clean() method
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
        
        # Kiểm tra nếu đang tạo user mới (instance chưa có pk)
        is_new_user = self.instance.pk is None
        
        # Nếu tạo user mới, password là bắt buộc
        if is_new_user:
            if not password:
                raise forms.ValidationError({
                    'password': 'Mật khẩu là bắt buộc khi tạo user mới.'
                })
            if not password_confirm:
                raise forms.ValidationError({
                    'password_confirm': 'Vui lòng xác nhận mật khẩu.'
                })
        
        # Kiểm tra password nếu có nhập (tạo mới hoặc đổi mật khẩu)
        if password or password_confirm:
            if password != password_confirm:
                raise forms.ValidationError({
                    'password_confirm': 'Mật khẩu xác nhận không khớp.'
                })
            if len(password) < 6:
                raise forms.ValidationError({
                    'password': 'Mật khẩu phải có ít nhất 6 ký tự.'
                })
        elif is_new_user:
            # Trường hợp này không nên xảy ra vì đã check ở trên, nhưng để chắc chắn
            raise forms.ValidationError({
                'password': 'Mật khẩu là bắt buộc khi tạo user mới.'
            })

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        
        # Nếu tạo user mới, password phải có (đã validate trong clean())
        # Nếu chỉnh sửa, chỉ set password nếu có nhập
        if password:
            user.set_password(password)
        elif user.pk is None:
            # Trường hợp này không nên xảy ra vì đã validate trong clean()
            # Nhưng để chắc chắn, raise error
            raise ValueError('Password is required when creating a new user.')
        
        if commit:
            user.save()
        return user

