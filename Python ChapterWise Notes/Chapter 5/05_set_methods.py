emp = set()

# Add elements into set
emp.add(1)
emp.add(2)
emp.add(1)
emp.add(2) # Will add only {1,2}, as set is non repetitive
emp.add(4)
emp.add(5)
emp.add(6)
emp.add(7)

print(emp)

# # Dictionary and lists can't be added into set as they are unhashable(values of those two can be changed)
# emp.add([4,5,6])
# emp.add({1:2})
# print(emp)

# emp.add((4,5,6)) #But tuple can be added into set as it's hashable(values of tuple two can not be changed)
# print(emp)

print(len(emp)) # Prints the length of the set
emp.remove(1) # Removes 1 from the set
print(emp)

emp.pop() # Here pop() removes 2 from the set
print(emp)

print(emp.pop()) # Here print(emp.pop()) removes 4 and prints the removed elemnt(which is 4)
print(emp)

emp.clear() # Empties the set
print("After using clear() method: ", emp)

# Union and intersection
s1 = {2,3,4,5}
s2 = {3,4,5,6}
print("After using s1&s2 or intersection: ", s1 & s2)
print("After using s1|s2 or union: ", s1 | s2)

#Using union() and intersection() method
union_set = s1.union(s2)
print(union_set)
union_set_1 = s2.union(s1)
print(union_set_1)

intersection_set = s1.intersection(s2)
print(intersection_set)
intersection_set_1 = s2.intersection(s1)
print(intersection_set_1)


