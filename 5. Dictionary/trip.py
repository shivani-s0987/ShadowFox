your_expenses = {
    "Hotel": 1400,
    "Food": 600,
    "Transportation": 400,
    "Attractions": 200,
    "Miscellaneous": 100
}

partner_expenses = {
    "Hotel": 1500,
    "Food": 400,
    "Transportation": 500,
    "Attractions": 200,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

if your_total > partner_total:
    print("You spent more.")
elif your_total < partner_total:
    print("Your partner spent more.")
else:
    print("Both spent the same.")

max_diff = 0
max_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_category = category

print(f"Greatest difference is in '{max_category}' with a difference of {max_diff}")
