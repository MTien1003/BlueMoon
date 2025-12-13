from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import User
from .forms import LoginForm, UserForm
from .decorators import login_required_custom, admin_required, canbo_required


def login_view(request):
    """View đăng nhập"""
    # Kiểm tra nếu đã đăng nhập
    if 'user_id' in request.session:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
                if user.check_password(password) and user.is_active:
                    # Lưu user vào session
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    request.session['vaitro'] = user.vaitro
                    
                    # Cập nhật last_login
                    from django.utils import timezone
                    user.last_login = timezone.now()
                    user.save(update_fields=['last_login'])
                    
                    messages.success(request, f'Chào mừng {user.username}!')
                    
                    # Redirect dựa trên vai trò
                    next_url = request.GET.get('next', 'home')
                    return redirect(next_url)
                else:
                    messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
            except User.DoesNotExist:
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
    else:
        form = LoginForm()
    
    return render(request, 'authentication-login1.html', {'form': form})


def logout_view(request):
    """View đăng xuất"""
    request.session.flush()
    messages.success(request, 'Bạn đã đăng xuất thành công.')
    return redirect('login')


@admin_required
def user_list(request):
    """Danh sách users - chỉ tổ trưởng/tổ phó (admin)"""
    users = User.objects.all().order_by('-date_joined')
    
    # Phân trang
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'users': page_obj,
    }
    return render(request, 'users/user_list.html', context)


@admin_required
def user_create(request):
    """Tạo user mới - chỉ tổ trưởng/tổ phó (admin)"""
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Đã tạo user {user.username} thành công.')
            return redirect('user_list')
    else:
        form = UserForm()
    
    context = {
        'form': form,
        'title': 'Tạo người dùng mới',
    }
    return render(request, 'users/user_form.html', context)


@admin_required
def user_edit(request, user_id):
    """Chỉnh sửa user - chỉ tổ trưởng/tổ phó (admin)"""
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'Không tìm thấy user.')
        return redirect('user_list')
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Đã cập nhật user {user.username} thành công.')
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    
    context = {
        'form': form,
        'user': user,
        'title': 'Chỉnh sửa người dùng',
    }
    return render(request, 'users/user_form.html', context)


@admin_required
def user_delete(request, user_id):
    """Xóa user - chỉ tổ trưởng/tổ phó (admin)"""
    
    try:
        user = User.objects.get(id=user_id)
        if user.id == request.user.id:
            messages.error(request, 'Bạn không thể xóa chính mình.')
        else:
            username = user.username
            user.delete()
            messages.success(request, f'Đã xóa user {username} thành công.')
    except User.DoesNotExist:
        messages.error(request, 'Không tìm thấy user.')
    
    return redirect('user_list')
