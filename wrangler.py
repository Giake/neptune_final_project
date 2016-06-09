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

datafile = open ("trace.csv","r")

for Line in datafile:
	Line = Line.strip()
	print (Line)
#print "Name of file:", datafile.name


#readlines (trace.csv)
#InFileName = trace.csv
#InFile = open ( InFileName, "r" )
#LineNumber = 0
#for Line in InFile:
#	Line = Line.split(",")

headertypes = []

speciesdata = []

#print list

datafile.close()

 
