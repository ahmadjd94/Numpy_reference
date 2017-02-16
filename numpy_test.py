#! ~/user/bin/python3
# This code file is used as a reference for numpy 

import numpy as np  # import the numpy library and add an alias to it\
import random
test_list = []

for i in range(100): #create a list of 100 random number
  test_list.append(random.randint(-100000,100000))

print (test_list)
print(type(test_list))
np_array = np.array(test_list) # creating a numpy array out of regular python list

#_______________________________________________________________
#numpy is powerful for running element wise operations on array
# array are homoginous(only contains element of the same type)
#_______________________________________________________________

print(type(np_array))

#_______________________________________________________________
print ("printing results of performing element wise operation on numpy array")

print ("performing addition")
test = np_array /2
print (test)
print ("performing multiplication")
test1 = np_array *2
print (test1)
#_______________________________________________________________
# when creating a numpy array out of python list some casting may occur
# boolean types will be casted to integers if list contained bool and ints
# all will be casted to strings if the list contained strings
#_______________________________________________________________

# numpy arrays support subsetting
print (test1[:5])

#_______________________________________________________________
# numpy validations:
# performing validations on elemnts array
print(test1 > 0)
#_______________________________________________________________

# grabbing every element which satisfies a certain validation\
test4=test1[test1 > 0]
print (test4)

#_______________________________________________________________
# performing element wise ops on 2 array

test_negative = test1 * -1

zeroes= test_negative + test1

print(zeroes)
#_______________________________________________________________
#numpy supports 2d arrays 
array_2d = [[1,2,34215,4326,6547,2],[3214,235,2346,547,5685,2354],[2345234,625246,3412515,3234,6154]]
test_2d=np.array(array_2d)
#_______________________________________________________________
#Operations on 2D arrays:
#printing cols
print(test_2d)
print(test_2d[1]) #print first raw
#print a range of columns 
print(test_2d[:2])
#print every 2 and third col of every raw
print("_________________________")
print (test_2d[:][2:4])
# rowwise  ops
print("_________________________")
print (test_2d[2] * 2 ) # needs further checking 
#_______________________________________________________________
test_2d = np.array([[1,2,4326,6547,2],[3214,235,547,5685,2354],[2345234,625246,3412515,3234,6154]])
print (test_2d)
print (test_2d.shape)
#array. shape prints the struture of the array
#print 3rd to fifth col of the 2d array
print (test_2d[:,3:])
print (test_2d[:][3:]) # totally different from the above line
#print  the third row only 
print (test_2d[2])
#___________________________________________________________________
#Numpy Functions :
#median
print (np.median(test_2d[1]))
#mean
print (np.mean(test_2d[1]))
#__________________________________________________________________
# generating data 
height = np.round(np.random.normal(1.75,0.2,5000))
print (len(height))
print (height)
# generate dummy data for the age array
age = np.round(np.random.normal(75,20,5000))
print (len(age))
print (age)
# combining the resulting arrays to form a 2d array
data = np.column_stack((height,age))
print ([data[1]>50])
##############################################################
##############################################################
##############################################################
##############################################################
######################## Using pandas ########################
##############################################################
##############################################################
##############################################################
##############################################################
#pandas is a powerful csv handeling librarty that is based on numpy 
#opening a csv file 
import pandas as ps
csv_data=ps.read_csv("filename.csv",index_col=0)
#after reading the file
#getting an array that indicates if some elements satisfy some condition
csv_data['col']>10000
#select every element based on a comparison
csv_data [csv_data['col']>10000]
#inserting a new column inside the reader object
csv_data['new-col']=csv_data['some_col'] *4132
#########################################
#dealing with dates in pandas 













###############################################
###############################################
###############################################
###################side notes##################
###############################################
###############################################
###############################################
from datetime import datetime
a=datetime.now()
a.strftime()
#########this should be done with a map ??
csv_data['date']=datetime.strptime(str(csv_data['sale_date']),'%a %b %d %H:%M:%S EDT %Y')


