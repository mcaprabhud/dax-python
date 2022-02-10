from accounts import Accounts, LowBalance


def withdrawal_menu():
    mention = input("a. Enter the amount to withdrawal in terms of 200 RS\n"
                    "b. Check balance info\n"
                    "c. If balance low then display Error message (Low balance)\n"
                    "d. Exit\n"
                    "e. Thank you\n")

    if not (mention == "d" or mention == "e"):
        acc_num = input("Enter account number")
        acc = Accounts(acc_num)

        if mention == "a":
            amt = int(input("Enter withdrawal Amount:"))
            acc.withdraw(amt)
            print(f"Record updated successfully!! Current balance {acc.get_balance()}")
        elif mention == "b":
            print(f"Current balance {acc.get_balance()}")
        elif mention == "c" and acc.get_balance() < 200:
            raise LowBalance("Too low Balance")


def other_menu():
    mention = int(input("1. PIN change\n2. Block card"))
    card = input("Enter card number:")
    acc = Accounts.get_account_from_card(card)

    if acc:
        mobile = input("Enter mobile:")
        pin = input("Enter old pin:")
        isvalid = acc.validate_phone_otp(mobile, pin)
        if isvalid and mention == 1:
            new_pin = input("Enter new pin:")
            acc.update_pin(new_pin)
            print("New pin set!!")
        elif isvalid and mention == 2:
            acc.block_card()
            print("Hurray! Card blocked successfully!!")


try:
    while True:
        print("")
        print("Menu:\n1. Withdrawal\n2. Other")
        option = int(input("Please select transaction:\n"))
        if option > 2:
            raise ValueError
        elif option == 1:
            withdrawal_menu()
        elif option == 2:
            other_menu()

except Exception as err:
    print(err)
finally:
    print("Thank you!!")
