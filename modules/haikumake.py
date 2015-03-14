from random import randint
from random import randrange
from random import shuffle
import sys
import glob
import errno
import HaikuMod
import userInputMatching

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

def randomEndPunc(line, lineNumber):
	line = line[:-1]
	commaRandInt = randint(1, 10)
	if(commaRandInt < 5 and lineNumber < 3):
		line += ","
	elif(commaRandInt < 5):
		line += "."
	return line	

def createLine(lineNumber, fileCountList, sylCountList):
	retLine = ""
	for tempSy, tempFi in zip(sylCountList, fileCountList):
		tempLines = HaikuMod.getWordFile(tempFi, tempSy)
		if (len(tempLines)-1 < 1):
			print("\n**ERROR**\n")
			break
		tempLinesNum = randrange(0, len(tempLines))
		retLine += tempLines[tempLinesNum] + " "
	retLine = randomEndPunc(retLine, lineNumber)
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

def getCustomLists (max, customWord, customWordInfo):
	startSylNum = customWordInfo[1]
	startFileNum = customWordInfo[0]

	sylList = [startSylNum]
	fileList = [startFileNum]

	remainSyl = max - startSylNum
	while (remainSyl > 0):
		if(remainSyl > 4):
			tempNum = randint(1, 4)
		else: 
			tempNum = randint(1, remainSyl)
		sylList.append(tempNum)
		remainSyl-=tempNum

	count = 1
	while (count < len(sylList)):
		tempNum = randint(1, 4)
		fileList.append(tempNum)
		count+=1

	((finalFileList, finalSylList), index) = randomizeCustomList(fileList, sylList)

	return ((finalFileList, finalSylList), index)

def randomizeCustomList(fList, sList):
	swap = randint(0, len(fList)-1)
	if(swap != 0):
		temp = fList[0]
		fList[0] = fList[swap]
		fList[swap] = temp
		temp = sList[0]
		sList[0] = sList[swap]
		sList[swap] = temp
	return ((fList, sList), swap)

def createCustomLine(lineNumber, customWord, ((fileCountList, sylCountList), swap)):
	retLine = ""
	ind = 0
	while(ind < len(sylCountList)):
		tempSy = sylCountList[ind]
		tempFi = fileCountList[ind]
		tempLines = HaikuMod.getWordFile(tempFi, tempSy)
		if (len(tempLines)-1 < 1):
			print("\n**ERROR**\n")
			break
		if(swap == ind):
			retLine += customWord + " "
		else:
			tempLinesNum = randrange(0, len(tempLines))
			retLine += tempLines[tempLinesNum] + " "
		ind+=1
	retLine = randomEndPunc(retLine, lineNumber)
	return retLine;		

def createLine3(word, wordInfo):
	theLists = getCustomLists(5, word, wordInfo)
	print theLists
	print createCustomLine(1, word, theLists)
	return word
