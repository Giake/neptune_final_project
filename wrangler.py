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


#open a file
InFileName = sys.argv[1]
datafile = open (InFileName,"r")

LineNumber = 0

for Line in datafile:
	Line = Line.strip()

	if LineNumber == 0:
		Headerlist = Line.split( ',' )
		#print ("Header List " + str(Headerlist))
	else:
	   	Datalist = Line.split( ',' )
		#print ("Species data" + str(Datalist))
		print ('SPECIES'' {}'.format (Datalist[2]))
		print ('\t''{}'.format (Datalist[1]))
		print ('\t''{}'.format (Datalist[3]))
		print ('\t''{}'.format (Datalist[4]))

	LineNumber = LineNumber + 1  

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

 
