import csv
import sys
import itertools
with open('MOCK_DATA.csv') as csvfile:
	data=list(csv.reader(csvfile,delimiter=' '))
	tempList=[]
	supportVariabe=50

	def getData(i,j):
		return data[j][0].split(',')[i] 
	#print(data[1][0].split(',')[1])
	# print(len(data))

	# print(data[101][0].split(',')[38])

	# sys.exit()
	#print(data[0][0].split(','))

	# value at a cell in excel data[j][0].split(',')[i] == "TRUE"
	nameOfProductColumn=data[0][0].split(',')
	noOfProducts=len(nameOfProductColumn[1:])
	counterList=[nameOfProductColumn[0:],[0]*(noOfProducts+1)]
	finalList=[]
	output=[]
	print(type(counterList[1][37]))
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
		#output = sum([map(list, combinations(finalList, i)) for i in range(2,len(finalList) + 1)], [])
		# output = [list(range(i, j)) for i in range(1,len(finalList+2) for j in range(i+1,len(finalList+2)]

		for L in range(2, len(finalList)+1):
		  for subset in itertools.combinations(finalList, L):
		    print(subset)
		    checkData(subset,L)

		# print("Combination\n",output)

	def checkData(tparam,tlength):
		temp=len(finalList)
		print("Inside CheckData")
		append=False
		sameCombinationSellCounter=0
		for n in range(1,len(data)-1):
			c=0
			for o in range(0,tlength+1):
				if data[n][0].split(',')[o] == "TRUE":
					c+=1
			if(c==tlength):
				print("Product with same pattern Combnation Found Increasing Sell Counter")
				sameCombinationSellCounter+=1
			if sameCombinationSellCounter>=30:
				print("More than supportVariabe Inserting in the finalist")
				tempList.append(tparam)
				append=True
				print("tempList After Changes =",tempList)
				break
			c=0

	print("Updating CounterList")
	updateCounterList()
	print("\nUpdate Completed \n")
	print("\n CounterList \n")
	printCounterList()

	print("\n Final List \n")
	printFinalList()
	print(finalList)
	print("\n Combination \n")
	createCombination()

	print(finalList+tempList)

