'''Problem Statement



Agalya is working on a simple calculator program. She wants to create a program that takes an integer input between 1 and 9 (inclusive) and then asks the user if they want to operate. If the user confirms (by entering 'y'), the program prompts for the operation (+, -, or *) and another integer operand.



The program then performs the specified operation on the initial number and the operand and displays the result. If the input integer is not between 1 and 9 or if the operation is invalid, the program prints "Invalid Input" or "Invalid operation", respectively.

Input format :
The first line of input consists of an integer number (between 1 and 9)(both 1 and 9 inclusive).

The second line of input consists of the characters 'y' or 'n' indicating whether the user wants to perform a calculation.

The third line of input consists, If the user wants to perform a calculation ('y'), the program should take the following additional inputs: an operation: '+' for addition, '-' for subtraction, '*' for multiplication.

The fourth line of input consists of an integer operand for the chosen operation.

Output format :
The output displays the different results based on the user's choices:



If the number is invalid: print "Invalid Input"

If the user doesn't want to perform a calculation ('n'): print the original number

If the user wants to perform a calculation ('y') and the operation is valid: "The result of the operation is: <result>" And if the operation is invalid (excluding +, -, and *), it prints an "Invalid operation".



Refer to the sample output for the formatting specifications.'''

x=int(input())
yes_no=input()
if (yes_no=="n"):
    print(f"{x}")
if x>9 or x<1:
    print("Invalid Input")
if yes_no=='y' and x>=1 and x<=9:
    o=input()
    if o!="+" and o!="-" and o!="*":
        print("Invalid operation")
    y=int(input())
    if o == "+":
        print(f"The result of the operation is: {x+y}")
    elif o =="-":
        print(f"The result of the operation is: {x-y}")
    else :
        print(f"The result of the operation is: {x*y}")

        