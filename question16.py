f=float(input())
h=float(input())
if f>75 and h<50:
    print("Recommended crop for planting: tomatoes")
elif f>75 and h>50:
    print("Recommended crop for planting: cucumbers")    
elif f<75 and h>70:
    print("Recommended crop for planting: lettuce")
else:
    print("Recommended crop for planting: Not suitable for planting")
