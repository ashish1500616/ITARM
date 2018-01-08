import sys 

file1=open("mushroom.txt","r")
file1.readline()


file2=open("mush4.txt","a+")
file2.seek(0)
file2.truncate()
l = list(file1)
count=1
for n in l[6000:]:
	var=[0]*120
	count+=1
	print(count,"\n")
	eachline=n.split(" ")
	del eachline[-1]

	for d in eachline:
		var[int(d)]=1
	
	file2.write(str(var))
	



file1.close()
file2.close()


# print((int((list(file1)[1]).split(" ")[0])))
# sys.exit()

# var=[0]*119


# print("val d =",d,"\n"