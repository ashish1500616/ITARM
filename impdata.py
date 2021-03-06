import csv
import sys
import itertools
#open the csv file containg the data
with open('MOCK_DATA.csv') as csvfile:

	data=list(csv.reader(csvfile,delimiter=' '))
	# print(data[0][0].split(',')[1])
	# sys.exit()
	tempList=[]
	supportVariabe=50
	indexCount=1
	supportList=[]
	supindex=0
	result=[]
	# sys.exit()
	#print(data[0][0].split(','))

	# value at a cell in excel data[j][0].split(',')[i] == "TRUE"
	nameOfProductColumn=data[0][0].split(',')
	noOfProducts=len(nameOfProductColumn[1:])
	counterList=[nameOfProductColumn[0:],[0]*(noOfProducts+1)]
	finalList=[]
	output=[]
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
		
		pfile="combinationList.txt"
		# create combination file txt
		f=open(pfile,"w+")
		#empty the content of the file
		f.seek(0)
		f.truncate()
		#create combination of all the indexes
		for L in range(2, len(finalList)+1):
		  for subset in itertools.combinations(finalList, L):
		  	f.write("%s\n"%str(subset))
		#close the file
		f.close()
		    #checkData(subset,L)
		# print("Combination\n",output)

	def readCombList():
		with open('combinationList.txt') as f:
			lines = f.read().split('\n')
		supportList=[0*len(lines)]

	def checkData():
		print("\t--->Row Checking")
		global lines
		#print(int(lines[1].strip('(').strip(')').split(',')[1]))
		# print(lines[2000])
		# sys.exit()
		for index,line in enumerate(lines):
			line=line.strip('(').strip(')').split(',')
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
			ind=int(l)
			if data[indexCount][0].split(',')[ind]=="TRUE":
				return 1




	# print("Updating CounterList")
	updateCounterList()
	# print("\nUpdate Completed \n")
	# print("\n CounterList \n")
	# printCounterList()

	# print("\n Final List \n")
	#printFinalList()
	#print(finalList)
	# print("\n Combination \n")
	createCombination()
	# readCombList()
	with open('combinationList.txt') as f:
			lines = f.read()
	lines=lines.split("\n")

	# print(type(lines))
	# sys.exit()
	supportList=[0]*len(lines)
	#print(supportList)
	for i in range(len(data)):
		indexCount=i
		print(i,end="")
		checkData()
	# Creation of Frequency List Created
	g=open("frequencyList.txt","w+")
	g.seek(0)
	g.truncate()
	g.write(str(supportList))
	g.close()
	
	print("Frequency File Created")
	# print(finalList+tempList)
	#create Combination Frequency
	print("Creating Combination Frequency")
	h=open("CombinationFrequency.txt","w+")
	h.seek(0)
	h.truncate()
	h.write(str(list(zip(lines,supportList))))
	h.close()
	print("Frequency of combination created")
	
	#creation of combination list above support variable
	# for count,data in 

	i=open("CombinationAboveSupport.txt","w+")
	i.seek(0)
	i.truncate()

	def traversupportList():
		global result
		for ind,val in enumerate(supportList):
			if(val>30):
				result.append(lines[ind])
	
	# print(list(map(traversupportList,supportList)))
	# sys.exit()
	traversupportList()

	#i.write(str(list(map(traversupportList,supportList))).strip('(').strip(')'))
	i.write(str(result))
	# for d in (list(map(traversupportList,supportList))):

	# 	result.append(lines[d])
	# i.write(str(result))
	i.close()
	print("Combination Above Support Text Created")


