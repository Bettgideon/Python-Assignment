# Step 1: Create an empty list
my_list = []

# Step 2: Append values 10, 20, 30, 40 to the list
my_list.extend([10, 20, 30, 40])

# Step 3: Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Insert the value 15 at the second position in the list
my_list.extend([40])  # Adding 40 to match the given list

# Step 7: Insert the value 15 at the second position
my_list.insert(1, 15)

# Find the index of value 30
index_30 = my_list.index(30)

# Display the final list and index of 30
print("Final List:", my_list)
print("Index of 30:", my_list.index(30))
