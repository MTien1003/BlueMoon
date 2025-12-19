# BlueMoon - Hệ thống Quản lý Dân cư

Dự án **BlueMoon** là một ứng dụng web được xây dựng trên nền tảng **Django Framework**, được thiết kế để hỗ trợ công tác quản lý dân cư, hộ khẩu và các khoản đóng góp tại địa phương một cách hiệu quả và trực quan.

---

## 🚀 Tính năng chính

Hệ thống được chia thành các phân hệ (Apps) chuyên biệt:

* **Quản lý Nhân khẩu (`nhankhau`)**:
    * Thêm mới, cập nhật thông tin nhân khẩu.
    * Khai báo khai sinh, khai tử.
    * Thống kê nhân khẩu theo các tiêu chí.

* **Quản lý Hộ khẩu (`hokhau`)**:
    * Đăng ký sổ hộ khẩu mới.
    * Tách khẩu, chuyển hộ khẩu đi/đến.
    * Thay đổi chủ hộ.

* **Quản lý Tạm trú & Tạm vắng (`tamtrutamvang`)**:
    * Đăng ký tạm trú cho người từ nơi khác đến.
    * Khai báo tạm vắng cho người địa phương đi vắng.

* **Quản lý Thu phí & Đóng góp (`khoanthu`, `noptien`)**:
    * Thiết lập các khoản thu (bắt buộc, tự nguyện).
    * Ghi nhận lịch sử đóng tiền của từng hộ.
    * Thống kê tình hình nộp phí.

* **Hệ thống & Người dùng (`users`, `home`)**:
    * Đăng nhập, đăng xuất, phân quyền quản trị.
    * Dashboard tổng quan với biểu đồ thống kê (sử dụng Chart.js/Morris.js).

---

## 🛠 Yêu cầu hệ thống

Để chạy được dự án, máy tính cần cài đặt:

* **Python**: Phiên bản 3.8 trở lên.
* **Django**: Phiên bản 3.x hoặc 4.x.
* **Cơ sở dữ liệu**: SQLite (mặc định) hoặc MySQL/PostgreSQL.

---

## ⚙️ Hướng dẫn cài đặt & Chạy dự án

Thực hiện các bước sau trong Terminal hoặc Command Prompt:

### Bước 1: Clone dự án hoặc giải nén

git clone [https://github.com/mtien1003/bluemoon.git](https://github.com/mtien1003/bluemoon.git)
cd bluemoon
cd myproject

Bước 2: Tạo môi trường ảo (Virtual Environment) - Khuyến nghị


# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

Bước 3: Cài đặt các thư viện phụ thuộc
Nếu dự án có file requirements.txt:

pip install -r requirements.txt

Nếu chưa có file requirements, hãy cài Django thủ công:

pip install django

Bước 4: Khởi tạo Cơ sở dữ liệu (Database)
Tạo các bảng dữ liệu cần thiết:

python manage.py makemigrations
python manage.py migrate

Bước 5: Tạo tài khoản Quản trị viên (Superuser)
Tài khoản này dùng để đăng nhập vào trang quản trị /admin:

python manage.py createsuperuser

Bước 6: Khởi chạy Server

python manage.py runserver

Sau khi chạy thành công, mở trình duyệt và truy cập:

Trang chủ: http://127.0.0.1:8000/

Trang quản trị: http://127.0.0.1:8000/admin/
