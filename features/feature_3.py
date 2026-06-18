from features.feature_2 import _find_table


def cancel_dish(table_records):
    print("\n--- HỦY MÓN / GIẢM TRỪ HÓA ĐƠN ---")
    raw_id = input("Nhập mã bàn cần hủy món: ")
    table = _find_table(table_records, raw_id)
    if table is None:
        return

    try:
        amount = int(input("Nhập giá trị món muốn giảm trừ: ").strip())
    except ValueError:
        print("Vui lòng nhập số tiền là một số nguyên dương!")
        return

    if amount <= 0:
        print("Vui lòng nhập số tiền là một số nguyên dương!")
        return

    table.cancel_dish(amount)