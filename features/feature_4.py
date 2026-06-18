from models.bistro_table import BistroTable


def update_vat(table_records):
    print("\n--- CẬP NHẬT THUẾ SUẤT VAT TOÀN NHÀ HÀNG ---")
    current_pct = int(BistroTable._vat_rate * 100)
    print(f"[HỆ THỐNG] Thuế suất VAT hiện tại là: {current_pct}% ({BistroTable._vat_rate})")

    try:
        new_rate = float(input("Nhập thuế suất VAT mới (ví dụ: 0.1 cho 10%): ").strip())
    except ValueError:
        print("Tỷ lệ thuế không hợp lệ!")
        return

    if new_rate < 0.0 or new_rate > 0.2:
        print("Tỷ lệ thuế không hợp lệ!")
        return

    BistroTable.update_vat_rate(new_rate)
    new_pct = int(new_rate * 100)
    print(f">> Thông báo: Rikkei Bistro cập nhật thuế suất VAT mới ở mức {new_pct}% thành công!")