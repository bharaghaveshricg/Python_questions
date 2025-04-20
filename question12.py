x=int(input())
if x<=0:
    print("Invalid age. Please enter a valid age.")
else:
    price=0
    if x<=5:
        price=0
    elif x>6 and x<=12:
        price=10
    elif x>12 and x<=64:
        price=15
    else:
        price=12
    print("Ticket Price:",price)

    
    
