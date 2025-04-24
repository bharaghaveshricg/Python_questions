# You are using Python
d=input()
n=int(input())
price=0
if d=="Monday" and n>=5:
    price=(200*n)-150
else:
    price=200*n
print("Total amount to be paid:",price)
