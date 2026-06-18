from models.bistro_table import BistroTable


def _find_table(table_records, raw_id):
    table_id = raw_id.strip().upper()
    if not BistroTable.validate_id(table_id):
        print("Mã bàn không hợp lệ!")
        return None
    for table in table_records:
        if table.table_id == table_id:
            return table
    print("Không tìm thấy bàn có mã này!")
    return None


def order_dish(table_records):
    print("\n--- GỌI MÓN MỚI ---")
    raw_id = input("Nhập mã bàn gọi món: ")
    table = _find_table(table_records, raw_id)
    if table is None:
        return

    try:
        amount = int(input("Nhập giá tiền món ăn mới: ").strip())
    except ValueError:
        print("Vui lòng nhập số tiền là một số nguyên dương!")
        return

    if amount <= 0:
        print("Vui lòng nhập số tiền là một số nguyên dương!")
        return

    table.order_dish(amount)