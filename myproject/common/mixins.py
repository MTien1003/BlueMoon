from django.shortcuts import redirect
from django.contrib import messages


class LoginRequiredMixin:
    """Mixin yêu cầu đăng nhập"""
    
    def dispatch(self, request, *args, **kwargs):
        if 'user_id' not in request.session:
            messages.warning(request, 'Vui lòng đăng nhập để truy cập trang này.')
            return redirect('login')
        
        try:
            from users.models import User
            user = User.objects.get(id=request.session['user_id'], is_active=True)
            request.user = user
        except User.DoesNotExist:
            request.session.flush()
            messages.error(request, 'Phiên đăng nhập đã hết hạn.')
            return redirect('login')
        
        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin(LoginRequiredMixin):
    """Mixin yêu cầu quyền admin"""
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if hasattr(response, 'status_code') and response.status_code == 302:
            return response
        
        if not request.user.is_admin:
            messages.error(request, 'Bạn không có quyền truy cập trang này.')
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)


class CanBoRequiredMixin(LoginRequiredMixin):
    """Mixin yêu cầu quyền cán bộ hoặc admin"""
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if hasattr(response, 'status_code') and response.status_code == 302:
            return response
        
        if not (request.user.is_admin or request.user.is_canbo):
            messages.error(request, 'Bạn không có quyền truy cập trang này.')
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)


class ToTruongRequiredMixin(LoginRequiredMixin):
    """Mixin yêu cầu quyền tổ trưởng/tổ phó (admin hoặc canbo)"""
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if hasattr(response, 'status_code') and response.status_code == 302:
            return response
        
        if not request.user.is_totruong:
            messages.error(request, 'Bạn không có quyền truy cập trang này. Chỉ tổ trưởng/tổ phó mới được truy cập.')
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)


class KeToanRequiredMixin(LoginRequiredMixin):
    """Mixin yêu cầu quyền kế toán"""
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if hasattr(response, 'status_code') and response.status_code == 302:
            return response
        
        if not request.user.is_ketoan:
            messages.error(request, 'Bạn không có quyền truy cập trang này. Chỉ kế toán mới được truy cập.')
            return redirect('home')
        
        return super().dispatch(request, *args, **kwargs)

