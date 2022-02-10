import pandas as csv

fields = ['Name', 'Account Number', 'Balance', 'Account Type', 'Card Number', 'Mobile Number', 'PIN', 'ACCESS']
filename = "accounts.csv"
balance = "balance.csv"
data = csv.read_csv(filename)


class Accounts:

    def __init__(self, account_number):
        if not (data['Account Number'] == int(account_number)).bool():
            raise ValueError
        self.account_number = int(account_number)

    def _get_item(self):
        return data[data['Account Number'] == self.account_number]

    def get_account_number(self):
        return self.account_number

    @classmethod
    def get_account_from_card(cls, card_number):
        row = data[data['Card Number'] == card_number]
        return cls(row['Account Number'].item())

    def get_balance(self):
        row = self._get_item()
        return row['Balance'].item()

    def withdraw(self, amount: int):
        row = self._get_item()
        if amount % 200 != 0:
            raise IncorrectAmount("In multiples of Rs. 200")

        row["Balance"] = row["Balance"].replace({row["Balance"].item(): row["Balance"].item() - amount})
        data.to_csv("accounts.csv", index=False)

    def validate_phone_otp(self, mobile, otp):
        row = self._get_item()
        return row['Mobile Number'].item() == int(mobile) and row['Pin'].item() == int(otp)

    def update_pin(self, new_pin):
        row = self._get_item()
        row["Pin"] = row["Pin"].replace(new_pin)
        data.to_csv("accounts.csv", index=False)

    def block_card(self):
        row = self._get_item()
        row["Access"] = row["Access"].replace('BLOCKED')
        data.to_csv("accounts.csv", index=False)


class LowBalance(Exception):
    pass


class IncorrectAmount(Exception):
    pass
