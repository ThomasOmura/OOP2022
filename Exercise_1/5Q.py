# File name: 5Q.py
# Author: Thomás Rizzi Omura
# Description: Function that counts the number of even integers

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

even_nos = [num for num in list_Of_Numbers if (num % 2) == 0]
         
#print(list_Of_Numbers) 
print("Even numbers in the list", *even_nos)