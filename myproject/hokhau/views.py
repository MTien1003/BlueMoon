from django.shortcuts import render
from .models import HoKhau, ThanhVienHoKhau, LichSuThayDoiHoKhau
from nhankhau.models import NhanKhau
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from django.utils import timezone
import datetime
import random


def hokhau(request):
    # Lấy giá trị tìm kiếm từ ô input (phương thức GET)
    query = request.GET.get('q')

    if query:
        # Lọc danh sách hộ khẩu theo tên chủ hộ (không phân biệt hoa thường)
        hokhau_list = HoKhau.objects.select_related('chuhokhau').filter(
            chuhokhau__hoten__icontains=query
        ).order_by('sohokhau')
    else:
        # Nếu không tìm kiếm, lấy toàn bộ danh sách
        hokhau_list = HoKhau.objects.select_related(
            'chuhokhau').all().order_by('sohokhau')

    return render(request, 'hokhau.html', {'hokhau_list': hokhau_list})


def create_hokhau(request):
    if request.method == 'POST':
        # --- 1. TỰ ĐỘNG SINH SỐ HỘ KHẨU THEO THỨ TỰ ---
        # Logic: Lấy hộ khẩu được tạo gần nhất để tính số tiếp theo
        last_hokhau = HoKhau.objects.all().order_by('id').last()

        if last_hokhau and last_hokhau.sohokhau.startswith('HK'):
            try:
                # Tách phần số ra khỏi chữ "HK" (Ví dụ: HK00005 -> lấy số 5)
                last_number = int(last_hokhau.sohokhau[2:])
                new_number = last_number + 1
            except ValueError:
                # Phòng trường hợp dữ liệu cũ không đúng định dạng chuẩn
                new_number = 1
        else:
            # Nếu chưa có hộ khẩu nào trong DB
            new_number = 1

        # Tạo chuỗi mã mới: HK + 5 chữ số (Ví dụ: HK00001, HK00010)
        sohokhau_auto = f"HK{new_number:05d}"

        # --- 2. Lấy dữ liệu từ form ---
        sonha = request.POST.get('sonha')
        duong = request.POST.get('duong')
        phuong = request.POST.get('phuong')
        quan = request.POST.get('quan')
        ngaylamhokhau = request.POST.get('ngaylamhokhau')
        chuhokhau_id = request.POST.get('chuhokhau')
        ghichu = request.POST.get('ghichu')

        # --- 3. Lấy danh sách thành viên ---
        thanhvien_ids = request.POST.getlist('thanhvien_id[]')
        quanhes = request.POST.getlist('quanhe[]')

        try:
            with transaction.atomic():
                chu_ho = NhanKhau.objects.get(id=chuhokhau_id)

                # Tạo Hộ Khẩu
                hokhau = HoKhau.objects.create(
                    sohokhau=sohokhau_auto,
                    sonha=sonha,
                    duong=duong,
                    phuong=phuong,
                    quan=quan,
                    ngaylamhokhau=ngaylamhokhau,
                    chuhokhau=chu_ho,
                    sothanhvien=len(thanhvien_ids) + 1,
                    ghichu=ghichu
                )

                # Tạo Thành viên
                for nhankhau_id, quanhe in zip(thanhvien_ids, quanhes):
                    if nhankhau_id:
                        nhan_khau = NhanKhau.objects.get(id=nhankhau_id)
                        ThanhVienHoKhau.objects.create(
                            hokhau=hokhau,
                            nhankhau=nhan_khau,
                            quanhevoichuho=quanhe,
                            ngaythemnhankhau=ngaylamhokhau
                        )

                messages.success(
                    request, f'Đã tạo hộ khẩu mới: {sohokhau_auto}')
                return redirect('hokhau')
        except Exception as e:
            messages.error(request, f'Lỗi hệ thống: {e}')

    nhankhau_list = NhanKhau.objects.all()
    return render(request, 'create_hokhau.html', {'nhankhau_list': nhankhau_list})


def xem_hokhau(request, pk):
    # Lấy thông tin hộ khẩu hoặc báo lỗi 404 nếu không tìm thấy
    hokhau = HoKhau.objects.select_related('chuhokhau').get(id=pk)

    # Lấy danh sách thành viên thuộc hộ khẩu này
    # Truy vấn qua ForeignKey hokhau trong model ThanhVienHoKhau
    danh_sach_thanh_vien = ThanhVienHoKhau.objects.filter(
        hokhau=hokhau).select_related('nhankhau')

    context = {
        'hokhau': hokhau,
        'danh_sach_thanh_vien': danh_sach_thanh_vien,
    }
    return render(request, 'xem_hokhau.html', context)


