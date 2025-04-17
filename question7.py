height=float(input())
waist=float(input())
bf=64-(20*(height/waist))
print(f"{bf:.2f}%")
if bf>=2 and bf<=5:
    print("Essential fat")
elif bf>=6 and bf<=13:
    print("Athletes")
elif bf>=14 and bf<=17:
    print("Fitness")
elif bf>=18 and bf<=24:
    print("Average")
else:
    print("Obese")   
