import csv
import sys
import itertools
import pandas as pd
# import time
# start_time = time.time()
# print("Start time {d}".format(d=start_time))
# open the csv file containg the data


class Frequency(object):
    def __init__(self, fileName,sup):
        self.fileName = fileName
        self.data = []
        self.support = sup
        self.firstFrequentSet = []
        self.firstCounterset = []
        self.nameOfProducts = []
        self.noOfProducts = 0

        self.indexCount = 0

        self.secondCandidateSet = []
        self.secondCandidateSupport = []
        self.secondCandidateDict = {}
        self.secondFrequentSupportZip = []
        self.secondFrequentSet = []
        self.secondFrequentProduct = []

        self.KCandidateSet = []
        self.KCandidateSupport = []
        self.KFrequentSupportZip = []
        self.KFrequentSet = []
        self.startPartition=[]
        self.endPartition=[]



    def openFile(self):
        # self.data=open(self.fileName).readlines()
        with open(self.fileName) as csvfile:
            self.data = list(csv.reader(csvfile, delimiter=' '))

    def createFirstCandidate(self):
        nameOfProducts = self.data[0][0].split(',')
        noOfProducts = len(nameOfProducts)
        self.firstCounterset = [0] * (noOfProducts + 1)
        for i in range(0, noOfProducts -1 ):
            for j in range(1, len(self.data) - 1):
                if self.data[j][0].split(',')[i] == "1":
                    self.firstCounterset[i] += 1
            if self.firstCounterset[i] > ((self.support / 100) * len(self.data)):
                self.firstFrequentSet.append(i)

    def createSecondCandidateSet(self):
        for combination in itertools.combinations(self.firstFrequentSet, 2):
            self.secondCandidateSet.append(combination)
        self.secondCandidateSupport = [0] * len(self.secondCandidateSet)
        self.startPartition=[1] * len(self.secondCandidateSet)
        self.endPartition=[1] * len(self.secondCandidateSet)

    def searchSecondCandidatesInTransaction(self):
        temp = []

        for i in range(len(self.data)):
            self.indexCount = i
            #searching combinations in each row.
            for index, val in enumerate(self.secondCandidateSet):
                if(len(
                list(
                filter(
                lambda x: x == 1, map(self.checkDataAtCell, val)))) == len(val)):
                    self.secondCandidateSupport[index] += 1
        self.secondFrequentSupportZip = list(
            zip(
            self.secondCandidateSet,
            self.secondCandidateSupport,
            self.startPartition,
            self.endPartition))
        # print(self.secondFrequentSupportZip)
        # sys.exit()
        # creating second candidate Dictionary# import time
# start_time = time.time()
# print("Start time {d}".format(d=start_time))
        for i in range(len(self.secondCandidateSet)):
            self.secondCandidateDict[self.secondCandidateSet[i]
                                     ] = list((self.secondCandidateSupport[i],
                                     self.startPartition[i],
                                     self.endPartition[i]))
        self.secondFrequentSet = (
        list(
        filter(lambda x: x != None, map(
            self.filterCandidateSet, self.secondFrequentSupportZip))))
        for data in self.secondFrequentSet:
            for dt in data:
                temp.append(dt)
        self.secondFrequentProduct = list(set(temp))

    def checkDataAtCell(self, l):
        if(l != ""):
            ind = l
            if self.data[self.indexCount][0].split(',')[ind] == "1":
                return 1

    def filterCandidateSet(self, x):
        if x[1] >  ((self.support/100)*len(self.data)):
            # if x[1]>((self.support/100)*len(self.data)):
            return x[0]

    def createKCandidateSet(self):
        for l in range(3, len(self.secondFrequentProduct) + 1):
            for s in itertools.combinations(self.secondFrequentProduct, l):
                self.KCandidateSet.append(s)
        self.KCandidateSupport = [0] * len(self.KCandidateSet)

    def searchKCandidateSet(self):
        for i in range(len(self.data)):
            #print("Transaction number {i} is being checked".format(i=i))
            self.indexCount = i
            for index, val in enumerate(self.KCandidateSet):
                if(len(list(filter(lambda x: x == 1, map(self.checkDataAtCell, val)))) == len(val)):
                    self.KCandidateSupport[index] += 1
        self.KFrequentSupportZip = list(
            zip(self.KCandidateSet, self.KCandidateSupport))
        self.KFrequentSet = (list(filter(lambda x: x != None, map(
            self.filterKCandidateSet, self.KFrequentSupportZip))))
        # print("self.KFrequentSet)

    def filterKCandidateSet(self, x):
        if x[1] >  ((self.support/100)*len(self.data)):
            return x



