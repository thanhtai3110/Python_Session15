# (1) Phân tích và thiết kế
# Pseudo-code luồng dữ liệu
# START

# Khởi tạo:
#     available_seats = 50
#     flight_revenue = 0.0
#     BASE_PRICE = 2000.0

# WHILE True
#     Hiển thị menu

#     Nhập lựa chọn

#     IF lựa chọn == 1
#         Nhập số lượng vé
#         Nhập hạng vé

#         total_cost = calculate_ticket_cost(quantity, seat_class)

#         booking_success = book_ticket(quantity, total_cost)

#     ELIF lựa chọn == 2
#         Nhập số lượng vé muốn hủy

#         refund_amount = refund_ticket(quantity)

#         In số tiền hoàn trả

#     ELIF lựa chọn == 3
#         display_flight_status()

#     ELIF lựa chọn == 4
#         Thoát chương trình

#     ELSE
#         Thông báo nhập sai

# END
# Dòng chảy giá trị tiền tệ
# Người dùng nhập:
#     quantity = 2
#     seat_class = Business

#             |
#             v

# calculate_ticket_cost()
#     -> tính tiền vé
#     -> cộng 5% phí dịch vụ
#     -> return total_payment

#             |
#             v

# book_ticket(quantity, total_payment)
#     -> kiểm tra ghế trống
#     -> flight_revenue += total_payment
#     -> cập nhật available_seats

# Ví dụ:

# 2 vé Business
# ↓
# calculate_ticket_cost()
# ↓
# 6300.0
# ↓
# book_ticket(2, 6300.0)
# ↓
# flight_revenue += 6300.0
# Tính toàn vẹn dữ liệu

# Biến flight_revenue cần là biến toàn cục (global) vì:

# Doanh thu là dữ liệu dùng chung cho toàn bộ hệ thống.
# Hàm đặt vé phải tăng doanh thu.
# Hàm hoàn vé phải giảm doanh thu.
# Hàm báo cáo phải đọc doanh thu hiện tại.

# Nếu không dùng biến toàn cục thì mỗi hàm sẽ chỉ làm việc với bản sao cục bộ của dữ liệu và doanh thu tổng sẽ không được đồng bộ trong toàn chương trình.

# (2) Triển khai chương trình
# ==========================
# SKYBOOKING SYSTEM
# ==========================

MAX_CAPACITY = 50
BASE_PRICE = 2000.0

available_seats = MAX_CAPACITY
flight_revenue = 0.0


def calculate_ticket_cost(quantity: int, seat_class: int) -> float:
    """
    Calculate the final ticket payment.

    Parameters:
        quantity (int): Number of tickets.
        seat_class (int): 1 for Economy, 2 for Business.

    Returns:
        float: Final payment including 5% airport service fee.
    """

    if seat_class == 1:
        ticket_price = BASE_PRICE
    else:
        ticket_price = BASE_PRICE * 1.5

    subtotal = quantity * ticket_price
    service_fee = subtotal * 0.05

    return subtotal + service_fee


def book_ticket(quantity: int, total_payment: float) -> bool:
    global available_seats
    global flight_revenue

    if quantity > available_seats:
        print(
            f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống."
        )
        return False

    available_seats -= quantity
    flight_revenue += total_payment

    print(
        f"Đặt vé thành công! Ghế trống còn lại: {available_seats}"
    )

    return True


def refund_ticket(quantity: int) -> float:
    global available_seats
    global flight_revenue

    if available_seats + quantity > MAX_CAPACITY:
        print(
            "Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra."
        )
        return 0.0

    refund_amount = quantity * BASE_PRICE * 0.8

    available_seats += quantity
    flight_revenue -= refund_amount

    return refund_amount


def display_flight_status():
    """
    Display current flight status report.

    Report format:
    - Maximum capacity
    - Reserved seats
    - Available seats
    - Current revenue
    """

    booked_seats = MAX_CAPACITY - available_seats

    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_CAPACITY}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue:.1f}")


def get_positive_quantity(message):
    while True:
        try:
            quantity = int(input(message))

            if quantity <= 0:
                print("Số lượng vé phải lớn hơn 0.")
                continue

            return quantity

        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")


def get_ticket_class():
    while True:
        try:
            seat_class = int(
                input("Chọn hạng vé (1: Economy, 2: Business): ")
            )

            if seat_class in (1, 2):
                return seat_class

            print("Hạng vé không hợp lệ.")

        except ValueError:
            print("Vui lòng nhập 1 hoặc 2.")


def main():
    while True:

        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")

        choice = input("Chọn chức năng (1-4): ")

        # ==========================
        # BOOKING
        # ==========================
        if choice == "1":

            print("\n--- ĐẶT VÉ MÁY BAY ---")

            quantity = get_positive_quantity(
                "Nhập số lượng vé: "
            )

            seat_class = get_ticket_class()

            if seat_class == 1:
                seat_name = "Economy"
                ticket_price = BASE_PRICE
            else:
                seat_name = "Business"
                ticket_price = BASE_PRICE * 1.5

            subtotal = quantity * ticket_price
            service_fee = subtotal * 0.05

            total_payment = calculate_ticket_cost(
                quantity,
                seat_class
            )

            print("-> Xác nhận đặt chỗ:")
            print(
                f"Số lượng: {quantity} | Hạng: {seat_name}"
            )
            print(f"Tạm tính: ${subtotal}")
            print(f"Phí dịch vụ (5%): ${service_fee}")
            print(
                f"Tổng thanh toán: ${total_payment}"
            )

            book_ticket(quantity, total_payment)

        # ==========================
        # REFUND
        # ==========================
        elif choice == "2":

            print("\n--- HỦY VÉ & HOÀN TIỀN ---")

            quantity = get_positive_quantity(
                "Nhập số lượng vé muốn hủy: "
            )

            refund_amount = refund_ticket(quantity)

            if refund_amount > 0:
                print(
                    f"Hủy vé thành công. Hệ thống đã hoàn lại: "
                    f"${refund_amount} (80% giá cơ bản)."
                )
                print(
                    f"Ghế trống hiện tại: {available_seats}"
                )

        # ==========================
        # STATUS
        # ==========================
        elif choice == "3":
            display_flight_status()

        # ==========================
        # EXIT
        # ==========================
        elif choice == "4":
            print(
                "\nCảm ơn đã sử dụng SKYBOOKING SYSTEM."
            )
            print("Đóng hệ thống...")
            break

        else:
            print(
                "Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4."
            )


if __name__ == "__main__":
    main()