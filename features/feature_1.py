def view_tables(table_records):
    print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")
    for i, table in enumerate(table_records, 1):
        print(
            f"{i}. Mã bàn: {table.table_id} | "
            f"Sức chứa: {table.capacity} người | "
            f"Tạm tính: {table.current_bill:,}đ{'':<5}| "
            f"Trạng thái: {table.status}"
        )
    print("----------------------------------\n")