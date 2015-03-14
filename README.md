# Project_Slojd_web2py

Andy Ly
Joseph Ou
Shivam Dave

***THIS FILE IS ON HOW TO RUN THE PROGRAM, CHECK THE ABOUT FILE FOR INFO ABOUT FILES/DIRS***

## How to run:
Make sure you install Web2Py by instructions online.
http://www.web2py.com/init/default/download

Running through web2py:
	There are two different ways to run the project. You can either unpack the packed file that we included or clone the project fold into your web2py/applications folder and it should appear. Either way works and we included directions for both in case one did not work.

	Prior to trying one or both ways you must download and install web2py.

	To use web2py:
		Go onto your terminal and run the project with web2py or type "python web2py.py" into your terminal

		Once it starts, there would be some popup. Add in some password and connect to the server. 
		On a browser, some http://127.0.0.1:8000/welcome/default/index should appear.

<<<<<<< HEAD
		Click on Administrative interface and type in your password. 
=======
Once done, just go onto your terminal and cd into the folder location of your web2py and type in: python web2py.py
>>>>>>> 4bd254ec6e7eb44c1fe1840bb7b7b15351114b75

	Way #1:
		1. First take the folder 'Project_Slojd_web2py' and place it into your web2py/applications folder.
		2. After going though the steps above about using web2py, the name of the folder you placed in applications should appear. Clicking on that would show our haiku maker website running.

	Way #2: 
		1. Go into the Administrative interface of web2py and then on the righthand side you will see the option to upload and install packed application. 
		2. Name it something and then upload the following package that was included within the zip: "web2py.app.Project_Slojd_web2py.w2p"
		3. Then click install
		4. After installing, the app will show up in your list and you can run it by clicking it

*Note: The program has been tested on Mac OSX, Ubuntu 12.04, and Windows 7 64 bit.

Online Version:
	Go to the url "http://shivamndave.pythonanywhere.com" to see a live version of the program and what it should run like.

Check the ABOUT file to see a short breakdown of each of the directories and what to expect within each.
  
<<<<<<< HEAD
## When running the project
There are 3 sections to our Haiku Project: A pure random haiku, a better/2.0 haiku, and an input haiku. Here are some descriptions/expectations of each.

Purely Random Haiku:
	This haiku is 100% random. It does not take into account nouns, verbs, etc. The only thing it cares about is syllable count. As long as the syllable count is correct, it will choose any word that fulfills it. As a result of this we can get some great haikus and others that are terrible. This was our first iteration of the haiku generator during the project.

Haiku 2.0:
	This haiku takes the purely random haiku and slightly adjusts it. What it does is it takes that haiku and iterates through it. While iterating through it, it applies some grammar/english rules in order to increase chances that a "better" haiku is made. Ofcouse this is likely to not create a fully sensible haiku, however we found that it was slightly better. Some grammar rules implemented include only letting adverbs appear to modify verbs (but this is still random), not allowing back to back verbs, and increasing the chances that verbs are followed properly by nouns/adjectives instead of other verbs.

Create (input haiku):
	This haiku is also a pure random haiku, however the user can enter in three words. After entering these three words, a haiku is generated that takes each word entered, and inserts each into a separate line of the haiku. Note that the words entered are completely dependent on our dictionary and alot of common words are not in these dictionaries for some reason. If you enter a word that is not in our dictionary, you will be noted and can enter other words to try. 
=======
## In the project
There shall be Haikus!
In the site there will be a Haiku that would be generated the moment you enter. This is from the Haiku Version 2.0 that shows by default. 
There's 3 buttons on type and if you click on "Purely Random Haiku", it would generate a random Haiku.

In Create, due to time constraints, if you type in three words that are contained in our dictionary, each line of the Haiku would contain your word. If one of the words is not contained, it would not show anything.
>>>>>>> 4bd254ec6e7eb44c1fe1840bb7b7b15351114b75
