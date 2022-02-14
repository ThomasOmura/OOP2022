
#Filename: Exercise_2_E2.py
#Author: Thomás Rizzi Omura
#Description: Pseudocode for a grading program


print("Please give your exercise points:") #Asks for integer input from user
exercise_points= int(input()) #if it is string the program stops



if exercise_points > 120:   
    #If its bigger then 120 then it asks for less points
    print("You can not have more then 120 points.")
elif exercise_points >= 108:
    #between 108 and 120 the grade is 5
    print ("Your grade is: 5")
elif exercise_points >= 96:
    #between 96 and 108 the grade is 4
    print ("Your grade is: 4")
elif exercise_points >= 84:
    #between 84 and 96 the grade is 3
    print ("Your grade is: 3")
elif exercise_points >= 72:
    #between 72 and 84 the grade is 2
    print ("Your grade is: 2")
elif exercise_points >= 60:
    #between 60 and 72 the grade is 1
    print ("Your grade is: 1")
elif exercise_points >= 0:
    #Bigger as and 108 = grade 5
    print ("Your grade is: 0. You did not pass.")
elif exercise_points <0:
    #Stops if integer is not positive
    print("You have to give a positive integers.")
else:
    print ("Please input a correct number.")