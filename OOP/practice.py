from dataclasses import dataclass, field
from typing import List, Optional


class InsufficientFundsError(Exception):
    def __init__(self, amount: float, balance: float):
        super().__init__(f"Cannot withdraw {amount}. Current balance is {balance}.")


class BankAccount:
    bank_name = "Python Bank"
    total_accounts = 0

    def __init__(self, owner: str, initial_balance: float = 0):
        self.__owner = owner
        self.__balance = initial_balance
        BankAccount.total_accounts += 1

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def owner(self) -> str:
        return self.__owner

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise InsufficientFundsError(amount, self.__balance)
        self.__balance -= amount

    def transfer(self, amount: float, target: 'BankAccount') -> None:
        self.withdraw(amount)
        target.deposit(amount)

    @classmethod
    def get_bank_info(cls) -> dict:
        return {"bank": cls.bank_name, "total_accounts": cls.total_accounts}

    def __str__(self) -> str:
        return f"Account({self.__owner}, Balance: {self.__balance})"

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.__owner!r}, balance={self.__balance!r})"


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, initial_balance: float = 0, interest_rate: float = 0.05):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        self.deposit(self.balance * self.interest_rate)

    def __str__(self) -> str:
        return f"SavingsAccount({self.owner}, Balance: {self.balance}, Rate: {self.interest_rate*100}%)"


# Test
acc1 = BankAccount("Chinedu", 1000)
acc2 = BankAccount("Ada", 500)
savings = SavingsAccount("Obi", 2000, 0.08)

acc1.deposit(500)
acc1.transfer(200, acc2)
savings.apply_interest()

print(acc1)
print(acc2)
print(savings)
print(BankAccount.get_bank_info())