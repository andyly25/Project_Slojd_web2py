import os

# Enter a number to get a file based on syllable count
# EX: getNounFile(3) = gets 3 syllable noun file

def getWordFile(fileNumR, sylNumR):
	if fileNumR == 1:
		return getNounFile(sylNumR)
	if fileNumR == 2:
		return getAdjFile(sylNumR)
	if fileNumR == 3:
		return getVerbFile(sylNumR)
	if fileNumR == 4:
		return getAdverbFile(sylNumR)

def getNounFile(sylNumN):

	return list(filter(None, fetchFile(1, sylNumN)))

def getAdjFile(sylNumAj):

	return list(filter(None, fetchFile(2, sylNumAj)))

def getVerbFile(sylNumV):

	return list(filter(None, fetchFile(3, sylNumV)))

def getAdverbFile(sylNumAv):

	return filter(None, fetchFile(4, sylNumAv))
def fetchFile(fileNum, sylNum):
	fileLines = fetchFilePath(fileNum, sylNum).read().split('\r\n')
	if os.name == 'nt':
		fileLines = fetchFilePath(fileNum, sylNum).read().split('\n')
	fetchFilePath(fileNum, sylNum).close
	return fileLines

def fetchFilePath(fileNumP, sylNumP):
	return open(fetchFileStrPath(fileNumP, sylNumP), "r")

def fetchFileStrPath(filePathNum, sylNum):
	basePath = os.path.dirname(os.path.abspath(__file__))
	nounsFilePath = os.path.abspath(os.path.join(basePath, "../static/dict/nouns"))
	adjFilePath = os.path.abspath(os.path.join(basePath, "../static/dict/adjectives"))
	verbFilePath = os.path.abspath(os.path.join(basePath, "../static/dict/verbs"))
	adverbFilePath = os.path.abspath(os.path.join(basePath, "../static/dict/adverbs"))

	if filePathNum == 1:
		return nounsFilePath + "/" + str(sylNum) +"syllablenouns.txt"

	if filePathNum == 2:
		return adjFilePath + "/" + str(sylNum) +"syllableadjectives.txt"

	if filePathNum == 3:
		return verbFilePath + "/" + str(sylNum) +"syllableverbs.txt"

	if filePathNum == 4:
		return adverbFilePath + "/" + str(sylNum) +"syllableadverbs.txt"
