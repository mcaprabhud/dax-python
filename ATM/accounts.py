import csv
# from dataclasses import dataclass

fields = ['Name', 'Account Number', 'Balance', 'Account Type', 'Card Number', 'Mobile Number', 'PIN', 'ACCESS']
filename = "accounts.csv"
balance = "balance.csv"


# @dataclass
class Accounts:
    # name: str
    # account_number: int
    # balance: float
    # card_number: int
    # mobile: int
    # pin: int
    # account_type: str = "Savings"
    # access: str = "ALLOWED"

    def __init__(self, account_number):
        with open(filename, 'r') as file:
            for row in csv.reader(file):
                if account_number in row:
                    self.name, self.account_number, self.balance, self.account_type, self.card_number, self.mobile, \
                        self.pin, self.access = row

        # Accounts.get_account(account_number)
        # self.name = name
        # self.account_number = account_number
        # self.balance = balance
        # self.card_number = card_number
        # self.mobile = mobile
        # self.pin = pin
        # self.account_type = account_type
        # self.access = access

    def __str__(self):
        return f"{self.account_number} {self.balance} {self.name}"

    @classmethod
    def get_account_from_card(cls, card_number):
        with open(filename, 'r') as file:
            for row in file.readlines()[1:]:
                if card_number == row.split(',')[4]:
                    return cls(row.split(',')[1])

            raise ModuleNotFoundError

    def _update_record(self):
        with open(balance, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow((self.name, self.account_number, self.balance, self.card_number, self.mobile, self.pin,
                                 self.account_type, self.access))

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return int(self.balance)

    def withdraw(self, amount: int):
        if amount % 200 != 0:
            raise IncorrectWithdrawalAmount("Withdrawal amount should be in multiples of Rs. 200")
        if self.get_balance() < 200:
            raise LowBalance("Balance too low")

        self.balance = self.get_balance() - amount
        self._update_record()

    def validate_phone_otp(self, mobile, otp):
        return self.mobile == mobile and self.pin == otp

    def update_pin(self, new_pin):
        self.pin = new_pin
        self._update_record()

    def block_card(self):
        self.access = 'BLOCKED'
        self._update_record()

class LowBalance(Exception):
    pass


class IncorrectWithdrawalAmount(Exception):
    pass
