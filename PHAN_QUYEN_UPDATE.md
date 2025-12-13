# Cập nhật Phân quyền theo Yêu cầu

## ✅ Đã cập nhật để đúng với yêu cầu

### 1. **Vai trò người dùng**

Theo yêu cầu, hệ thống có 2 tác nhân chính:
- **Tổ trưởng/Tổ phó**: Quản lý hộ khẩu, nhân khẩu và quản lý/phân quyền tài khoản
- **Kế toán**: Quản lý thu phí, quản lý các khoản đóng góp

**Đã cập nhật:**
- ✅ Thêm vai trò `ketoan` (Kế toán) vào User model
- ✅ Cập nhật `admin` thành "Tổ trưởng/Tổ phó"
- ✅ Giữ nguyên `canbo` (Cán bộ) và `user` (Người dùng)

### 2. **Phân quyền theo module**

#### **Quản lý Hộ khẩu và Nhân khẩu**
- ✅ **Nhân khẩu** (`nhankhau/views.py`): Chỉ **Tổ trưởng/Tổ phó** (admin/canbo)
- ✅ **Hộ khẩu** (`hokhau/views.py`): Chỉ **Tổ trưởng/Tổ phó** (admin/canbo)
- ✅ Sử dụng decorator: `@totruong_required`

#### **Quản lý Thu phí và Đóng góp**
- ✅ **Khoản thu** (`khoanthu/views.py`): Chỉ **Kế toán** (ketoan)
- ✅ **Nộp tiền** (`noptien/views.py`): Chỉ **Kế toán** (ketoan)
- ✅ Sử dụng decorator: `@ketoan_required`

#### **Quản lý Users (Phân quyền tài khoản)**
- ✅ **Quản lý users** (`users/views.py`): Chỉ **Tổ trưởng/Tổ phó** (admin)
- ✅ Sử dụng decorator: `@admin_required`

### 3. **Các decorator và mixins mới**

#### Decorators (`users/decorators.py`):
- ✅ `@totruong_required`: Chỉ tổ trưởng/tổ phó (admin/canbo)
- ✅ `@ketoan_required`: Chỉ kế toán
- ✅ `@admin_required`: Chỉ admin (tổ trưởng)
- ✅ `@canbo_required`: Cán bộ hoặc admin

#### Mixins (`common/mixins.py`):
- ✅ `ToTruongRequiredMixin`: Cho class-based views
- ✅ `KeToanRequiredMixin`: Cho class-based views

### 4. **User Model Properties**

Thêm các properties mới:
- ✅ `is_ketoan`: Kiểm tra user có phải kế toán không
- ✅ `is_totruong`: Kiểm tra user có phải tổ trưởng/tổ phó không (admin/canbo)

## 📋 Tóm tắt phân quyền

| Module | Chức năng | Vai trò được phép |
|--------|-----------|-------------------|
| **Nhân khẩu** | Quản lý nhân khẩu | Tổ trưởng/Tổ phó (admin/canbo) |
| **Hộ khẩu** | Quản lý hộ khẩu | Tổ trưởng/Tổ phó (admin/canbo) |
| **Khoản thu** | Quản lý các khoản thu | Kế toán (ketoan) |
| **Nộp tiền** | Quản lý nộp tiền | Kế toán (ketoan) |
| **Users** | Quản lý tài khoản, phân quyền | Tổ trưởng (admin) |
| **Trang chủ** | Dashboard | Tất cả user đã đăng nhập |

## 🔄 Cần chạy migrations

```bash
cd myproject
python manage.py migrate
```

## 🧪 Test phân quyền

1. **Tạo các user test:**
   ```bash
   python manage.py create_admin --username totruong --password totruong123
   # Tạo user kế toán qua admin panel hoặc code
   ```

2. **Kiểm tra:**
   - Tổ trưởng/Tổ phó có thể truy cập: Nhân khẩu, Hộ khẩu, Quản lý users
   - Kế toán có thể truy cập: Khoản thu, Nộp tiền
   - User thường chỉ xem trang chủ

## 📝 Lưu ý

- Tất cả các views đã được bảo vệ bằng decorators phù hợp
- Messages thông báo rõ ràng khi user không có quyền
- Redirect về trang chủ khi không có quyền truy cập

