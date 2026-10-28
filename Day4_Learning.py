
from abc import ABC, abstractmethod


# 1. ABSTRACTION
class Account(ABC):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount
        print(f"Deposited: ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.__balance:
            print("Insufficient balance.")
            return False

        self.__balance -= amount
        print(f"Withdrawn: ₹{amount:.2f}")
        return True

    @abstractmethod
    def account_type(self):
        pass

    # 2. MAGIC METHOD
    def __str__(self):
        return (
            f"{self.account_holder} | "
            f"{self.account_type()} Account | "
            f"Balance: ₹{self.balance:.2f}"
        )

    # 3. OPERATOR OVERLOADING
    def __add__(self, other):
        if not isinstance(other, Account):
            return NotImplemented

        return self.balance + other.balance


# 4. INHERITANCE
class SavingsAccount(Account):
    def account_type(self):
        return "Savings"


class CurrentAccount(Account):
    def account_type(self):
        return "Current"


# 5. POLYMORPHISM
def display_account(account):
    print(account)


def main():
    savings = SavingsAccount("Raghav", 10000)
    current = CurrentAccount("Aman", 5000)

    print("Account Details")
    display_account(savings)
    display_account(current)

    print("\n Encapsulation")
    print("Savings balance:", savings.balance)

    print("\nDeposit and Withdrawal")
    savings.deposit(2000)
    savings.withdraw(1500)
    print("Updated balance:", savings.balance)

    print("\nPolymorphism")
    for account in [savings, current]:
        print(f"{account.account_holder}: {account.account_type()}")

    print("\nOperator Overloading ")
    total_balance = savings + current
    print(f"Combined balance: ₹{total_balance:.2f}")

    print("\n Magic Method: __str__ ")
    print(savings)


if __name__ == "__main__":
    main()
