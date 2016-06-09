#! /usr/bin/env python

#This program will have as input a species name from a list
#The output will be anything requested from a number of dictionaries

import re
import sys #for arguments
import csv

#arguments = sys.argv
#species_data = sys.argv[1] #filename is argument 1
#with open (species_data, 'ru') as f:
	
	#data = list (list(rec) for rec in csv.reader(f, delimiter=','))
#print(reader)
#	for row in data:
#		print row[0]
#		for data in row:
#			print data

Morphodict = {}

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

		Morphodict [ Specieskey ] = Datalist [0]

		if len(Datalist [1]) == 0: print ('\t''?') 
		else: print ('\t''{}'.format (Datalist[1]))
		if len(Datalist [3]) == 0: print ('\t''?') 
		else: print ('\t''{}'.format (Datalist[3]))
		if len(Datalist [4]) == 0: print ('\t''?') 
		else: print ('\t''{}'.format (Datalist[4]))

 

	LineNumber = LineNumber + 1 

print (Morphodict) 

	#print (Line)
#print "Name of file:", datafile.name


#readlines (trace.csv)
#InFileName = trace.csv
#InFile = open ( InFileName, "r" )
#LineNumber = 0
#for Line in InFile:
#	Line = Line.split(",")

headertype = []

speciesdata = []

#print list

datafile.close()

 
