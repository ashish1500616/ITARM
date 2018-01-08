import csv
import sys
import itertools
import pandas as pd
#open the csv file containg the data
with open('MOCK_DATA.csv') as csvfile:
	#start  timer 

	data=list(csv.reader(csvfile,delimiter=' '))
	# print(data[0][0].split(',')[1])
	# sys.exit()
	# for row in data:
	# 	print(row,end="\n")
	# 	f=open("DataList.txt","w+")
	# 	f.write(str(row)+'\n')
	# f.close()
	# sys.exit()

	tempList=[]
	supportVariabe=50
	indexCount=1
	supportList=[]
	supindex=0
	result=[]
	com2=[]
	secfinal=[]
	kfrequentset=[]
	# sys.exit()
	#print(data[0][0].split(','))

	# value at a cell in excel data[j][0].split(',')[i] == "TRUE"
	nameOfProductColumn=data[0][0].split(',')
	noOfProducts=len(nameOfProductColumn[1:])
	counterList=[nameOfProductColumn[0:],[0]*(noOfProducts+1)]
	finalList=[]
	output=[]
	combin=[]
	#print(type(counterList[1][37]))

	def updateCounterList():
		for i in range(1,noOfProducts+1):
			for j in range(1,len(data)-1):
				if data[j][0].split(',')[i] == "TRUE" :
					#print("Matched True")
					counterList[1][i]+=1
			if counterList[1][i]>supportVariabe:
				finalList.append(i)


	def printCounterList():
		for k in range(0,39):
			# for l in range(0,39):
				print(counterList[0][k],"   ",counterList[1][k])
			# print('\n')

	def printFinalList():
		for m in range(0,len(finalList)):
			print("Index      ProductName")
			print(finalList[m],"        ",counterList[0][finalList[m]])

	def createCombination():
		global supportList
		pfile="combinationList.txt"
		# create combination file txt
		f=open(pfile,"w+")
		#empty the content of the file
		f.seek(0)

		f.truncate()
		#create combination of all the indexes
		#for L in range(2, len(finalList)+1):
		for subset in itertools.combinations(finalList, 2):
			#global com2
			com2.append(subset)
		print(com2)
		supportList=[0]*len(com2)

		  	#f.write("%s\n"%str(subset))

		#close the file
		f.close()
		    #checkData(subset,L)
		# print("Combination\n",output)
	def nfrequencySet(d):
		global indexCount,kfrequentset
		print("Working for n frequency Set")
		for L in range(3, len(d)+1):
			combin=[]
			for subset in itertools.combinations(d, L):
				combin.append(subset)
			supportList=[0]*len(combin)
			for i in range(len(data)):
				indexCount=i
				for index,line in enumerate(combin):
					
					# sys.exit()
					if(len(list(filter(lambda x: x==1,map(parseDataCsv,line))))==len(line)):
						# print((line))
						# print((list(filter(lambda x: x==1,map(parseDataCsv,line)))))
						# print("Increasing")
						# print("SupportValue before",supportList[index])
						supportList[index]+=1
						# print("SupportValue after",supportList[index])
			sup=list(zip(combin,supportList))
			chedata=(list(filter(lambda x: x!=None,map(filt2,sup))))
			# print(chedata,"\n")
			kfrequentset.append(chedata)
		# end timer



	def readCombList():
		with open('combinationList.txt') as f:
			lines = f.read().split('\n')
		supportList=[0*len(lines)]

	def checkData():
		print("\t--->Row Checking")
		# global lines
		#print(int(lines[1].strip('(').strip(')').split(',')[1]))
		# print(lines[2000])
		# sys.exit()
		for index,line in enumerate(com2):
			#line=line.strip('(').strip(')').split(',')
			# print("Combination",line)
			# print("1 array",list(map(parseDataCsv,line)))
			# sys.exit()

			if(len(list(filter(lambda x: x==1,map(parseDataCsv,line))))==len(line)):
				supportList[index]+=1
		#sys.exit()
		


	def parseDataCsv(l):
		global indexCount
		#print(indexCount)
		if(l!=""):
			ind=l
			#sys.exit()
			if data[indexCount][0].split(',')[ind]=="TRUE":
				return 1




	# print("Updating CounterList")
	updateCounterList()
	# print("\nUpdate Completed \n")
	# print("\n CounterList \n")
	# printCounterList()

	# print("\n Final List \n")
	printFinalList()
	#print(finalList)
	# print("\n Combination \n")
	createCombination()
	# readCombList()
	# with open('combinationList.txt') as f:
	# 		lines = f.read()
	# lines=lines.split("\n")

	# # print(type(lines))
	# # sys.exit()
	# supportList=[0]*len(lines)
	# #print(supportList)
	for i in range(len(data)):
		indexCount=i
		print(i,end="")
		checkData()
	sup2=list(zip(com2,supportList))
	def filt2(x):
		if x[1]>(.20)*len(data):
			return x
	chedata=(list(filter(lambda x: x!=None,map(filt2,sup2))))
	kfrequentset.append(chedata)
	# print(chedata)
	print("Length =",len(chedata))
	for dt in chedata:
		for n in dt[0]:
			secfinal.append(n)
	secfinal2=list(set(secfinal))
	# print(secfinal2)
	nfrequencySet(secfinal2)





	#Creation of Frequency List Created
	g=open("2--frequentSet.txt","w+")
	g.seek(0)
	g.truncate()
	g.write(str(list(zip(com2,supportList))))
	g.close()
	
	# print("Frequency File Created")
	# # print(finalList+tempList)
	# #create Combination Frequency
	# print("Creating Combination Frequency")
	# h=open("CombinationFrequency.txt","w+")
	# h.seek(0)
	# h.truncate()
	# h.write(str(list(zip(lines,supportList))))
	# h.close()
	# print("Frequency of combination created")
	
	# #creation of combination list above support variable
	# # for count,data in 

	# i=open("CombinationAboveSupport.txt","w+")
	# i.seek(0)
	# i.truncate()

	# def traversupportList():
	# 	global result
	# 	for ind,val in enumerate(supportList):
	# 		if(val>30):
	# 			result.append(lines[ind])
	
	# # print(list(map(traversupportList,supportList)))
	# traversupportList()

	# #i.write(str(list(map(traversupportList,supportList))).strip('(').strip(')'))
	# i.write(str(result))
	# # for d in (list(map(traversupportList,supportList))):

	# # 	result.append(lines[d])
	# # i.write(str(result))
	# i.close()
	# print("Combination Above Support Text Created")




