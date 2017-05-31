#Nick McComb | www.nickmccomb.net
#Written October 2016 for OSURC
# v .1

#Wow, 80% formatting errors...

import csv
import sys
import re
import time
import random
from getMajorFromEmail import getMajorFromEmail

def generateYear(major):
  if "Robotics" in major:
    return "Grad Student"
  elif "Pre" in major:
    year = random.randint(1,2)
  else:
    year = random.randint(3,5)
  if year == 1:
    return "First Year"
  elif year == 2:
    return "Second Year"
  elif year == 3:
    return "Third Year"
  elif year == 4:
    return "Fourth Year"
  elif year == 5:
    return "Fifth Year +"

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
writer = open('output_' + sys.argv[1], 'w')

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
      writer.write('First,Last,Major,Year\n')
      pass
    else:
      if counter == 1:
        print row
      if(len(processIDNum(row[4])) == 9):
        pass
        #Information to process here
        major = getMajorFromEmail(row[2] + "@oregonstate.edu")
        print "Email: " + row[2] + "@oregonstate.edu" + " has major " + major
        if major == 'No record found.':
          print "      !! No major found for " + row[0] + " " + row[1] + " !!"
        #Output row of information
        writer.write(row[0] + "," + row[1] + "," + major + "," + generateYear(major) + "\n")
        #row.append(major)
        time.sleep(.5)
        
        #print "Found ID Number: " + processIDNum(row[5])
      else:
        print "Error in ID Number for " + row[1] + " " + row[2]
      if not '-' in row[5]:
        improperFormatCount = improperFormatCount + 1
    
    emailList.write(getEmail(row) + "\n")
    counter = counter + 1
  
  print "Total ID Number Formatting Error: " + str(round(float(improperFormatCount)/float(counter), 4) * 100) + "%"
  print "Total Members: " + str(counter - 1)
  
finally:
  f.close()
  result.close()
  emailList.close()
  writer.close()
