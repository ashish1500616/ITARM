import csv
import sys
import itertools
import pandas as pd
#open the csv file containg the data

class Frequency(object):
	def __init__(self,fileName):
		self.fileName=fileName
		self.data=[]
		self.support=50
		self.firstFrequentSet=[]
		self.firstCounterset=[]
		self.nameOfProducts=[]
		self.noOfProducts=0

		self.indexCount=0

		self.secondCandidateSet=[]
		self.secondCandidateSupport=[]
		self.secondFrequentSupportZip=[]
		self.secondFrequentSet=[]
		self.secondFrequentProduct=[]

		self.KCandidateSet=[]
		self.KCandidateSupport=[]
		self.KFrequentSupportZip=[]
		self.KFrequentSet=[]


	def openFile(self):
		with open(self.fileName) as csvfile:
			self.data=list(csv.reader(csvfile,delimiter=' '))
			print(self.data)

	def createFirstCandidate(self):
		nameOfProducts=self.data[0][0].split(',')
		noOfProducts=len(nameOfProducts[1:])
		self.firstCounterset=[0]*(noOfProducts+1)
		for i in range(1,noOfProducts+1):
			for j in range(1,len(self.data)-1):
				if self.data[j][0].split(',')[i] == "TRUE" :
					self.firstCounterset[i]+=1
			if self.firstCounterset[i]>((self.support/100)*len(self.data)):
				self.firstFrequentSet.append(i)

	def createSecondCandidateSet(self):
		for combination in itertools.combinations(self.firstFrequentSet, 2):
			self.secondCandidateSet.append(combination)
		self.secondCandidateSupport=[0]*len(self.secondCandidateSet)

	def searchSecondCandidatesInTransaction(self):
		temp=[]

		for i in range(len(self.data)):
			self.indexCount=i
			for index,val in enumerate(self.secondCandidateSet):
				if(len(list(filter(lambda x: x==1,map(self.checkDataAtCell,val))))==len(val)):
					self.secondCandidateSupport[index]+=1
		self.secondFrequentSupportZip=list(zip(self.secondCandidateSet,self.secondCandidateSupport))
		self.secondFrequentSet=(list(filter(lambda x: x!=None,map(self.filterCandidateSet,self.secondFrequentSupportZip))))
		for data in self.secondFrequentSet:
			for dt in data:
				temp.append(dt)
		self.secondFrequentProduct=list(set(temp))

	def checkDataAtCell(self,l):
		if(l!=""):
			ind=l
			if self.data[self.indexCount][0].split(',')[ind]=="TRUE":
				return 1

	def filterCandidateSet(self,x):
		if x[1]>(20):#((self.support/100)*len(self.data))
			return x[0]

	def createKCandidateSet(self):
		for l in range(3,len(self.secondFrequentProduct)+1):
			for s in itertools.combinations(self.secondFrequentProduct, l):
				self.KCandidateSet.append(s)
		self.KCandidateSupport=[0]*len(self.KCandidateSet)

	def searchKCandidateSet(self):
		for i in range(len(self.data)):
			print("Transaction number {i} is being checked".format(i=i))
			self.indexCount=i
			for index,val in enumerate(self.KCandidateSet):
				if(len(list(filter(lambda x: x==1,map(self.checkDataAtCell,val))))==len(val)):
					self.KCandidateSupport[index]+=1
		self.KFrequentSupportZip=list(zip(self.KCandidateSet,self.KCandidateSupport))
		self.KFrequentSet=(list(filter(lambda x: x!=None,map(self.filterKCandidateSet,self.KFrequentSupportZip))))
		print(self.KFrequentSet)

	def filterKCandidateSet(self,x):
		if x[1]>(20):#((self.support/100)*len(self.data))
			return x






object=Frequency("MOCK_DATA.csv")
object.openFile()
object.createFirstCandidate()
print(object.firstFrequentSet)
object.createSecondCandidateSet()
object.searchSecondCandidatesInTransaction()
object.createKCandidateSet()
object.searchKCandidateSet()
