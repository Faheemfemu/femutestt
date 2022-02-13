# 
# print('hello,wolrd' )
import array as arr
myarr=arr.array('i',[1,2,3,4])
# print(myarr)
#searchingElementInArray
# def searchInarray(array,value):
#     for i in array :
#         if i==value :
#             return array.index(value) 
#     return "the element does not exist in this array"
# print(searchInarray(myarr,4))
#deletingElementFromArray
myarr.remove(3)
print(myarr)
#traversearray
for i in myarr :
    print(i)

#accses individual element through index
print(myarr[2])
#append any value of array using append method
myarr.append(7)
print(myarr)
#INSERT Value in array using insert method
myarr.insert(1,9)
print(myarr)
#extend python array using extent method
myarr1=arr.array('i',[11,9,18,12])
myarr.extend(myarr1)
print(myarr)
#remove last element using pop method
myarr.pop()
print(myarr)
#fetch any element using index method

print(myarr.index(4))
#reverse a python array using reverse method
myarr.reverse()
print(myarr)
#get array buffer information use buffer_info method
print(myarr.buffer_info())
#check the number of accurance of an element using count methed
print(myarr.count(9))
#convert array to pyhon list with the same element  using tostring method
strTemp = myarr.tostring()
print(strTemp)
inst = arr.array('i')
inst.fromstring(strTemp)
print(inst)
#slice element from an array
print(myarr[2:5])
#2Darray
import numpy as np
myarr2=np.array([[1,2,3,3],[3,5,66,4] , [6,7,8,8],[4,6,8,8]] )
print(myarr2)
#searching element in 2d array
def searchTDarray(array, value):
    for i in range (len(array)):
        for j in range (len(array[0])):
            if array[i][j]==value:
                return 'the value is located at index '+str(i)+" "+str(j)
    return 'the element is not found'
print(searchTDarray(myarr2,4))
#deleting element in 2D array
newarray=np.delete(myarr2,0, axis = 1)
print(newarray)
    
