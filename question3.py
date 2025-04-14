Problem Statement



Ram recently appeared for three exams and wants to analyze his scores. Write a program to help Ram find the maximum score, average score, and total sum of his exam scores.

Input format :
The first line of input consists of x as an integer.

The second line of input consists of y as an integer.

The third line of input consists of z as an integer.

Output format :
The first line of output displays the following format:



If x is the largest among the three numbers, output: "The maximum number is: x", where x is the value of x.
If y is the largest among the three numbers, output: "The maximum number is: y", where y is the value of y.
If z is the largest among the three numbers, output: "The maximum number is: z", where z is the value of z.


The second line of output displays the average of the three numbers, rounded to two decimal places, printed as: "Average: avg", where avg is the average value.



The third line of output displays the sum of the three numbers and is printed as: "Sum: sum", where the sum is the total sum.


SOLUtion:
# You are using Python
x=int(input())
y=int(input())
z=int(input())

if x>y and x>z:
    max=x
elif y>x and y>z:
    max=y
else:
    max=z
    
sum=x+y+z  
average=sum/3
print(f"The maximum number is: {max}")
print(f"Average: {average:.2f}")
print(f"Sum: {sum}")
