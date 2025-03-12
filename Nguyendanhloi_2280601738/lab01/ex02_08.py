# Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

# Nhập chuỗi số nhị phân từ người dùng (phân tách bởi dấu phẩy)
chuoi_so_nhi_phan = input("Nhập các số nhị phân: ")

# Tách chuỗi thành danh sách các số nhị phân và kiểm tra số chia hết cho 5
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

# In kết quả
if len(so_chia_het_cho_5) > 0:
    ket_qua = ', '.join(so_chia_het_cho_5)
    print(f"Các số nhị phân chia hết cho 5 là: {ket_qua}")
else:
    print("Không có số nhị phân chia hết cho 5 trong chuỗi đã nhập.")