# File name: 2Q.py
# Author: Thomás Rizzi Omura
# Description: After writing 10 numbers, transform those numbers in a list.

# creating an empty list
lst = []

# number of elements as input
n = int(input("Write 10"))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)
