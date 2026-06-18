from models.bistro_table import BistroTable
from features import view_tables, order_dish, cancel_dish, update_vat, checkout


def main():
    table_records = [
        BistroTable("TB01", 4),
        BistroTable("TB02", 2),
        BistroTable("TB03", 8),
    ]

    while True:
        print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
        print("1. Hiển thị sơ đồ & Trạng thái bàn ăn")
        print("2. Gọi món mới (Tăng tiền hóa đơn)")
        print("3. Hủy món / Giảm trừ hóa đơn (Sự cố nhà bếp)")
        print("4. Cập nhật thuế suất VAT toàn nhà hàng")
        print("5. Thanh toán hóa đơn & Trả bàn trống")
        print("6. Thoát chương trình")
        print("=====================================================")
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                view_tables(table_records)
            case "2":
                order_dish(table_records)
            case "3":
                cancel_dish(table_records)
            case "4":
                update_vat(table_records)
            case "5":
                checkout(table_records)
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống điều phối bàn ăn Rikkei Bistro!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6!")


if __name__ == "__main__":
    main()