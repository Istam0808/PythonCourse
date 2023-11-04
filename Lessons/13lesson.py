# my_set = {"apple", "banana", "cherry"}
# my_set = ["apple", "banana", "cherry", "cherry", "cherry"]
# print(set(my_set))
# {'banana', 'apple', 'cherry'}

# or use the set function and create from an iterable, e.g. list, tuple, string
# my_set_2 = set(["one", "two", "three"])
# my_set_2 = set(("one", "two", "three"))
# print(my_set_2)
# {'three', 'one', 'two'}

# my_set_3 = set("aaabbbcccdddeeeeeffff")
# print(my_set_3)
# {'b', 'c', 'd', 'e', 'f', 'a'}

# # careful: an empty set cannot be created with {}, 
# as this is interpreted as dict
# # use set() instead
# a = {}
# print(type(a))
# # <class 'dict'>
# a = set()
# print(type(a))
# # <class 'set'>
# # -----------------------------------------------------------------------------------
# # NOTES  -----------------------------------------------------

# test_set = {1, 2, 3, 4, 5}
# Don't allow duplications
# Doesn't have order, index, keys, values, items, slices, etc...


# test_set = {1, True, False, 0}
# print(set(test_set))
# 1 and True are the same and 0 and False are the same
# 1 == True  =>  True
# 0 == False  =>  True
# 1 is True  =>  False
# 0 is False  =>  False


# -----------------------------------------------------------------------------------
# ACCESSING ITEMS --------------------------------------------
# loop   ||    ... in ...
# x = {1, 2, 3, 4, 5}
# for n in x:
#     if ... in x:
#         pass
#     print(n)

# -----------------------------------------------------------------------------------
# ADDING -----------------------------------------------------

# add()                  Adds an element to the set
#   EX: x.add(4)  => changes the original set
# l = {1, 2, 3}
# l.add(1) # NOTHING IS ADDED
# l.add(4)

# update()              Updates the set with the union of this set and others
# EX: x.update([4, 5, 6])  => changes the original set
# l = {1, 2, 3}
# l.update([3, 2, 4, 5, 6])
# print(l)


# # -----------------------------------------------------------------------------------
# # Union and Intersection

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# union(): combine elements from both sets, no duplication
# note that this does not change the two sets
# u = odds.union(evens)
# u = odds | evens
# print(u)
# EX:
# a = x.union(y)  # =>  x | y

# # intersection(): take elements that are in both sets
# # return a new set, that only contains the items that are present in both sets.
# i = odds.intersection(evens)  # =>  x & y
# print("intersection 1: ", i)  # =>  {}
# # EX: x.intersection(y) #  =>  x & y

# i = odds.intersection(primes)  # => {3, 5, 7}
# print("intersection 2: ", i)

# i = evens.intersection(primes)  # => {2}
# print("intersection 3: ", i)


# # -----------------------------------------------------------------------------------
# # DIFFERENCE of sets
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3,                  10, 11, 12}

# # difference() : returns a set with all the elements from the setA that are not in setB or in C,D... .
# # x.difference(y)     =>  x - y
# # x.difference(y, z)  =>  x - y - z

# diff_set = setA.difference(setB, {8, 9})
# print("difference 1: ", diff_set)

# # A.difference(B) is not the same as B.difference(A)
# diff_set = setB.difference(setA)
# print("difference 2: ", diff_set)

# # symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
# diff_set = setA.symmetric_difference(setB)
# print("difference 3: ", diff_set)

# # A.symmetric_difference(B) = B.symmetric_difference(A)
# diff_set = setB.symmetric_difference(setA)
# print("difference 4: ", diff_set)

# # -----------------------------------------------------------------------------------
# # DELETE

# remove(x): removes x, raises a KeyError if element is not present
my_set = {"apple", "banana", "cherry"}
# my_set.remove("apple")
# print(my_set)

# # KeyError:
# # my_set.remove("orange")

# # discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)



# # clear() : remove all elements
# my_set.clear()
# print(my_set)

# # pop() : return and remove a random element
# a = {True, False, 2, "hi", "hello"}
# result = a.pop()
# print(result)
# print(a)

# # -----------------------------------------------------------------------------------
# # Check if element is in Set
# my_set = {"apple", "banana", "cherry"}
# if "apple" in my_set:
#     print("yes")


# # -----------------------------------------------------------------------------------
# # UPDATE sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3,                    10, 11, 12}

# # update() : Update the set by adding elements from another set.
# setA.update(setB)
# print("Set update", setA)

# Keep ONLY the Duplicates
# intersection_update() : Update the set by keeping only 
# the elements found in both
# setA.intersection_update(setB)
# print("Set intersection_update", setA)

# # difference_update() : Update the set by removing elements found in another set.
# setA.difference_update(setB)
# print("Set difference_update", setA)

# # symmetric_difference_update():  Keeps only the elements that 
# are NOT present in both sets.
# # Keep All, But NOT the Duplicates.
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setA.symmetric_difference_update(setB)
# print("Set symmetric_difference_update", setA)

# Note: all update methods also work with other 
# iterables as argument, e.g lists, tuples
# setA.update([1, 2, 3, 4, 5, 6])

# # -----------------------------------------------------------------------------------
# # Copying ---------------------------------------------------------------------------
# set_org = {1, 2, 3, 4, 5}

# # this just copies the reference to the set, so be careful
# set_copy = set_org

# # now modifying the copy also affects the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)

# # use copy() to actually copy the set
# set_org = {1, 2, 3, 4, 5}
# set_copy = set_org.copy()

# # now modifying the copy does not affect the original
# set_copy.update([3, 4, 5, 6, 7])
# print(set_copy)
# print(set_org)


# # -----------------------------------------------------------------------------------
# super => always parent
# sub   => always child

# # Subset, Superset, and Disjoint ----------------------------------------------------
# setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# # issubset(setX): Returns True if setX contains the set
# print(setA.issubset(setB))
# print(setB.issubset(setA))  # True

# # issuperset(setX): Returns True if the set contains setX
# print(setA.issuperset(setB))  # True
# print(setB.issuperset(setA))

# # isdisjoint(setX) : Return True if both sets have a 
# null intersection, i.e. no same elements
# setC = {7, 8, 9}
# print(setA.isdisjoint(setB))
# print(setB.isdisjoint(setA))
# print(setA.isdisjoint(setC))
# # -----------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # FROZENSET
# Frozen set is just an immutable version of normal set.
# While elements of a set can be modified at any time, elements of frozen set
# remains the same after creation. Creation with: my_frozenset = frozenset(iterable)

# a = frozenset([0, 1, 2, 3, 4])

# The following is NOT allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()
# a.update([1,2,3])


# Other set operations work
# odds = frozenset({1, 3, 5, 7, 9})
# evens = frozenset({0, 2, 4, 6, 8})
# print(odds.union(evens))
# print(odds.intersection(evens))
# print(odds.difference(evens))
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# frozenset()
# frozenset({1, 3, 5, 7, 9})

# In order to change the SET
# we can change its type to a normal set or another sequence type
# odds = frozenset({1, 3, 5, 7, 9})
# changed_fz_set = list(odds)
# print(changed_fz_set)
