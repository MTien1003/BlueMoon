# Danh sách User Test

## 👥 Các tài khoản test đã tạo

### 1. **Tổ trưởng/Tổ phó (Admin)**
- **Username**: `admin`
- **Password**: `admin123`
- **Vai trò**: Tổ trưởng/Tổ phó
- **Quyền hạn**:
  - ✅ Quản lý hộ khẩu, nhân khẩu
  - ✅ Quản lý users (tạo, sửa, xóa tài khoản)
  - ✅ Phân quyền cho các tài khoản
  - ✅ Truy cập tất cả các module

### 2. **Cán bộ (Canbo)**
- **Username**: `canbo`
- **Password**: `canbo123`
- **Vai trò**: Cán bộ
- **Quyền hạn**:
  - ✅ Quản lý hộ khẩu, nhân khẩu
  - ❌ Không quản lý users
  - ❌ Không quản lý thu phí

### 3. **Kế toán (KeToan)**
- **Username**: `ketoan`
- **Password**: `ketoan123`
- **Vai trò**: Kế toán
- **Quyền hạn**:
  - ✅ Quản lý khoản thu
  - ✅ Quản lý nộp tiền
  - ❌ Không quản lý hộ khẩu, nhân khẩu
  - ❌ Không quản lý users

### 4. **Người dùng thường (User)**
- Có thể tạo qua admin panel hoặc command
- **Quyền hạn**:
  - ✅ Chỉ xem trang chủ
  - ❌ Không truy cập các module khác

## 🧪 Cách test phân quyền

### Test với Tổ trưởng/Tổ phó (admin):
1. Đăng nhập: http://127.0.0.1:8000/login/
2. Username: `admin`, Password: `admin123`
3. Kiểm tra:
   - ✅ Có thể truy cập: Nhân khẩu, Hộ khẩu, Quản lý users
   - ✅ Có thể tạo/sửa/xóa users

### Test với Cán bộ (canbo):
1. Đăng nhập với: `canbo` / `canbo123`
2. Kiểm tra:
   - ✅ Có thể truy cập: Nhân khẩu, Hộ khẩu
   - ❌ Không thể truy cập: Quản lý users, Khoản thu, Nộp tiền

### Test với Kế toán (ketoan):
1. Đăng nhập với: `ketoan` / `ketoan123`
2. Kiểm tra:
   - ✅ Có thể truy cập: Khoản thu, Nộp tiền
   - ❌ Không thể truy cập: Nhân khẩu, Hộ khẩu, Quản lý users

## 📝 Tạo thêm user mới

### Sử dụng command:
```bash
cd myproject
python manage.py create_user --username <username> --password <password> --vaitro <vaitro>
```

**Vai trò có thể chọn:**
- `admin` - Tổ trưởng/Tổ phó
- `canbo` - Cán bộ
- `ketoan` - Kế toán
- `user` - Người dùng

**Ví dụ:**
```bash
# Tạo user kế toán
python manage.py create_user --username ketoan2 --password ketoan123 --vaitro ketoan

# Tạo user cán bộ
python manage.py create_user --username canbo2 --password canbo123 --vaitro canbo
```

### Hoặc qua Admin Panel:
1. Đăng nhập với tài khoản admin
2. Truy cập: http://127.0.0.1:8000/users/
3. Click "Thêm người dùng mới"
4. Điền thông tin và chọn vai trò

## ⚠️ Lưu ý

- Tất cả các user test đều có password đơn giản, chỉ dùng cho development
- Trong production, cần đổi password mạnh hơn
- User admin có thể quản lý tất cả users khác

