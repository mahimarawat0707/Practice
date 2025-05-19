#sets are mutable but it's element are immutable
collection = {1, 2, 2, 2, "hello", "world", "world", 4}

print(collection) #duplicate value are ignored
print(type(collection)) 
print(len(collection)) #total number of items

coll = set() #empty set syntax
print(coll)

#SET METHODS 
coll.add(1)
coll.add(2)
coll.add(1)
coll.remove(1)

print(coll)

print(collection.pop())
print(collection.pop())

set1 = {1, 2, 3, 5, 8}
set2 = {2, 3, 4, 6, 7}
print(set1.union(set2)) #combines both set value & return new
