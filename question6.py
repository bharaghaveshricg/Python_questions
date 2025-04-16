salary = float(input())
years_of_service = int(input())
bonus_percentage = float(input())
tax_percentage = float(input())

net_bonus = 0

if years_of_service > 5:
    net_bonus = (bonus_percentage / 100) * salary
    print("You have earned a bonus of", net_bonus, "units.")
else:
    print("Sorry, you are not eligible for a bonus.")

tax_amount = (tax_percentage / 100) * (salary + net_bonus)
net_salary = salary + net_bonus - tax_amount

print("Tax Amount:", tax_amount, "units")
print("Net Salary:", net_salary, "units")
