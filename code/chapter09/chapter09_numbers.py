# Chapter 9 - How to Work with Numbers

# Example 1: Floating-Point Numbers

balance = 100.10
balance += 100.10
balance += 100.10

print("Balance =", balance)

rounded_balance = round(balance, 2)
print("Rounded Balance =", rounded_balance)


# Example 2: The math Model

import math

print("Square root of 25 =", math.sqrt(25))
print("4.2 rounded up =", math.ceil(4.2))
print("4.8 rounded down =", math.floor(4.8))
print("Pi =", math.pi)


# Example 3: Format Numbers with f-strings

price = 12345.678
rate = 0.075

print("Original price =", price)
print(f"Price with 2 decimal places = {price:.2f}")
print(f"Price with comma = {price:,.2f}")
print(f"Rate as percentage = {rate:.1%}")


# Example 4: Decimal Numbers

from decimal import Decimal

decimal_balance = Decimal("100.10")
decimal_balance += Decimal("100.10")
decimal_balance += Decimal("100.10")

print("Decimal Balance =", decimal_balance)


# Example 5: Rounding Decimal Numbers

from decimal import ROUND_HALF_UP

price = Decimal("10.005")
rounded_price = price.quantize(
    Decimal("1.00"),
    rounding=ROUND_HALF_UP
)
print("Original Decimal =", price)
print("Rounded Decimal =", rounded_price)

