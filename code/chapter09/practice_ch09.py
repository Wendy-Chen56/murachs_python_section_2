# Chapter 9 Practice

# Practice 1: Floating-Point Numbers
amount = 50.10
amount += 50.10
amount += 50.10

print("Amount =", amount)
print("Rounded Amount =", round(amount, 2))



# Practice 2: math Module
import math

number =36
print("Square root =", math.sqrt(number))



# Practice 3: f-string Formatting
sales = 9876.543

print(f"Sales = {sales:,.2f}")



# Practice 4: Decimal
from decimal import Decimal

price = Decimal("20.15")
quantity = Decimal("3")

total = price * quantity

print("Total =", total)
