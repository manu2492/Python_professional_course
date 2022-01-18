#union
set1 = {3, 4, 5}
set2 = {6, 7, 8}

set3 = set1 | set2
print(set3)


#intersection
#returns only elements in common 
set3 = {3, 4, 5}
set4 = {5, 6, 7}

set5 = set3 & set4
print(set5)


#subtraction
#return items that are not in set7
set6 = {3, 4, 5}
set7 = {5, 6, 7}

set8 = set6 - set7
print(set8)


#simetric difference
#returns elements that do not have in common
set9 = {3, 4, 5}
set10 = {5, 6, 7}

set11 = set9 ^ set10
print(set11)#return {3, 4, 6, 7}

















