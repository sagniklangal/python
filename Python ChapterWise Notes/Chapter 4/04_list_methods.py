l1 = [1,8,7,2,21,15]
#Right
# print(l1.sort()) # sort() can't be used inside print
l1.sort() # Sorts the list
print(l1)

#Wrong, See chapter 3 letter program
# l1_sorted = l1.sort()
# print(l1_sorted)

l1.reverse()    # Reverse the list
print(l1)
l1.append(45)   # Appends 45 at the end
print(l1)
l1.insert(0,54) # inserts 54 at 0th index
print(l1)

#Removing from list
l1.pop(-5)
print(l1)
l1.remove(45)
print(l1)
