# File name: 9Q.py
# Author: Thomás Rizzi Omura
# Description: A program which repeatedly reads integers until the user enters 0 (NEGATIVE NUMBERS)

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

neg_nos = [num for num in list_Of_Numbers if num < 0]

total = len(neg_nos)
         
#print(list_Of_Numbers) 
print("Negative numbers in the list", total)