# minDict={},maxDict={}
# MOCK_DATA.csv
# MOCK_DATA2.csv
file1=input("Enter the name of the FILE1:::   ")
file2=input("Enter the name of the FILE2:::   ")
sup_t=int(input("The support for the FILE1:::   "))
print("Support Variable For File 1 is {d}".format(d=sup_t ))
sup2_t=int(input("The support for the FILE2:::   "))
print("Support Variable For File 1 is {d}.".format(d=sup2_t ))
object = Frequency(file1,sup_t)
object.openFile()
object.createFirstCandidate()
print("File1 : First Frequent Set {d1}".format(d1=object.firstFrequentSet))
print("\n\n")
object.createSecondCandidateSet()
object.searchSecondCandidatesInTransaction()
print("File1: Second Candidate Set\n {d1}".format(
    d1=object.secondCandidateDict))
print("\n\n")
object.createKCandidateSet()
print("Creation of KCandidateSet done starting searching for K candidate.")
object.searchKCandidateSet()
print(" searching for K candidate Set done.")

# print("File 1: KCandidateSet \n {data}".format(data=object.KFrequentSet))
print("\n\n")

print("Started working on second Partition")

object2 = Frequency(file2,sup2_t)
object2.openFile()
object2.createFirstCandidate()
print("File2 : First Frequent Set {d1}".format(d1=object2.firstFrequentSet))
print("\n\n")
object2.createSecondCandidateSet()# for key,value in object.secondCandidateDict:
# 	secondFrequentSet[key]=value

# for key,value in object2.secondCandidateDict:
# 	secondFrequentSet[key]=value

#print("Second Frequent Set {d1}".format(d1=secondFrequentSet))
object2.searchSecondCandidatesInTransaction()
print("File2: Second Candidate Set\n {d1}".format(
    d1=object2.secondCandidateDict))
print("\n\n")
if(len(object.secondCandidateDict) >= len(object2.secondCandidateDict)):
    minDict = object2.secondCandidateDict
    maxDict = object.secondCandidateDict
else:
    minDict = object.secondCandidateDict
    maxDict = object2.secondCandidateDict

# print("minDict{data}".format(data=minDict.viewitems()))
# print("maxDict{data}".format(data=maxDict.viewitems()))

print("File2: Creating Second Frequent Set ")
print("\n\n")
# print("Taken 50 as the support variable for File2.")
secondFrequentSet = {}
for key in minDict:
    if key in maxDict:
        val = minDict[key][0] + maxDict[key][0]
        if val > sup2_t:
            secondFrequentSet[key] =maxDict[key]
            secondFrequentSet[key][0]=val

print("File 2: SecondCandidateSet Before Deletion{data}".format(
    data=object2.secondCandidateDict))
print("\n\n")
for key in secondFrequentSet:
    del object2.secondCandidateDict[key]
    del object.secondCandidateDict[key]


temp = list(object.secondCandidateDict.keys())
for key in temp:
    if object.secondCandidateDict[key][0] < ((sup2_t/100)*len(object.data)+len(object2.data)):#(initialLen+finalLen)
        del object.secondCandidateDict[key]
temp = list(object2.secondCandidateDict.keys())
for key in temp:
    if object2.secondCandidateDict[key][0] < ((sup2_t/100)*len(object2.data)):#40:#(finalLen)
        del object2.secondCandidateDict[key]

print("File2 :SecondCandidateSet After Deletion{data}".format(
    data=object2.secondCandidateDict))
print("\n\n")

secondFrequentSet.update(object2.secondCandidateDict)
secondFrequentSet.update(object.secondCandidateDict)

print("File 2: Second Frequent Set {data}".format(data=secondFrequentSet))
