
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

option = ''

while option != '6':
    print('\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====')
    print('1. Hiển thị danh sách sản phẩm')
    print('2. Bán sản phẩm cho khách hàng')
    print('3. Xử lý đổi trả sản phẩm')
    print('4. Áp dụng giảm giá cho sản phẩm')
    print('5. Nhập thêm hàng vào kho cửa hàng')
    print('6. Thoát chương trình')
    print('====================================================')
    
    option = input('Nhập lựa chọn của bạn (1-6): ').strip()
    
    match option:
        case '1':
            print()
            if not product_list:
                print('Danh sách sản phẩm hiện đang trống.')
            else:
                print('DANH SÁCH SẢN PHẨM HIỆN TẠI:')
                print(f"{'STT':<4} | {'Mã SP':<7} | {'Tên sản phẩm':<18} | {'Giá gốc':<10} | {'Kho':<5} | {'Bán':<5} | {'Trả':<5} | {'Giảm':<5} | {'Trạng thái'}")
                print("-" * 90)
                
                for i, item in enumerate(product_list, start=1):
                    if item["quantity"] == 0:
                        status = "Hết hàng"
                    elif item["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                        
                    print(f"{i:<4} | {item['product_id']:<7} | {item['product_name']:<18} | {item['price']:<10,} | {item['quantity']:<5} | {item['sold']:<5} | {item['returned']:<5} | {item['discount']:<4}% | {status}")
            print()
            
        case '2':
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm khách muốn mua: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    qty_str = input('Nhập số lượng khách mua: ').strip()
                    if not qty_str.isdigit() or int(qty_str) <= 0:
                        print('Lỗi: Số lượng mua không hợp lệ, phải là số nguyên dương!')
                        break
                        
                    qty_buy = int(qty_str)
                    if qty_buy > item['quantity']:
                        print(f'Lỗi: Số lượng trong kho không đủ (Hiện còn: {item["quantity"]})')
                        break
                        
                    item['quantity'] -= qty_buy
                    item['sold'] += qty_buy
                    
                    price_after_discount = item['price'] * (100 - item['discount']) / 100
                    total_payment = price_after_discount * qty_buy
                    print(f'Giá gốc: {item["price"]:,} VNĐ | Giảm giá: {item["discount"]}%')
                    print(f'Tổng tiền khách cần thanh toán: {int(total_payment):,} VNĐ')
                    break
                    
            if not found:
                print('Lỗi: Không tìm thấy mã sản phẩm cần bán trong hệ thống.')
            print()
            
        case '3':
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm khách muốn đổi/trả: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    if item['sold'] == 0:
                        print('Lỗi: Sản phẩm này chưa có lịch sử bán ra, không thể đổi trả!')
                        break
                    
                    qty_str = input('Nhập số lượng đổi/trả: ').strip()
                    if not qty_str.isdigit() or int(qty_str) <= 0:
                        print('Lỗi: Số lượng đổi/trả không hợp lệ!')
                        break
                        
                    qty_return = int(qty_str)
                    if qty_return > item['sold']:
                        print(f'Lỗi: Số lượng trả ({qty_return}) vượt quá số lượng đã bán ({item["sold"]})')
                        break
                        
                    item['sold'] -= qty_return
                    item['quantity'] += qty_return
                    item['returned'] += qty_return
                    
                    price_after_discount = item['price'] * (100 - item['discount']) / 100
                    total_refund = price_after_discount * qty_return
                    print(f'Số tiền cần hoàn lại cho khách: {int(total_refund):,} VNĐ')
                    break
                    
            if not found:
                print('Lỗi: Không tìm thấy mã sản phẩm cần đổi trả.')
            print()
            
        case '4':
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm cần áp dụng giảm giá: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    dct_str = input('Nhập phần trăm giảm giá (0-70): ').strip()
                    if not dct_str.isdigit():
                        print('Lỗi: Phần trăm giảm giá phải là ký tự số!')
                        break
                        
                    dct_val = int(dct_str)
                    if dct_val < 0 or dct_val > 70:
                        print('Lỗi: Phần trăm giảm giá không hợp lệ, chỉ áp dụng từ 0% đến 70%!')
                        break
                        
                    item['discount'] = dct_val
                    print(f'Thành công: Đã cập nhật giảm giá cho sản phẩm {item["product_id"]} thành {dct_val}%')
                    break
                    
            if not found:
                print('Lỗi: Không tìm thấy mã sản phẩm cần áp dụng giảm giá.')
            print()
            
        case '5':
            print()
            found = False
            input_pro_id = input('Nhập mã sản phẩm cần nhập thêm: ').strip().upper()
            
            for item in product_list:
                if input_pro_id == item['product_id']:
                    found = True
                    
                    qty_str = input('Nhập số lượng nhập thêm: ').strip()
                    if not qty_str.isdigit() or int(qty_str) <= 0:
                        print('Lỗi: Số lượng nhập thêm không hợp lệ!')
                        break
                        
                    qty_add = int(qty_str)
                    item['quantity'] += qty_add
                    print(f'Thành công: Nhập hàng thành công! Số lượng tồn kho mới của {item["product_id"]}: {item["quantity"]} chiếc.')
                    break
                    
            if not found:
                print('Lỗi: Không tìm thấy mã sản phẩm này trong hệ thống.')
            print()
            
        case '6':
            print('Đã thoát hệ thống. Tạm biệt!')
            
        case _:
            print('Lỗi: Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 6!')
