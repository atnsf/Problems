# excercise_003
import sys
numersArray = [1, 2, 3, 4, 25, 26, 27, 53, 54, 55, 81, 83, 84]
number = int(input("Choose number: "))
arr = []
for index in numersArray:
	if index < number:
		arr.append(index)
print arr