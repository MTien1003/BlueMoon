# Hướng dẫn tạo Feature và đẩy lên Git Repository

## Bước 1: Kiểm tra Git Repository

```bash
# Kiểm tra xem đã có git repo chưa
cd C:\BlueMoon
git status
```

Nếu chưa có git repo, khởi tạo:
```bash
git init
```

## Bước 2: Thêm Remote Repository (nếu chưa có)

```bash
# Thêm remote repository (thay URL bằng repo của bạn)
git remote add origin <URL_REPO_CUA_BAN>
# Ví dụ: git remote add origin https://github.com/username/bluemoon.git
```

## Bước 3: Tạo Feature Branch

```bash
# Tạo và chuyển sang branch mới cho feature users
git checkout -b feature/users-authentication

# Hoặc nếu đã có branch main/master
git checkout -b feature/users-authentication origin/main
```

## Bước 4: Thêm các file đã thay đổi

```bash
# Xem các file đã thay đổi
git status

# Thêm tất cả các file đã thay đổi
git add .

# Hoặc thêm từng file cụ thể:
git add myproject/users/
git add myproject/myproject/urls.py
git add myproject/home/views.py
git add myproject/nhankhau/views.py
git add myproject/templates/authentication-login1.html
git add myproject/templates/users/
git add .gitignore
```

## Bước 5: Commit các thay đổi

```bash
# Commit với message mô tả rõ ràng
git commit -m "feat: Implement user authentication and authorization system

- Add User model with password hashing and role management
- Implement login/logout functionality
- Add user management (CRUD) for admin
- Create permission decorators (@admin_required, @canbo_required)
- Add login page template with Django forms
- Add user list and user form templates
- Protect views with authentication and authorization
- Add management command to create admin user"
```

## Bước 6: Push lên Repository

```bash
# Push branch lên remote repository
git push -u origin feature/users-authentication
```

## Bước 7: Tạo Pull Request (nếu dùng GitHub/GitLab)

1. Vào repository trên GitHub/GitLab
2. Sẽ có thông báo tạo Pull Request
3. Click "Compare & pull request"
4. Điền title và description:
   - **Title**: `feat: Implement user authentication and authorization system`
   - **Description**: Mô tả các tính năng đã thêm
5. Click "Create pull request"

## Các file đã thay đổi trong feature này:

### Models
- `myproject/users/models.py` - User model với authentication

### Views
- `myproject/users/views.py` - Login, logout, user management views
- `myproject/home/views.py` - Thêm authentication
- `myproject/nhankhau/views.py` - Thêm authorization

### Forms
- `myproject/users/forms.py` - LoginForm và UserForm

### Decorators & Mixins
- `myproject/users/decorators.py` - Permission decorators
- `myproject/common/mixins.py` - Permission mixins

### URLs
- `myproject/users/urls.py` - User URLs
- `myproject/myproject/urls.py` - Include user URLs

### Templates
- `myproject/templates/authentication-login1.html` - Login page
- `myproject/templates/users/user_list.html` - User list
- `myproject/templates/users/user_form.html` - User form

### Migrations
- `myproject/users/migrations/0002_*.py` - User model migrations

### Management Commands
- `myproject/users/management/commands/create_admin.py` - Create admin command

## Lưu ý:

1. **Không commit file nhạy cảm**: 
   - `db.sqlite3` (đã có trong .gitignore)
   - `SECRET_KEY` trong settings.py (nên dùng environment variables)

2. **Kiểm tra lại trước khi commit**:
   ```bash
   git status
   git diff  # Xem các thay đổi
   ```

3. **Nếu có conflict khi merge**, giải quyết conflict trước khi push

4. **Best practices**:
   - Commit message rõ ràng, mô tả đầy đủ
   - Mỗi commit nên là một thay đổi logic hoàn chỉnh
   - Test code trước khi commit

