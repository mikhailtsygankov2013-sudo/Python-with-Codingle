def total_bill(bill, tip):
    total = bill*(1+0.01*tip)
    total = round(total, 2)
    print(f"Please pay the total of {total:.2f}")

total_bill(100, 4)
