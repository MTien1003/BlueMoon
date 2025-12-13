from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, vaitro='user', **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, vaitro=vaitro, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, vaitro='admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, vaitro, **extra_fields)


class User(models.Model):
    VAITRO_CHOICES = [
        ('admin', 'Tổ trưởng/Tổ phó'),
        ('canbo', 'Cán bộ'),
        ('ketoan', 'Kế toán'),
        ('user', 'Người dùng'),
    ]
    
    username = models.CharField(max_length=150, unique=True, verbose_name='Tên đăng nhập')
    password = models.CharField(max_length=128, verbose_name='Mật khẩu')
    vaitro = models.CharField(max_length=50, choices=VAITRO_CHOICES, default='user', verbose_name='Vai trò')
    is_active = models.BooleanField(default=True, verbose_name='Kích hoạt')
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Ngày tham gia')
    last_login = models.DateTimeField(null=True, blank=True, verbose_name='Đăng nhập lần cuối')

    objects = UserManager()

    class Meta:
        verbose_name = 'Người dùng'
        verbose_name_plural = 'Người dùng'

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        """Hash password (không tự động save)"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Kiểm tra password"""
        return check_password(raw_password, self.password)

    def is_authenticated(self):
        """Kiểm tra user đã đăng nhập"""
        return True

    def is_anonymous(self):
        """Kiểm tra user chưa đăng nhập"""
        return False

    @property
    def is_admin(self):
        """Kiểm tra user có phải admin không"""
        return self.vaitro == 'admin'

    @property
    def is_canbo(self):
        """Kiểm tra user có phải cán bộ không"""
        return self.vaitro == 'canbo'

    @property
    def is_ketoan(self):
        """Kiểm tra user có phải kế toán không"""
        return self.vaitro == 'ketoan'
    
    @property
    def is_totruong(self):
        """Kiểm tra user có phải tổ trưởng/tổ phó không (admin hoặc canbo)"""
        return self.vaitro in ['admin', 'canbo']

    def has_perm(self, perm, obj=None):
        """Kiểm tra quyền - chỉ admin mới có quyền"""
        return self.vaitro == 'admin'

    def has_module_perms(self, app_label):
        """Kiểm tra quyền module"""
        return self.vaitro == 'admin'