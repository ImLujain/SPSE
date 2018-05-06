#!/usr/bin/env python




import sys
sys.path.append('C:/Program Files (x86)/Immunity Inc/Immunity Debugger')
sys.path.append('C:/Program Files (x86)/Immunity Inc/Immunity Debugger/Libs')

import immlib 
import csv

#description
DESC = " Find all process and print them to csv file"

def main(args):


	#create a table and print the details 

	imm = immlib.Debugger()
	
	processList = imm.ps()
	 
	myFile = open('processList.csv', 'w')
	with myFile:
	    writer = csv.writer(myFile)
	    writer.writerows(processList)

	return "Success"
