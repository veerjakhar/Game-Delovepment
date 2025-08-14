samplelist = [1, 1, 2, 2, 3, 3]
sampleset = set(samplelist)
print(sampleset)

if 2 in sampleset:
    print("yes")
else:
    print("no")

myset = set([])
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)
print(myset)


myset.discard(5)
print(myset)

# Set operations
#1 Union
# Union means addition of sets
a = {1,2,3,4,5}
b = {4,5,6,7,8}
aUb = {1,2,3,4,5,6,7,8}
print(a.union(b))
print(a|b)

#2 Intersection
# Intersection means common elements between 2 sets
aIb = {4,5}
print(a.intersection(b))
print(a&b)

#3 Diffrence
# Diffrance of a and b is the elements that exist in a but not in b
print(b-a)
print(a-b)

#4 Symmetric Diffrence
# Symmetric Diffrence is Unoin of sets minus intersection of sets
print(a.symmetric_difference(b))
print(a^b)