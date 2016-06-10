#! /usr/bin/env python

#This program will have as input a species name from a list
#The output will be anything requested from a number of dictionaries

import re
import sys #for arguments
import csv #seems unecessary if i dont directly open .csv files


#only one dictionary is necessary and has to be defined with {}
Morphodict = {}
#Geodict = {}
#Makerdict = {}
#Referencedict = {}

#open a file as input in argument position [1]
InFileName = sys.argv[1]
datafile = open (InFileName,"r")

LineNumber = 0


for Line in datafile:
	Line = Line.strip()

	if LineNumber == 0:
		Headerlist = Line.split( ':' )
		#print ("Header List " + str(Headerlist))
	else:
	   	Datalist = Line.split( ':' )
		#print ("Species data" + str(Datalist)) 1ST STOP
		#Datalist[2] = Datalist[2].split ( ',' )
		Specieskey = (Datalist[2].replace(';',',').replace(',','').split ( ' ') [0])



		print ('SPECIES'' {}'.format (Datalist[2]))

		Morphodict [ str(Specieskey) ] = [Datalist [1] , Datalist [3] , Datalist [4]]


		if len(Datalist [1]) == 0: print ('\t''?') 
		else: print ('\t''{}'.format (Datalist[1]))
		if len(Datalist [3]) == 0: print ('\t''?') 
		else: print ('\t''{}'.format (Datalist[3]))
		if len(Datalist [4]) == 0: print ('\t''?') 
		else: print ('\t''{}'.format (Datalist[4]))

 

	LineNumber = LineNumber + 1 

#print (Morphodict) 

# Get the columns wanted by the user, which follow the file name
fields = sys.argv[2:]
Specieskey = fields[0]
Attributes = fields[1:]

print ("\n\n\n")
print (">>>:Species Searched:<<<")
print ("\n")
print (Specieskey)
#print ("\n")

if Specieskey not in Morphodict:
	print ("!Go find it!")
else:
	if "geography" in Attributes or "geo" in Attributes:
		print ("\n")
		print ("Result: Geography")
		print (Morphodict[Specieskey][0])

	if "maker" in Attributes:
		print ("\n")
		print ("Result: Maker")
		print (Morphodict[Specieskey][1])

	if "reference" in Attributes or "ref" in Attributes:
		print ("\n")
		print ("Result: Reference")
		print (Morphodict[Specieskey][2])

	if not Attributes or "all" in Attributes:
		print ("\n")
		print ("Result: All Data")
		print ('Geography: ''{}''\n''Maker: ''{}''\n''Reference: ''{}'.format ((Morphodict[Specieskey][0]),(Morphodict[Specieskey][1]),(Morphodict[Specieskey][2])))

	print ("\n")
	print ("~~Search Concluded~~")
	print ("\n")


datafile.close()

 
