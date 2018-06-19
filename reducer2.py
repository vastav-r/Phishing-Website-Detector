#!/usr/bin/env python

import math
import sys

last_key = None
running_total = 1
neg=1 #total no of negitive class labels
zero=1 #total no of class labels with value 0
pos=1	#total no of class labels with value 1
negnum=1; #multiply the numerator values of all atributes which belong to class label -1
posnum=1; #multiply the numerator values of all atributes which belong to class label 1
zeronum=1;	#multiply the numerator values of all atributes which belong to class label 0
total=0; #total no of entries  
for input_line in sys.stdin:
	input_line = input_line.strip()
	if len(input_line) >2:
		#print ("sd")
		key, value = input_line.split("\t",1)
		value = int(value)
		#print(last_key)
		#print(key)
		if   key=='Total-0':
			zero=value
		elif key=='Total--1':
			neg=value
		elif key=='Total-1':
			pos=value
		elif key=='zero':
			zeronum=zeronum*value; #neumarator multiplication of all the values which belong to class label 0
		elif key=='neg':
			negnum=negnum*value; #neumarator multiplication of all the values which belong to class label -1
		elif key=='pos':
			posnum=posnum*value; #neumarator multiplication of all the values which belong to class label 1
total=zero+pos+neg;

#finding the probability for each class label
zero=((zeronum/(math.pow(zero,8)))*(zero/float(total))) 
neg=((negnum/(math.pow(neg,8)))*(pos/float(total)))
pos=((posnum/(math.pow(pos,8)))*(neg/float(total)))


print( "%s\t%0.15f" % ("phishing probability",pos) )
print( "%s\t%0.15f" % ("suspicious probablity ",zero) )
print( "%s\t%0.15f" % ("benign website probablity ",neg) )
if(zero>neg and zero>pos):
	print("it is a suspicious website")
elif(pos>neg and zero<pos):
	print("it is a phishing website")
elif(zero<neg and neg>pos):
	print("it is a benign website")
else:	
	print("cannot be determined")



