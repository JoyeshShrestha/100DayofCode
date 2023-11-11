# tip calculator
bill=input("What was the total bill? $")

total_bill = float(bill)
tip=input("What percentage tip would you like to give?10, 12 or 15?")
percent_tip = int(tip)
people = input("How many people to split the bill?")
total_people = int(people)
net_amt = total_bill+(total_bill*(percent_tip/100))
final = net_amt/total_people
round_final = round(final,2)
print(f"Each person should pay: ${round_final}")