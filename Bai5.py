
# 1. PHÂN TÍCH INPUT / OUTPUT
# - Input: 
#   + Danh sách 'product_list' (chứa thông tin cố định ban đầu của các sản phẩm).
#   + Biến 'option': Lựa chọn menu người dùng nhập (số nguyên từ 1 đến 6).
#   + Dữ liệu phụ nhập thêm: Mã SP (chuỗi), Số lượng/Phần trăm giảm giá (chuỗi số).
# - Output:
#   + Bảng danh sách sản phẩm kèm trạng thái tính toán tự động (Còn hàng/Sắp hết/Hết).
#   + Hóa đơn tiền khách trả hoặc tiền hoàn lại cho khách (số nguyên).
#   + Thông báo trạng thái giao dịch (thành công hoặc báo lỗi dữ liệu).
#
# 2. THIẾT KẾ GIẢI PHÁP & THUẬT TOÁN
# - Sửa lỗi gán biến menu từ mã cũ (đổi 'input_option' thành 'option' để match-case nhận diện được).
# - Dùng vòng lặp while để duy trì hệ thống chạy liên tục cho đến khi chọn 6.
# - Sử dụng .strip().upper() chuẩn hóa mã nhập vào, tránh lỗi khoảng trắng hay chữ thường chữ hoa.
# - Dùng .isdigit() để kiểm tra bẫy dữ liệu đầu vào, chặn lỗi crash code nếu người dùng nhập chữ.

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

option = 0
found = False

while option != 6:
    print()
    print('===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====')
    print('1. Hiển thị danh sách sản phẩm')
    print('2. Bán sản phẩm cho khách hàng')
    print('3. Xử lý đổi trả sản phẩm')
    print('4. Áp dụng giảm giá cho sản phẩm')
    print('5. Nhập thêm hàng vào kho cửa hàng')
    print('6. Thoát chương trình')
    
    option = int(input('Nhập lựa chọn của bạn (1-6): '))
    
    match option:
        case 1:
            print()
            if product_list == []:
                print('Danh sách sản phẩm hiện đang trống.')
            else:
                print('Danh sách sản phẩm hiện tại:')
                for i, item in enumerate(product_list, start=1):
                    if item["quantity"] == 0:
                        status = "Hết hàng"
                    elif item["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(f'{i}. Mã SP: {item["product_id"]} | Tên: {item["product_name"]} | Giá: {item["price"]} | Tồn kho: {item["quantity"]} | Đã bán: {item["sold"]} | Đổi trả: {item["returned"]} | Giảm giá: {item["discount"]}% | Trạng thái: {status}')
            print()
            
        case 2:
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm khách muốn mua: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    qty_str = input('Nhập số lượng khách mua: ').strip()
                    if not qty_str.isdigit() or int(qty_str) <= 0:
                        print('Số lượng mua không hợp lệ')
                        break
                        
                    qty_buy = int(qty_str)
                    if qty_buy > item['quantity']:
                        print('Số lượng trong kho không đủ để bán')
                        break
                        
                    item['quantity'] -= qty_buy
                    item['sold'] += qty_buy
                    
                    price_after_discount = item['price'] * (100 - item['discount']) / 100
                    total_payment = price_after_discount * qty_buy
                    print(f'Tổng tiền khách cần thanh toán: {int(total_payment)} VNĐ')
                    break
                    
            if not found:
                print('Không tìm thấy sản phẩm cần bán')
            print()
            
        case 3:
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm khách muốn đổi/trả: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    qty_str = input('Nhập số lượng đổi/trả: ').strip()
                    if not qty_str.isdigit() or int(qty_str) <= 0:
                        print('Số lượng đổi/trả không hợp lệ')
                        break
                        
                    qty_return = int(qty_str)
                    if qty_return > item['sold']:
                        print('Số lượng đổi/trả không được vượt quá số lượng đã bán')
                        break
                        
                    item['sold'] -= qty_return
                    item['quantity'] += qty_return
                    item['returned'] += qty_return
                    
                    price_after_discount = item['price'] * (100 - item['discount']) / 100
                    total_refund = price_after_discount * qty_return
                    print(f'Số tiền hoàn lại cho khách: {int(total_refund)} VNĐ')
                    break
                    
            if not found:
                print('Không tìm thấy sản phẩm cần đổi trả')
            print()
            
        case 4:
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm cần áp dụng giảm giá: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    dct_str = input('Nhập phần trăm giảm giá: ').strip()
                    if not dct_str.isdigit():
                        print('Phần trăm giảm giá không hợp lệ')
                        break
                        
                    dct_val = int(dct_str)
                    if dct_val < 0 or dct_val > 70:
                        print('Phần trăm giảm giá không hợp lệ')
                        break
                        
                    item['discount'] = dct_val
                    print(f'Đã cập nhật giảm giá cho sản phẩm {item["product_id"]} thành {dct_val}%')
                    break
                    
            if not found:
                print('Không tìm thấy sản phẩm cần áp dụng giảm giá')
            print()
            
        case 5:
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm cần nhập thêm: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    qty_str = input('Nhập số lượng nhập thêm: ').strip()
                    if not qty_str.isdigit() or int(qty_str) <= 0:
                        print('Số lượng nhập thêm không hợp lệ')
                        break
                        
                    qty_add = int(qty_str)
                    item['quantity'] += qty_add
                    print(f'Nhập thêm hàng thành công! Số lượng tồn kho mới: {item["quantity"]}')
                    break
                    
            if not found:
                print('Không tìm thấy sản phẩm trong hệ thống')
            print()
            
        case 6:
            print('Thoát chương trình.')
            
        case _:
            print('Lựa chọn không hợp lệ, vui lòng nhập lại!')