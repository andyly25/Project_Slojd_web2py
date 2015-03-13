from random import randint
from random import randrange
import sys
import glob
import errno
import HaikuMod

def getRandomSyllableList (max):
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

def getRandomFileList (size):
	fileList = []
	count = 0
	while (count < size):
		tempNum = randint(1, 4)
		fileList.append(tempNum)
		count+=1
	return fileList


def createLine(lineNumber, sylCountList, fileCountList):
	# print ("SYL: " + str(sum(sylCountList)))
	# print ("FILE: " + str(fileCountList))
	retLine = ""
	for tempSy, tempFi in zip(sylCountList, fileCountList):
		tempLines = HaikuMod.getWordFile(tempFi, tempSy)
		if (len(tempLines)-1 < 1):
			print("\n**ERROR**\n")
			break
		tempLinesNum = randrange(0, len(tempLines))
		retLine += tempLines[tempLinesNum] + " "
	retLine = retLine[:-1]
	commaRandInt = randint(1, 10)
	if(commaRandInt < 4 and lineNumber < 3):
		retLine += ","
	elif(commaRandInt < 4):
		retLine += "."
	return retLine;	

def editLine (size, fileList):
	count = 0
	while (count < size-1):
		if(fileList[count-1] == 1 or fileList[count + 1] == 1):
			fileList[count] = randint(2, 3)
		if(fileList[count] == 4 and (fileList[count-1] != 3 or fileList[count + 1] != 3)):
			fileList[count] = randint(1, 3)
		if(fileList[count-1] == 3 or fileList[count + 1] == 3):
			tempI = randint(1, 3)
			if(tempI == 1):
				fileList[count] = 1
			if(tempI == 2):
				fileList[count] = 2
			if(tempI == 3):
				fileList[count] = 4	
		if(fileList[count-1] == 3 and fileList[count] == 3):
			fileList[randint(count-1, count)] = randint(1, 2)	
		if(fileList[count-1] == 4 and fileList[count] == 4):
			fileList[randint(count-1, count)] = randint(1, 3)
		count+=1
	return fileList	

def createHaiku1():
	sylList1 = getRandomSyllableList(5)
	sylList2 = getRandomSyllableList(7)
	sylList3 = getRandomSyllableList(5)

	fileList1 = getRandomFileList(len(sylList1))
	fileList2 = getRandomFileList(len(sylList2))
	fileList3 = getRandomFileList(len(sylList3))

	haikuStr = ("\n" + createLine(1, sylList1, fileList1) + "\n" + 
				createLine(2, sylList2, fileList2) + "\n" + 
				createLine(3, sylList3, fileList3) + "\n")

	return haikuStr

def createHaiku2():
	sylList1 = getRandomSyllableList(5)
	sylList2 = getRandomSyllableList(7)
	sylList3 = getRandomSyllableList(5)
	fileList1 = getRandomFileList(len(sylList1))
	fileList2 = getRandomFileList(len(sylList2))
	fileList3 = getRandomFileList(len(sylList3))

	haikuStr = ("\n" + createLine(1, sylList1, editLine(len(sylList1), fileList1)) + "\n" + 
				createLine(2, sylList2, editLine(len(sylList2), fileList2)) + "\n" + 
				createLine(3, sylList3, editLine(len(sylList3), fileList3)) + "\n")

	return haikuStr
