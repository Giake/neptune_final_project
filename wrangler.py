#! /usr/bin/env python

#This program will have as input a species name from a list
#The output will be anything requested from a number of dictionaries


import re

#area_dict ={}
#age_dict = {}
#maker_dict = {}
#reference_dict = {}
#total_dict ={}
#age_dict["C.tenella": Sweden]
#print age_dict

#open a file
datafile = open ("trace.csv","rw+")
print "Name of file:", datafile.name

list = open ("trace.csv").readlines()

#readlines (trace.csv)

#InFileName = trace.csv

#InFile = open ( InFileName, "r" )

#LineNumber = 0

#for Line in InFile:
#	Line = Line.split(",")

headertypes = []

speciesdata = []

print list


 
