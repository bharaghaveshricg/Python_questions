'''Problem Statement:
Stephanie is managing a small clinic and needs to automate the scheduling system to display which doctor is available on a particular day. The clinic operates on a two-week cycle with each doctor assigned to specific days within these 14 days. 

Stephanie's system should input the day number and output the corresponding doctor's name using only if statements.

Schedule information:

Day 1, Day 8 and Day 14 doctor's name is "Dr. Smith"

Day 2 and Day 9 doctor's name is "Dr. Johnson"

Day 3 and Day 10 doctor's name is "Dr. Williams"

Day 4 and Day 11 doctor's name is "Dr. Brown"

Day 5 and Day 12 doctor's name is "Dr. Davis"

Day 6 and Day 13 doctor's name is "Dr. Miller"

Day 7 doctor's name is "Dr. Wilson"

Input format :
The input consists of an integer n, representing the day of the two-week cycle.
Output format :
The output displays "Doctor available on day X: Y", where X is an integer representing the day number and Y is a string representing the name of the doctor available on that day.'''



'''SOLUTION:'''
# You are using Python
day=int(input())

if day==1 or day==8 or day==14:
    doctor="Dr. Smith"
    print(f"Doctor available on day {day} : {doctor}")
elif day==2 or day==9:
    doctor="Dr. Johnson"
    print(f"Doctor available on day {day} : {doctor}")
elif day==3 or day==10:
    doctor="Dr. Willams"
    print(f"Doctor available on day {day} : {doctor}")
elif day==4 or day==11:
    doctor="Dr. Brown"
    print(f"Doctor available on day {day} : {doctor}")
elif day==5 or day==12:
    doctor="Dr. Davis"
    print(f"Doctor available on day {day} : {doctor}")
elif day==6 or day==13:
    doctor="Dr. Miller"
    print(f"Doctor available on day {day} : {doctor}")
else:
    doctor="Dr. Wilson"
    print(f"Doctor available on day {day} : {doctor}")