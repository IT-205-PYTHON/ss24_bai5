from features.feature_2 import _find_table


def checkout(table_records):
    print("\n--- THANH TOÁN HÓA ĐƠN ---")
    raw_id = input("Nhập mã bàn thanh toán: ")
    table = _find_table(table_records, raw_id)
    if table is None:
        return

    if table.current_bill == 0:
        print("Lỗi: Bàn này hiện đang trống, không có hóa đơn để thanh toán!")
        return

    table.checkout()