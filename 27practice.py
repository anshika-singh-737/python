marks1 = int(input("enter marks 1:"))
marks2 = int(input("enter marks 2:"))
marks3 = int(input("enter marks 3"))

#check total percentage
total_percentage = marks1+marks2+marks3/300

if(total_percentage>= 40):
    print("you are pass" , total_percentage)
else:
    print("you failed, try again!"), total_percentage