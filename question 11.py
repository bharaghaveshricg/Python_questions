x=int(input())
y=int(input())
if x>0 and y>0:
    print("The coordinate point lies in the first quadrant.")
elif x<0 and y>0:
    print("The coordinate point lies in the second quadrant.")
elif x<0 and y<0:
    print("The coordinate point lies in the third quadrant.")
elif x>0 and y<0:
    print("The coordinate point lies in the fourth quadrant.")
elif x==0 and y==0:
    print("The coordinate point lies at the origin.")
