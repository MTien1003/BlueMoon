from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def login_required_custom(view_func):
    """Decorator kiểm tra user đã đăng nhập chưa"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'user_id' not in request.session:
            messages.warning(request, 'Vui lòng đăng nhập để truy cập trang này.')
            return redirect('login')
        
        # Lấy user từ session
        try:
            from .models import User
            user = User.objects.get(id=request.session['user_id'], is_active=True)
            request.user = user
        except User.DoesNotExist:
            request.session.flush()
            messages.error(request, 'Phiên đăng nhập đã hết hạn.')
            return redirect('login')
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def admin_required(view_func):
    """Decorator kiểm tra user có phải admin không"""
    @wraps(view_func)
    @login_required_custom
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_admin:
            messages.error(request, 'Bạn không có quyền truy cập trang này.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def canbo_required(view_func):
    """Decorator kiểm tra user có phải cán bộ hoặc admin không"""
    @wraps(view_func)
    @login_required_custom
    def _wrapped_view(request, *args, **kwargs):
        if not (request.user.is_admin or request.user.is_canbo):
            messages.error(request, 'Bạn không có quyền truy cập trang này.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def ketoan_required(view_func):
    """Decorator kiểm tra user có phải kế toán không"""
    @wraps(view_func)
    @login_required_custom
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_ketoan:
            messages.error(request, 'Bạn không có quyền truy cập trang này. Chỉ kế toán mới được truy cập.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def totruong_required(view_func):
    """Decorator kiểm tra user có phải tổ trưởng/tổ phó không (admin hoặc canbo)"""
    @wraps(view_func)
    @login_required_custom
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_totruong:
            messages.error(request, 'Bạn không có quyền truy cập trang này. Chỉ tổ trưởng/tổ phó mới được truy cập.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

