from random import randint
from random import randrange
import sys
import glob
import errno
import HaikuMod

def randSylLine (max):
	startNum = randint(1, 4)
	sylList = [startNum]
	remainSyl = max - startNum
	while (remainSyl > 0):
		if(remainSyl > 4):
			tempNum = randint(1, 4)
		else: 
			tempNum = randint(1, remainSyl)
		sylList.append(tempNum)
		remainSyl-=tempNum
	return sylList


def makeHaiku1():
	# print ("\n" + makeLine(randSylLine(5)))
	# print (makeLine(randSylLine(7)))
	# print (makeLine(randSylLine(5)) + "\n")
	# apple1=makeLine1(randSylLine(5))
	# apple2=makeLine1(randSylLine(7))
	# apple3=makeLine1(randSylLine(5))
	apple = "\n\" " + makeLine(randSylLine(5), randFileLine (5))+ "\n  " + makeLine(randSylLine(7), randFileLine (7)) + "\n  " +makeLine(randSylLine(5), randFileLine (5)) + "\"\n"
	return apple

def randFileLine (size):
	fileList = []
	count = 0
	while (count < size):
		tempNum = randint(1, 4)
		fileList.append(tempNum)
		count+=1
	return fileList


def makeLine(sylCountList, fileCountList):
	# print ("SYL: " + str(sum(sylCountList)))
	print ("FILE: " + str(fileCountList))
	retLine = ""
	for tempSy, tempFi in zip(sylCountList, fileCountList):
		tempLines = HaikuMod.getWordFile(tempFi, tempSy)
		if (len(tempLines)-1 < 1):
			print("\n**ERROR**\n")
			break
		tempLinesNum = randrange(0, len(tempLines))

		retLine += tempLines[tempLinesNum] + " "
	return retLine;	

def fileLine2 (size, fileList):
	# fileList = randFileLine(size)
	count = 0
	while (count < size-1):
		if(fileList[count-1] == 1 or fileList[count + 1] == 1):
			fileList[count] = randint(2, 3)
		if(fileList[count] == 4 and (fileList[count-1] != 3 or fileList[count + 1] != 3)):
			fileList[count] = randint(1, 3)
		if(fileList[count-1] == 3 or fileList[count + 1] == 3):
			fileList[count] = 4			
		if(fileList[count-1] == 3 and fileList[count] == 3):
			fileList[randint(count-1, count)] = randint(1, 2)	
		if(fileList[count-1] == 4 and fileList[count] == 4):
			fileList[randint(count-1, count)] = randint(1, 3)
		count+=1
	return fileList	

def haikuType1():
	sylList1 = randSylLine(5)
	sylList2 = randSylLine(7)
	sylList3 = randSylLine(5)
	haikuStr = ("\n" + makeLine(sylList1, randFileLine(len(sylList1))) + "\n" + 
				makeLine(sylList2, randFileLine(len(sylList2))) + "\n" + 
				makeLine(sylList3, randFileLine(len(sylList3))) + "\n")
	return haikuStr

def haikuType2():
	sylList1 = randSylLine(5)
	sylList2 = randSylLine(7)
	sylList3 = randSylLine(5)
	fileList1 = randFileLine(len(sylList1))
	fileList2 = randFileLine(len(sylList2))
	fileList3 = randFileLine(len(sylList3))

	haikuStr1 = ("\n" + makeLine(sylList1, fileList1) + "\n" + 
				makeLine(sylList2, fileList2) + "\n" + 
				makeLine(sylList3, fileList3) + "\n")

	haikuStr2 = ("\n" + makeLine(sylList1, fileLine2(len(sylList1), fileList1)) + "\n" + 
				makeLine(sylList2, fileLine2(len(sylList2), fileList2)) + "\n" + 
				makeLine(sylList3, fileLine2(len(sylList3), fileList3)) + "\n")

	return haikuStr1 + haikuStr2

print (haikuType2())





