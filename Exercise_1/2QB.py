# creating an empty list
lst = []

# number of elements as input
n = int(input("Write 10"))

# string till the range
for i in range(0, n):
	ele = str(input())

	lst.append(ele) # adding the element
	
print(lst)