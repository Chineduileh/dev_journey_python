## WORKING WITH NUMERIC DATA TYPES

a=1
b=2.3
c= (1+2j)
print (type(a), type(b), type(c))

## WORKING WITH DICTIONARIES

names= {1: "Gloria", 2: "Kennedy"}
print (names[1])

## WORKING WITH ARRAYS
default_list=[1,2,3,"pet","money"]
default_tuple=(1,2,3,"pet","money")
default_string= "NEW TO THIS"
default_list.insert(3,4) #adds the integer 4 to index position 3
print(default_list)
print(default_tuple[4]) #get the 5th element in the tuple
print(default_string+" THING") #String Concatenation

##WORKING WITH SETS
default_set={1,2,3,4,4,5,3,2,5}
print(default_set)

## TYPE CASTING IN PYTHON

a= "200"
b=int(a)
print(type(a), type(b))