import time


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    def contains(self, this_guy):
        if self.value == this_guy:
            return True
        if this_guy > self.value:
            if not self.right:
                return False
            else:
                self.right.contains(this_guy)
        else:
            if not self.left:
                return False
            else:
                self.left.contains(this_guy)
    

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements


# Will need to implement a binary tree to make the names search go faster...
# Just put name_2 into a binary tree, and do the same logic as below

names_2_tree_version = BinarySearchTree(names_2[0])
for each_name in names_2:
    for i in (1, len(names_2)):
        names_2_tree_version.insert(each_name)

for this_name in names_1:
    if names_2_tree_version.contains(this_name):
        duplicates.append(this_name)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
