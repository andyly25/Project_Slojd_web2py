# userInputMatching.py
# Joseph Ou, Shivam Dave, Andy Ly
# CMPS112
# This binary search was created to compare a user input
import sys
import os

from HaikuMod import getWordFile

#fileIn = getWordFile(1,1)

#lowerBound = 0
#UpperBound = len(fileIn)


#binary search that returns 1 if found and 0 if not
def binarySearch(wordFile, key, lowerBound, UpperBound):
	if (UpperBound <= lowerBound):
		print("reached the end without finding solution")
		return 0;
	else:
		#round the midpoint down
		mid = int((round(UpperBound + lowerBound)/2 - .5))
		if (wordFile[mid - 1] == key):
			return 1
		#if desired word is smaller, move to the greater half of list
		if (wordFile[mid] > key):
			return binarySearch(wordFile, key, lowerBound, mid - 1)
		#if desired word is greater, move to the lesser half of the list
		elif (wordFile[mid] < key):
			return binarySearch(wordFile, key, mid + 1, UpperBound)
		#if something is found, return
		else:
			return 1;


#print binarySearch(getWordFile(1,1), "pears", 0, len(getWordFile(1,1)))


#inputMatching takes a string and compares it to the source dictionaries. if found, it returns 1
def inputMatching(userIn):
	i = 0
	j = 0
	for i in range(1,5):
		for j in range(1,5):
			fileIn = getWordFile(i,j)
			hello = len(fileIn)
			print hello
			total = binarySearch(fileIn, userIn, 0, len(fileIn))
			output = [i, j]
			print output
			if (total != 0):
				return output
				break
	return [0,0]

print inputMatching("obfuscation")
