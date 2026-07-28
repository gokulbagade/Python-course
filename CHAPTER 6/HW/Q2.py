# 2. Write a program to find out whether a student has passed or failed if it requires
#  a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks
#  as an input from the user.

sub1 = int(input("enter the marks of sub 1 : "))
sub2 = int(input("enter the marks of sub 2 : "))
sub3 = int(input("enter the marks of sub 3 : "))


marks1 =(sub1/100)*100
marks2 =(sub2/100)*100
marks3 =(sub3/100)*100

#average percentage
average_marks = (marks1+marks2+marks3)/3

#total markes percentage
total = ((sub1+sub2+sub3)/300)*100

if total >= 40 and average_marks >= 33  and marks1 >33 and marks2 >33 and marks3>3:
    print(f"you are pass \n total percentage : {total} \n marks of sub 1 : {sub1} \t per : {marks1} \n marks of sub2 : {sub2} \t per : {marks2} \n marks of sub3 : {sub3} \t per : {marks3}")  
else:
    print("you are fail")