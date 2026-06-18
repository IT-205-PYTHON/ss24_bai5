"""
===================================================================
TÀI LIỆU THIẾT KẾ LỚP BISTROTABLE
===================================================================
1. Class Attributes (Thuộc tính Lớp):
   - Tên biến: _vat_rate | Ý nghĩa: Thuế suất VAT áp dụng chung
     cho toàn bộ bàn ăn trong nhà hàng. Mặc định 0.08 (8%).

2. Instance Attributes (Thuộc tính Đối tượng):
   - Quyền Public  : capacity     | Ý nghĩa: Sức chứa tối đa (số người)
   - Quyền Private : __table_id   | Ý nghĩa: Mã định danh bàn (TB01...)
   - Quyền Private : __current_bill | Ý nghĩa: Tổng tiền tạm tính hiện tại,
     mặc định 0. Bảo vệ bằng name mangling tránh sửa trực tiếp từ ngoài.

3. Methods (Các Phương thức):
   - __init__(self, table_id, capacity):
       Gán __table_id, capacity. Khởi tạo __current_bill = 0.

   - Getters (@property):
       + table_id      → trả về __table_id (read-only)
       + current_bill  → trả về __current_bill (read-only)
       + status        → tính động: "Đang trống" nếu __current_bill == 0,
                         ngược lại "Có khách"
       + final_total   → tính động: __current_bill * (1 + _vat_rate)

   - Instance Methods:
       + order_dish(amount)  : Cộng amount vào __current_bill
       + cancel_dish(amount) : Trừ amount khỏi __current_bill,
                               chặn nếu amount > __current_bill
       + checkout()          : In hóa đơn, reset __current_bill về 0

   - Class Methods:
       + update_vat_rate(cls, new_rate): Cập nhật cls._vat_rate

   - Static Methods:
       + validate_id(table_id): Kiểm tra mã bàn hợp lệ —
         bắt đầu bằng "TB" và độ dài >= 3. Trả về bool.
===================================================================
"""


class BistroTable:
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        self.__table_id = table_id
        self.capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self):
        return self.__table_id

    @property
    def current_bill(self):
        return self.__current_bill

    @property
    def status(self):
        return "Đang trống" if self.__current_bill == 0 else "Có khách"

    @property
    def final_total(self):
        return int(self.__current_bill * (1 + BistroTable._vat_rate))

    def order_dish(self, amount):
        self.__current_bill += amount
        print(f">> Thành công: Đã ghi nhận món ăn {amount:,}đ vào Bàn '{self.__table_id}'.")
        print(f">> Số tiền tạm tính hiện tại của bàn: {self.__current_bill:,}đ.")

    def cancel_dish(self, amount):
        if amount > self.__current_bill:
            print("Lỗi: Số tiền giảm trừ vượt quá giá trị hóa đơn hiện tại!")
            return
        self.__current_bill -= amount
        print(f">> Thành công: Đã giảm trừ {amount:,}đ khỏi Bàn '{self.__table_id}' do sự cố bếp.")
        print(f">> Số tiền tạm tính còn lại: {self.__current_bill:,}đ.")
        if self.__current_bill == 0:
            print(f">> Bàn '{self.__table_id}' hiện đã chuyển về trạng thái Đang trống.")

    def checkout(self):
        base = self.__current_bill
        vat_pct = int(BistroTable._vat_rate * 100)
        total = self.final_total
        tid = self.__table_id
        print(f"\n--- HÓA ĐƠN THANH TOÁN BÀN {tid} ---")
        print(f"Số tiền món ăn: {base:,}đ")
        print(f"Thuế suất VAT áp dụng: {vat_pct}%")
        print(f"Tổng tiền cần thanh toán (gồm thuế): {total:,}đ")
        print("-----------------------------------")
        self.__current_bill = 0
        print(f">> Thanh toán thành công! Bàn '{tid}' đã được dọn sạch và chuyển sang trạng thái Đang trống.")

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls._vat_rate = new_rate

    @staticmethod
    def validate_id(table_id):
        return len(table_id) >= 3 and table_id[:2] == "TB"