def update_hokhau(request, pk):
    hokhau = get_object_or_404(HoKhau, id=pk)
    # Không nên lấy queryset cố định ở đầu nếu bạn định xóa/thêm
    # Hãy lấy trực tiếp bên trong POST để đảm bảo dữ liệu mới nhất

    if request.method == 'POST':
        try:
            with transaction.atomic():
                # 1. Cập nhật thông tin cơ bản của hộ khẩu
                hokhau.sohokhau = request.POST.get('sohokhau')
                hokhau.sonha = request.POST.get('sonha')
                hokhau.duong = request.POST.get('duong')
                hokhau.phuong = request.POST.get('phuong')
                hokhau.quan = request.POST.get('quan')
                hokhau.ngaylamhokhau = request.POST.get('ngaylamhokhau')
                hokhau.ghichu = request.POST.get('ghichu')

                chu_ho_id = request.POST.get('chuhokhau')
                if chu_ho_id:
                    hokhau.chuhokhau = NhanKhau.objects.get(id=chu_ho_id)

                # 2. Lấy danh sách thành viên từ Form gửi lên
                moi_thanhvien_ids = request.POST.getlist('thanhvien_id[]')
                moi_quanhes = request.POST.getlist('quanhe[]')
                # Chuyển ID sang số nguyên và loại bỏ giá trị rỗng
                moi_thanhvien_ids_int = [int(x)
                                         for x in moi_thanhvien_ids if x]

                # 3. XỬ LÝ XÓA: Tìm những người có trong DB nhưng KHÔNG có trong danh sách mới
                thanh_vien_db = ThanhVienHoKhau.objects.filter(hokhau=hokhau)
                for tv_cu in thanh_vien_db:
                    if tv_cu.nhankhau_id not in moi_thanhvien_ids_int:
                        # Lưu lịch sử trước khi xóa
                        LichSuThayDoiHoKhau.objects.create(
                            hokhau=hokhau,
                            nhankhau=tv_cu.nhankhau,
                            loaithaydoi=2,  # Giả sử 2 là Xóa
                            ngaythaydoi=timezone.now()
                        )
                        tv_cu.delete()  # Lệnh xóa thực thi ở đây

                # 4. XỬ LÝ THÊM/CẬP NHẬT
                cu_thanhvien_ids = set(ThanhVienHoKhau.objects.filter(
                    hokhau=hokhau).values_list('nhankhau_id', flat=True))

                for nk_id_str, qh in zip(moi_thanhvien_ids, moi_quanhes):
                    if not nk_id_str:
                        continue
                    nk_id = int(nk_id_str)

                    if nk_id not in cu_thanhvien_ids:
                        nhankhau_obj = NhanKhau.objects.get(id=nk_id)
                        ThanhVienHoKhau.objects.create(
                            hokhau=hokhau, nhankhau=nhankhau_obj,
                            quanhevoichuho=qh, ngaythemnhankhau=timezone.now().date()
                        )
                        LichSuThayDoiHoKhau.objects.create(
                            hokhau=hokhau, nhankhau=nhankhau_obj,
                            loaithaydoi=1, ngaythaydoi=timezone.now()
                        )
                    else:
                        # Cập nhật lại quan hệ nếu người đó vẫn còn trong hộ
                        ThanhVienHoKhau.objects.filter(
                            hokhau=hokhau, nhankhau_id=nk_id).update(quanhevoichuho=qh)

                # --- BƯỚC QUAN TRỌNG NHẤT: CẬP NHẬT SỐ THÀNH VIÊN ---
                # Chúng ta đếm lại toàn bộ số bản ghi đang thực sự tồn tại trong DB sau khi xóa/thêm
                so_thanh_vien_hien_tai = ThanhVienHoKhau.objects.filter(
                    hokhau=hokhau).count()

                # Cập nhật vào trường sothanhvien (Cộng thêm 1 nếu chủ hộ không nằm trong bảng ThanhVienHoKhau)
                hokhau.sothanhvien = so_thanh_vien_hien_tai + 1
                hokhau.save()  # Lưu lại hộ khẩu với số lượng mới
                # ---------------------------------------------------

                messages.success(
                    request, f"Cập nhật hộ khẩu {hokhau.sohokhau} thành công!")
                return redirect('hokhau')

        except Exception as e:
            messages.error(request, f"Lỗi hệ thống: {str(e)}")

    # Load lại dữ liệu cho GET request
    nhankhau_list = NhanKhau.objects.all()
    thanh_vien_hien_tai = ThanhVienHoKhau.objects.filter(hokhau=hokhau)
    context = {
        'hokhau': hokhau,
        'thanh_vien_hien_tai': thanh_vien_hien_tai,
        'nhankhau_list': nhankhau_list,
    }
    return render(request, 'update_hokhau.html', context)


def lich_su_hokhau(request, pk):
    # Lấy thông tin hộ khẩu
    hokhau = get_object_or_404(HoKhau, id=pk)

    # Lấy danh sách lịch sử thay đổi của hộ khẩu này, sắp xếp mới nhất lên đầu
    history_list = LichSuThayDoiHoKhau.objects.filter(
        hokhau=hokhau).select_related('nhankhau').order_by('-ngaythaydoi')

    context = {
        'hokhau': hokhau,
        'history_list': history_list,
    }
    return render(request, 'lich_su_hokhau.html', context)
