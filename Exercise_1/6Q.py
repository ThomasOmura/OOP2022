# File name: 6Q.py
# Author: Thomás Rizzi Omura
# Description: funcation that counts the sum of the positive integers divisible by three

list_Of_Numbers=[] 
num=None 
print("Enter '0' to stop the program") 
while True: 
    print("Enter Integer Number") 
    num=input() 
    if(num=="0"): 
        break 
    try: 
        num=int(num) 
        list_Of_Numbers.append(num) 
    except: 
        print("Invalid Integer")

pos_nos = [num for num in list_Of_Numbers if (num % 3) == 0]
pos_nos2 = [num for num in pos_nos if num > 0]

sum = sum(pos_nos2)
         
#print(list_Of_Numbers) 
print("Positive numbers in the list", sum)