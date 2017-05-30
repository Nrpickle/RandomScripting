#Nick McComb | www.nickmccomb.net
#Written October 2016 for OSURC
# v .1

#Wow, 80% formatting errors...

import csv
import sys
import re

#Removes all dashes and spaces from ID Numbers
def processIDNum(number):
  return number.translate(None, "- ")

def getEmail(row):
  if len(row[4]) > 2:
    return row[4]
  else:
    parsed = row[3].split("@")  #For the people who added @oregonstate.edu when they shouldn't have
    return parsed[0] + "@oregonstate.edu"
  
if(len(sys.argv) < 2):
  print "Please use command line arguments."
  quit()

f = open(sys.argv[1], 'rb')  #Open's the csv file

try:
  reader = csv.reader(f) #creates the reader object
  
  result = open('scriptOutput.txt', 'w')
  emailList = open('emailList.txt', 'w')
  
  counter = 0    
  improperFormatCount = 0
  UWInterest = 0
  print "Start processing..."
  for row in reader:
    if counter == 0: #Don't process the first line
      pass
    else:
      if(len(processIDNum(row[5])) == 9):
        pass
        if processIDNum(row[5]) in open('UWList.csv').read():  #Check the target file for any valid IDs
          UWInterest = UWInterest + 1
          result.write(getEmail(row) + '\n')
        #print "Found ID Number: " + processIDNum(row[5])
      else:
        print "Error in ID Number for " + row[1] + " " + row[2]
      if not '-' in row[5]:
        improperFormatCount = improperFormatCount + 1
    
    emailList.write(getEmail(row) + "\n")
    counter = counter + 1
  
  print "Total Formatting Error: " + str(round(float(improperFormatCount)/float(counter), 4) * 100) + "%"
  print "Total Members: " + str(counter - 1)
  print "Underwater Interest: " + str(UWInterest)
  
finally:
  f.close()
  result.close()
  emailList.close()
  
