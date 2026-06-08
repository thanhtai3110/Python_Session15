# =========================
# GLOBAL VARIABLES
# =========================
atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    """
    Hiển thị số dư tài khoản và tiền mặt trong ATM.

    Parameters:
        None

    Returns:
        None
    """
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Nạp tiền vào tài khoản.

    Parameters:
        amount (int): Số tiền cần nạp.

    Returns:
        bool: True nếu nạp thành công.
    """
    global user_account_balance
    global atm_vault_balance

    user_account_balance += amount
    atm_vault_balance += amount

    return True


def check_withdrawal_rules(amount):
    """
    Kiểm tra điều kiện rút tiền.

    Parameters:
        amount (int): Số tiền muốn rút.

    Returns:
        tuple:
            (status, fee, total_deduction)
    """
    fee = 1100
    total_deduction = amount + fee

    if amount % 50000 != 0:
        return ("INVALID_MULTIPLE", fee, total_deduction)

    if total_deduction > user_account_balance:
        return ("INSUFFICIENT_FUNDS", fee, total_deduction)

    if amount > atm_vault_balance:
        return ("ATM_OUT_OF_CASH", fee, total_deduction)

    return ("OK", fee, total_deduction)


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện giao dịch rút tiền.

    Parameters:
        total_deduction (int): Tổng tiền bị trừ.
        amount_to_dispense (int): Tiền ATM trả cho khách.

    Returns:
        None
    """
    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense


def main():
    """
    Chạy chương trình ATM.

    Parameters:
        None

    Returns:
        None
    """
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input("Vui lòng chọn giao dịch (1-4): ")

        match choice:

            case "1":
                display_balances()

            case "2":
                print("\n--- NẠP TIỀN ---")

                try:
                    amount = int(input("Nhập số tiền muốn nạp: "))
                except ValueError:
                    print("Vui lòng nhập số hợp lệ.")
                    continue

                if amount <= 0:
                    print("Số tiền không hợp lệ")
                    continue

                if deposit_money(amount):
                    print(
                        f"Giao dịch thành công! "
                        f"Số dư tài khoản hiện tại: "
                        f"{user_account_balance:,} VND."
                    )

            case "3":
                print("\n--- RÚT TIỀN ---")

                try:
                    amount = int(input("Nhập số tiền cần rút: "))
                except ValueError:
                    print("Vui lòng nhập số hợp lệ.")
                    continue

                if amount <= 0:
                    print("Số tiền không hợp lệ")
                    continue

                status, fee, total_deduction = check_withdrawal_rules(amount)

                match status:

                    case "INVALID_MULTIPLE":
                        print("Số tiền rút phải là bội số của 50,000")

                    case "INSUFFICIENT_FUNDS":
                        print(
                            "Giao dịch thất bại: "
                            "Số dư tài khoản không đủ."
                        )

                    case "ATM_OUT_OF_CASH":
                        print(
                            "Giao dịch thất bại: "
                            "Máy ATM không đủ tiền mặt để phục vụ."
                        )

                    case "OK":
                        print("Giao dịch đang xử lý...")

                        execute_withdrawal(
                            total_deduction,
                            amount
                        )

                        print(f"Phí giao dịch: {fee:,} VND")
                        print(
                            f"Bạn đã rút thành công "
                            f"{amount:,} VND."
                        )
                        print(
                            f"Số dư tài khoản còn lại: "
                            f"{user_account_balance:,} VND."
                        )

            case "4":
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break

            case _:
                print("Lựa chọn không hợp lệ.")


main()