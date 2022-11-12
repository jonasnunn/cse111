from datetime import datetime
from re import sub

subtotal  = float(input('What is the subtotal? '))

day = datetime.today().weekday()

if subtotal >= 50 and day == 2 or day == 3:
    discount_amt = subtotal * .1
    total_pre_tax = subtotal - discount_amt
    sales_tax = total_pre_tax *.06
    total = total_pre_tax + sales_tax
    print(f'Discount amount {discount_amt:.2f}')
else:
    sales_tax = subtotal *.06
    total = subtotal + sales_tax


print(f'The sales tax is {sales_tax:.2f}')
print(f'The total is {total:.2f}')


