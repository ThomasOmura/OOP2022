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
         
#print(list_Of_Numbers) 
print("Negative numbers in the list", *neg_nos)