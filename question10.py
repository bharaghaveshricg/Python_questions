pa_age = int(input())

addon_age = int(input())

e_type = int(input())

pa_income = int(input())



if (21 <= pa_age <= 60) and (18 <= addon_age) and (1 <= e_type <= 4) and (pa_income >= 300000):

    print("Yes. You are eligible for SBI credit cards")

    discount = pa_income * 0.05  

    print(f"Discount applied: {discount}")

else:

    print("No. You are not eligible for SBI credit cards")

    discount = pa_income * 0.02  

    print(f"Discount applied: {discount}")

