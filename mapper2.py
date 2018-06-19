#!/usr/bin/env python

import sys
for line in sys.stdin:
	key, value = line.split("\t")
	if len(key)<=2:
		print ("{0}\t{1}".format("Total-"+key, value))#print the value of the class label as Total + class label to differentiate from other keys
	#remove the trailing part of the keys for other attributes to generalise them into either -1,0,1 ie:-the class they belong to
	else:
		a,b=key.split("_")
		if(value==0): 
			value=value+1 #normalisation
		print ("{0}\t{1}".format(b, value))



