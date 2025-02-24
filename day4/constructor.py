#constructor
fruits=list(("Apple","berry","Cherry","dfdf","dfdsfe","Avacado"))
ice=list(("gg","hhtht"))
print(fruits)
print(fruits[1])
print(fruits[-1]) #negative indexing
print(fruits[2:4]) #range of list need to be printed
print(fruits[1:])
print(fruits[:1])
if "berry" in fruits:
    print("true")
print("berry" in fruits)
fruits.append("sasasas") #to append into list
print(fruits)
fruits[3]="watermelon" #replacing by over writing process
print(fruits)
fruits[4:5]="Blue berry","Choco" #if u need to change for some series of list elements u can do by range
print(fruits)
print(fruits.count("Apple")) #to know how many elements
fruits.insert(7,"Pine apple")
print(fruits)
fruits.insert(9,"rgttg")
print(fruits)
#in one list 2 lists
fruits.extend(ice)
print(fruits)
list1=[1,4,6]
ice.remove("gg")
print(ice)
ice.extend(list1) # check once tuple list relation
print(ice)





