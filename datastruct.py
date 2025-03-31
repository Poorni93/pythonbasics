#list
lists = [1,2,3,4,5,6,"hp",33.33,True]
#ordered,mutable
lists.append(29)
lists.insert(4,False)
lists.remove(4)
print(lists,type(lists))
#typle
ty = (10,9,8,7,"poorni","charu","hari")
#ordered,immutable
#this index function we need to provide value it gives the index
print(ty,type(ty),ty.index("charu"))
#sets
sets = {}
print(sets,type(sets))
#empty sets type is dictionary
setss = {2,2,5,6,7,33,33,"poorni","poorni"}
print(setss)
#its unordered ,duplicate value is not allow
setss.add(29)
setss.add("charu")
print(setss)
"""union insertion in sets"""
set1 = {1,2,3,4}
set2 = {4,5,6,7,8,9,9}
print(set1.union(set2))
print(set1.intersection(set2))
"""try in string"""
set3 = {"hai","hardik","kabil","virat","dhoni"}
set4 = {"hardik","poorni","charu","hari"}
print(set3.union(set4))
print(set3.intersection(set4))

#dictionary
dic = {1:"laddu",2:"kesari",3:"alwa"}

print(dic,type(dic),dic[3])