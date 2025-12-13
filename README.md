# BlueMoon - Hệ thống quản lý dân cư

Dự án Django quản lý hộ khẩu, nhân khẩu, khoản thu, nộp tiền và tạm trú tạm vắng.

## Yêu cầu hệ thống

- Python 3.8 trở lên
- PostgreSQL (hoặc có thể chuyển sang SQLite)
- pip (Python package manager)

## Hướng dẫn cài đặt và chạy

### Bước 1: Cài đặt PostgreSQL (nếu chưa có)

1. Tải và cài đặt PostgreSQL từ: https://www.postgresql.org/download/
2. Trong quá trình cài đặt, ghi nhớ mật khẩu bạn đặt cho user `postgres`
3. Tạo database tên `bluemoon`:
   ```sql
   CREATE DATABASE bluemoon;
   ```

**Lưu ý:** Nếu bạn muốn dùng SQLite thay vì PostgreSQL, có thể sửa file `settings.py` (xem phần cuối).

### Bước 2: Tạo và kích hoạt môi trường ảo (Virtual Environment)

Mở PowerShell hoặc Command Prompt và chạy:

```powershell
# Di chuyển vào thư mục dự án
cd C:\BlueMoon\myproject

# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Hoặc trên Command Prompt:
.\venv\Scripts\activate.bat
```

### Bước 3: Cài đặt các thư viện cần thiết

```powershell
pip install -r requirements.txt
```

### Bước 4: Cấu hình database

Mở file `myproject/settings.py` và kiểm tra thông tin database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bluemoon',
        'USER': 'postgres',
        'PASSWORD': '123456',  # Đổi thành mật khẩu PostgreSQL của bạn
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**Nếu muốn dùng SQLite (không cần PostgreSQL):**

Thay đổi cấu hình database trong `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Bước 5: Chạy migrations

```powershell
python manage.py migrate
```

### Bước 6: Tạo superuser (tùy chọn)

Để truy cập trang admin:

```powershell
python manage.py createsuperuser
```

Nhập username, email và password khi được yêu cầu.

### Bước 7: Chạy server

```powershell
python manage.py runserver
```

### Bước 8: Truy cập ứng dụng

Mở trình duyệt và truy cập:
- Trang chủ: http://127.0.0.1:8000/
- Trang admin: http://127.0.0.1:8000/admin/

## Cấu trúc dự án

- `hokhau/` - Quản lý hộ khẩu
- `nhankhau/` - Quản lý nhân khẩu
- `khoanthu/` - Quản lý khoản thu
- `noptien/` - Quản lý nộp tiền
- `tamtrutamvang/` - Quản lý tạm trú tạm vắng
- `users/` - Quản lý người dùng
- `home/` - Trang chủ

## Xử lý lỗi thường gặp

### Lỗi: "ModuleNotFoundError: No module named 'django'"
- Giải pháp: Đảm bảo bạn đã kích hoạt môi trường ảo và cài đặt requirements.txt

### Lỗi: "could not connect to server"
- Giải pháp: Kiểm tra PostgreSQL đã chạy chưa, và thông tin kết nối trong settings.py

### Lỗi: "database does not exist"
- Giải pháp: Tạo database `bluemoon` trong PostgreSQL hoặc chuyển sang SQLite
