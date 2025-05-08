from typing import Any, ClassVar

class BankAccount: 
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

account: BankAccount = BankAccount("Alice", 400)

def transfer(src: BankAccount, dst: BankAccount, amount: int) -> None:
    src.withdraw(amount)
    dst.deposit(amount)


class AuditedBankAccount(BankAccount):
    audit_log: list[str]

    def __init__(self, acccount_name: str, initial_balance: int=0) -> None:
        super().__init__(account_name, initial_balance)
        self.audit_log: list[str] = []

    def deposit(self, amount: int) -> None:
        self.audit_log.append(f"Deposited {amount}")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.audit_log.append(f"Withdrew {amount}")
        self.balance -= amount

audited = AuditedBankAccount("Bob", 300)
transfer(audited, account, 100)

class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[list[str]]

class A:
    def __setattr__(self, __name: str, __value: int) -> None:
        pass

    def __getattr__(self, name: str) -> int: 
        pass


a = A()
a.food = 42
a.bar = 'Ex-parrot'