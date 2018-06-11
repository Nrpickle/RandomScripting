''' 

Written by Nick McComb
February 2016 

Renames files based on specific requirements. Originally designed for renaming
Law and Order (the original, of course) ripped DVDs for personal archival.

'''

from os import listdir, rename
from os.path import isfile, join
import re

fo = open("_namingScriptConfig.txt", "r")

#Skip the documentation lines
for i in range(10):
	fo.readline()

#Get Season from config file
seasonStr = fo.readline()
season = seasonStr.split(":")[1].strip('\n')

#Get name prefix from config file
namePrefixStr = fo.readline()
namePrefix = namePrefixStr.split(":")[1].strip('\n')

#Script Output Header
print "[Renaming LAW AND ORDER episode names...]"
print "[Reading config from: " + fo.name + "]"
print "[Current Season: " + str(season) + "]"
print "[Name Prefix: " + str(namePrefix) + "]"

mypath = "./" #Local path
#Find the files in the current directory
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#Only get the ones that need to be renamed
rawFiles = [f for f in onlyfiles if "RAW" in f]
#Get the files that are not rename targets
notRawFiles = [f for f in onlyfiles if "RAW" not in f]
#Get the files that are current episodes
currentEpisodes = [f for f in notRawFiles if "_" not in f]

print "##Current Raw Files: " + str(rawFiles)

#Now, we need to find the current episode number (cause we already have season)
#We're going to use... REGULAR EXPRESSIONS! Dun dun dun.

episodeNo = 0 #assume start of 0 (will be incremented to 1 if there are no matches)
txt='Law and Order S02E01'
#Configure regular expressions
re1='.*?'	# Non-greedy match on filler
re2='\\d+'	# Uninteresting: int
re3='.*?'	# Non-greedy match on filler
re4='(\\d+)'	# Integer Number 1

#Loop to find expressions
for ep in currentEpisodes:	
	rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
	m = rg.search(ep)
	if m:
		int1=m.group(1)
		#print "("+str(int(int1))+")"+"\n"
		if((int(int1) > episodeNo)):
			episodeNo = int(int1)

for targetFile in rawFiles:
	#Add one because this is where we want to make a new one
	episodeNo = episodeNo + 1
	
	#Generate the output string
	print "#New Episode Number: " + str(episodeNo)
	
	outputStr = namePrefix + " - S" + str(season).zfill(2) + "E" + str(episodeNo).zfill(2) + ".mp4"
	print "#Current output Str: " + outputStr
	
	print "### RENAMING " + targetFile + " TO " + outputStr
	rename(targetFile, outputStr)

print "[Script Finished]"
			
fo.close()