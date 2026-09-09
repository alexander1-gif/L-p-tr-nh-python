# BÀI 7: Mini project 2 - Quản lý kho hàng ---
kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5)
]

# Thêm sản phẩm mới
kho_hang.append(("Tai nghe", 300000, 15))

# Xóa một sản phẩm
kho_hang.remove(("Chuot", 150000, 20))

# Hiển thị danh sách kho hàng
print("DANH SACH KHO HANG:")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} - SL: {so_luong}")

# Tính tổng giá trị kho hàng bằng vòng lập cộng dồn
tong_gia_tri = 0
for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(f"Tong gia tri kho hang: {tong_gia_tri:,} VND")