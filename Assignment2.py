# Create an empty list called_list.
my_list = []
print(my_list)
# Append the following elements to_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print(my_list)
list2 = [50,60,70]
print(list2)
# Extend my_list with another list: [50, 60, 70].
my_list.extend(list2)

print("list after extend",my_list)
# Remove the last element from my_list.
del my_list[-1]
print('After deleting the last item', my_list)
# Sort my_list in ascending order.
my_list.sort()
print('After Sorting',my_list)
# Find and print the index of the value 30 in  my_list
index_30 = my_list.index(30)
print(index_30)
