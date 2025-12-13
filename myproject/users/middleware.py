from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse


class AuthenticationMiddleware(MiddlewareMixin):
    """Middleware để thêm user vào request từ session"""
    
    def process_request(self, request):
        # Bỏ qua các URL không cần authentication
        public_urls = ['/login/', '/admin/', '/static/', '/media/']
        if any(request.path.startswith(url) for url in public_urls):
            return None
        
        # Kiểm tra session
        if 'user_id' in request.session:
            try:
                from .models import User
                user = User.objects.get(
                    id=request.session['user_id'],
                    is_active=True
                )
                request.user = user
            except User.DoesNotExist:
                # User không tồn tại hoặc đã bị khóa
                request.session.flush()
                request.user = None
        else:
            request.user = None
        
        return None

