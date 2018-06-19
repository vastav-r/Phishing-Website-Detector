#!/usr/bin/env python

import sys
# values for each attribute depending on the input tupple
#example tupple 1,1,1,1,1,1,1,1
popup_t="1" 
sslf_t="1" 
requ_t="1"
urlanchor_t="1"
webtraffic_t="1"
urllen_t="1"
age_t="1"
havingip_t="1"

#loop through input lines
for line in sys.stdin:
	data = line.strip().split(",")
	#obtain attributes per each data entry
	popup, sslf, requ, urlanchor, webtraffic, urllen, age, havingip, result = data
	#select the attribute which matches the questions attribute value and then find its result and map its count as 1
	if sslf==sslf_t and result=="-1":	
		print ("{0}\t{1}".format("sslf_neg", 1))
	if sslf==sslf_t and result=="0"	:
		print ("{0}\t{1}".format("sslf_zero", 1))
	if sslf==sslf_t and result=="1"	:
			print ("{0}\t{1}".format("sslf_pos", 1))
	if popup==popup_t and result=="-1":	
		print ("{0}\t{1}".format("popup_neg", 1))
	if popup==popup_t and result=="0":	
		print ("{0}\t{1}".format("popup_zero", 1))
	if popup==popup_t and result=="1":	
		print ("{0}\t{1}".format("popup_pos", 1))
	if requ==requ_t and result=="-1":	
		print ("{0}\t{1}".format("requ_neg", 1))
	if requ==requ_t and result=="0"	:
		print ("{0}\t{1}".format("requ_zero", 1))
	if requ==requ_t and result=="1"	:
		print ("{0}\t{1}".format("requ_pos", 1))
	if urlanchor==urlanchor_t and result=="-1":	
		print ("{0}\t{1}".format("urlanchor_neg", 1))
	if urlanchor==urlanchor_t and result=="0":	
		print ("{0}\t{1}".format("urlanchor_zero", 1))
	if urlanchor==urlanchor_t and result=="1" :	
		print ("{0}\t{1}".format("urlanchor_pos", 1))
	if webtraffic==webtraffic_t and result=="-1":	
		print ("{0}\t{1}".format("webtraffic_neg", 1))
	if webtraffic==webtraffic_t and result=="0"	:
		print ("{0}\t{1}".format("webtraffic_zero", 1))
	if webtraffic==webtraffic_t and result=="1"	:
		print ("{0}\t{1}".format("webtraffic_pos", 1))
	if urllen==urllen_t and result=="-1"	:
		print ("{0}\t{1}".format("urllen_neg", 1))
	if urllen==urllen_t and result=="0"	:
		print ("{0}\t{1}".format("urllen_zero", 1))
	if urllen==urllen_t and result=="1"	:
		print ("{0}\t{1}".format("urllen_pos", 1))
	if age==age_t and result=="-1"	:
		print ("{0}\t{1}".format("age_neg", 1))
	if age==age_t and result=="0"	:
		print ("{0}\t{1}".format("age_zero", 1))
	if age==age_t and result=="1"	:
		print ("{0}\t{1}".format("age_pos", 1))
	if havingip==havingip_t and result=="-1" :	
		print ("{0}\t{1}".format("havingip_neg", 1))
	if havingip==havingip_t and result=="0"	:
		print ("{0}\t{1}".format("havingip_zero", 1))
	if havingip==havingip_t and result=="1"	:
		print ("{0}\t{1}".format("havingip_pos", 1))
	print ("{0}\t{1}".format(result, 1)) #this is used to count the no Phishing, suspiciuos and normal websites in the dataset
	
