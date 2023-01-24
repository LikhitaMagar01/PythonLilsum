print("hello")

# using correct datatype is necessary for effeciency, security and retening a meaning
# python:
# List
getList = ["quill", "wheel", "eraser", "referee", "trouser"]
# print(getList)
# -- use to store multiple items in a single variable
# -- one of the built-in data types 
# -- store collections of data
# -- use square bracket
# -- create ordered, changable list and allow duplicates
# to determine lenght of list: len()
# print(len(getList))
# to determine type of list: type
# print(type(getList))

# list() constructor
getList = list(("quill", "wheel", "eraser", "referee", "trouser"))
# print(getList)

# access items
# you can access list item by its index number
# first item is index 0 last item is -1
# print(getList[3])

# range of index
# starts from 1 and end in 2 index; 3 is not included
# [:2] means first to 2; [2:] means 2 index to last
# print(getList[1:3])
# print(getList[-5:-2])
# check item in list
getList = ["quill", "wheel", "eraser", "referee", "trouser"]
if 'eraser' in getList:
    print('yippe! it is there')
# change item value
getList[3]= "rose water"
# print(getList[3])

# change item in range
getList[1:3]=["worried", "error"]
# print(getList[1:3])

# insert item acc to index
getList.insert(1, "quiet")
# print(getList)

# add item
getList.append("young")
# print(getList)

# add list to list or tuple or set or dictionaries
addList=["hi", "namaste", "ohayo", 1]
getList.extend(addList)
# print(getList)

# remove 
# remove specific item
# getList.remove("quiet")
# print(getList)

# remove specific index
getList.pop(5)
# print(getList)

del getList[6]
# print(getList)

# remove last item
getList.pop()
# print(getList)

# clear list 
# clear item; keeps list
print(addList)
addList.clear()
# print(addList)

# loop in list
# for x in getList:
#     print(x)

# loop using index
# for i in range(len(getList)):
    # print(getList[i])

# while loop 
i = 1
while i < len(getList):
    print(getList[i])
    i = i+1

# sort list alphabetically
# case sensitive; priority to uppercase than lowecase
getList.sort()
print(getList)
getList.sort(reverse=True)
print(getList)
def func(n):
    return abs(n - 2)

numlist= [1,2,3,4,5,6,7]
numlist.sort(key=func)
# print(numlist)
thislist = ["quill", "Wheel", "Eraser", "Referee", "trouser"]
thislist.sort(key = str.lower)
# print(thislist)
thislist.reverse()
print(thislist)

# copy list
copyList = getList.copy()
print("copy list", copyList)

# set
# --unchangeable but can remove or add items as you want

# dictionaries
# -- ordered items

# one liner
onelist = ["quill", "wheel", "eraser", "referee", "trouser"]
# otherlist = [x for x in onelist if "e" in x]
# print(otherlist)
# variable = [expression for item in iterable if condition == true]
# otherlist = [x for x in onelist if x == "eraser"]
# print("it is use to erase")