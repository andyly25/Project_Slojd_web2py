from random import randint
from random import randrange
from random import shuffle
import sys
import glob
import errno
import HaikuMod
import UserInputMatching

# Creates a list of random syllables that add up to 
# the max number of syllables allowed in a line
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

# Creates a list of random file numbers that will be
# used to access the noun, adjective, verb, & adverb files
def getRandomFileList (size):
	fileList = []
	count = 0
	while (count < size):
		tempNum = randint(1, 4)
		fileList.append(tempNum)
		count+=1
	return fileList

# Adds random commas or periods at the end of lines
def randomEndPunc(line, lineNumber):
	line = line[:-1]
	commaRandInt = randint(1, 10)
	if(commaRandInt < 5 and lineNumber < 3):
		line += ","
	elif(commaRandInt < 5):
		line += "."
	return line	

# Adds random commas within lines and has an increased chance if 
# 2 adjectives or 2 of the same type of words are in a row
def randomMidPunc(line, ind, fList):
	commaRandInt = randint(1, 10)
	comma = ","
	if(fList[ind] == fList[ind+1] and fList[ind] == 2 and commaRandInt > 2):
		return comma
	elif((fList[ind] == fList[ind+1] and commaRandInt < 6) or commaRandInt < 3):
		return comma
	return ""

# Creates a haiku line using file number and syllable number lists
def createLine(lineNumber, fileCountList, sylCountList):
	retLine = ""
	ind = 0
	while(ind < len(sylCountList)):
		tempSy = sylCountList[ind]
		tempFi = fileCountList[ind]
		tempLines = HaikuMod.getWordFile(tempFi, tempSy)
		if (len(tempLines)-1 < 1):
			print("\n**ERROR**\n")
			break
		tempLinesNum = randrange(0, len(tempLines))
		retLine += tempLines[tempLinesNum]
		if(ind != (len(sylCountList)-1)):
			retLine += randomMidPunc(retLine, ind, fileCountList)
		retLine += " "
		ind += 1
	retLine = randomEndPunc(retLine, lineNumber)
	return retLine;	

# Takes in a file list and edits it so that it follows some grammar rules
# in order to increase chance of getting phrases that make sense
def editLine (size, fileList):
	count = 0
	while (count < size-1):

		# 2 nouns do not follow one another & increases chance of nouns being followed by verbs or adjectivesz
		if(fileList[count-1] == 1 or fileList[count + 1] == 1):
			fileList[count] = randint(2, 3)

		# adverbs not modifying verbs will be removed
		if(fileList[count] == 4 and (fileList[count-1] != 3 or fileList[count + 1] != 3)):
			fileList[count] = randint(1, 3)

		# verbs will not follow one another and adverbs will randomly modify verbs
		if(fileList[count-1] == 3 or fileList[count + 1] == 3):
			tempI = randint(1, 3)
			if(tempI == 1):
				fileList[count] = 1
			if(tempI == 2):
				fileList[count] = 2
			if(tempI == 3):
				fileList[count] = 4	

		# 3 adverbs do not follow one another	
		if(fileList[count-1] == 4 and fileList[count] == 4):
			fileList[randint(count-1, count)] = randint(1, 3)

		count+=1

	return fileList	

# Creates random file and syllable lists while incorporating an
# inputted word
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

# Randomizes the file and syllable lists that have the inputted word
# so the word can be anywhere within a line
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

# Puts together a haiku line using the inputted word and file/syllable count lists
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
			retLine += customWord
		else:
			tempLinesNum = randrange(0, len(tempLines))
			retLine += tempLines[tempLinesNum]
		if(ind != (len(sylCountList)-1)):
			retLine += randomMidPunc(retLine, ind, fileCountList)
		retLine += " "
		ind+=1
	retLine = randomEndPunc(retLine, lineNumber)
	return retLine;		

# Outputs the type 1 haiku, which is completely random
def createHaiku1():
	sylList1 = getRandomSyllableList(5)
	sylList2 = getRandomSyllableList(7)
	sylList3 = getRandomSyllableList(5)

	fileList1 = getRandomFileList(len(sylList1))
	fileList2 = getRandomFileList(len(sylList2))
	fileList3 = getRandomFileList(len(sylList3))

	haikuStr = ("\n" + createLine(1, fileList1, sylList1) + "\n" + 
				createLine(2, fileList2, sylList2) + "\n" + 
				createLine(3, fileList3, sylList3) + "\n")

	return haikuStr

# Outputs the type 2 haiku, which is random, but has more chances of
# being made up of phrases that make sense
def createHaiku2():
	sylList1 = getRandomSyllableList(5)
	sylList2 = getRandomSyllableList(7)
	sylList3 = getRandomSyllableList(5)
	fileList1 = editLine(len(sylList1), getRandomFileList(len(sylList1)))
	fileList2 = editLine(len(sylList2), getRandomFileList(len(sylList2)))
	fileList3 = editLine(len(sylList3), getRandomFileList(len(sylList3)))

	haikuStr2 = ("\n" + createLine(1, fileList1, sylList1) + "\n" + 
				createLine(2, fileList2, sylList2) + "\n" + 
				createLine(3, fileList3, sylList3) + "\n")

	return haikuStr2	

# Creates a line of a haiku that incorporates an inputted word
def createLine3(word, wordInfo, sylCount, lineNum):
	customLists = getCustomLists(sylCount, word, wordInfo)
	return createCustomLine(lineNum, word, customLists)
