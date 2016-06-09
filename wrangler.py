#! /usr/bin/env python

#This program will have as input a species name from a list
#The output will be anything requested from a number of dictionaries

import re
import sys #for arguments
import csv #seems unecessary

#arguments = sys.argv
#species_data = sys.argv[1] #filename is argument 1
#with open (species_data, 'ru') as f:
	
	#data = list (list(rec) for rec in csv.reader(f, delimiter=','))

Morphodict = {}
#Geodict = {}
#Makerdict = {}
#Referencedict = {}

#open a file
InFileName = sys.argv[1]
datafile = open (InFileName,"r")

#DNAseq=raw_input ('Enter species name: ')

LineNumber = 0


for Line in datafile:
	Line = Line.strip()

	if LineNumber == 0:
		Headerlist = Line.split( ':' )
		#print ("Header List " + str(Headerlist))
	else:
	   	Datalist = Line.split( ':' )
		#print ("Species data" + str(Datalist))
		#Datalist[2] = Datalist[2].split ( ',' )
		Specieskey = (Datalist[2].replace(';',',').replace(',','').split ( ' ') [0])



		print ('SPECIES'' {}'.format (Datalist[2]))

		Morphodict [ str(Specieskey) ] = [Datalist [1] , Datalist [3] , Datalist [4]]
		#Geodict [str(Specieskey)] = Datalist [1]
		#Makerdict [str(Specieskey)] = Datalist [3]
		#Referencedict [str(Specieskey)] = Datalist [4]


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
print ("Species Searched:")
print ("\n")
print (Specieskey)
print ("\n")

if Specieskey not in Morphodict:
	print ("Go find it")
else:
	if "geography" in Attributes:
		print ("Result: Geography")
		print (Morphodict[Specieskey][0])

	if "maker" in Attributes:
		print ("Result: Maker")
		print (Morphodict[Specieskey][1])

	if "reference" in Attributes:
		print ("Result: Reference")
		print (Morphodict[Specieskey][2])

	if "all" in Attributes:
		print ("Result: All Data")
		print (Morphodict[Specieskey])
	print ("\n")

	print ("Analysis Concluded")

	print ("\n")

# Print the column header
#print ( '\t'.join(fields) )
# Print the requested field for each
#print (Morphodict[fields])




	#print (Line)
#print "Name of file:", datafile.name


#readlines (trace.csv)
#InFileName = trace.csv
#InFile = open ( InFileName, "r" )
#LineNumber = 0
#for Line in InFile:
#	Line = Line.split(",")


#print list

datafile.close()

 
