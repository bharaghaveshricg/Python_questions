Single File Programming Question
Problem Statement



Prakya is studying ancient numeral systems and is particularly fascinated by Roman numerals. She wishes to create a program that can convert regular numbers into their Roman numeral equivalents. To achieve this, she seeks your assistance in developing the conversion tool.



Roman Numeral Conversion Rules:



Roman numerals use the symbols I, V, X, L, C, D, and M to represent numbers.
Thousands are represented by the letter M repeated the required number of times.
Hundreds are represented by C, D, and M, and variations are based on subtraction and repetition.
Tens are represented by X, L, and C, with variations based on subtraction and repetition.
Ones are represented by I, V, and X, and variations based on subtraction and repetition.
Input format :
The input consists of a single integer, num, representing the number to be converted into a Roman numeral.

Output format :
The output displays a single line containing the Roman numeral representation of the input number.

If the input number is invalid less than 1 or greater than 3999, it will print "Invalid input".



Refer to the sample output for the formatting specifications.

Code constraints :
In this scenario, the given test cases will fall under the following constraints:

0 ≤ num ≤ 8000

Sample test cases :
Input 1 :
23
Output 1 :
XXIII
Input 2 :
567
Output 2 :
DLXVII
  
SOLUtion:
num = int(input())

if num < 1 or num > 3999:
    print("Invalid input")
else:
    thousands = num // 1000
    hundreds = (num // 100) % 10
    tens = (num // 10) % 10
    ones = num % 10

    roman_numeral = ""

    roman_numeral += "M" * thousands

    if hundreds == 9:
        roman_numeral += "CM"
    elif hundreds == 4:
        roman_numeral += "CD"
    else:
        if hundreds >= 5:
            roman_numeral += "D" + "C" * (hundreds - 5)
        else:
            roman_numeral += "C" * hundreds


    if tens == 9:
        roman_numeral += "XC"
    elif tens == 4:
        roman_numeral += "XL"
    else:
        if tens >= 5:
            roman_numeral += "L" + "X" * (tens - 5)
        else:
            roman_numeral += "X" * tens


    if ones == 9:
        roman_numeral += "IX"
    elif ones == 4:
        roman_numeral += "IV"
    else:
        if ones >= 5:
            roman_numeral += "V" + "I" * (ones - 5)
        else:
            roman_numeral += "I" * ones

    print(roman_numeral)
