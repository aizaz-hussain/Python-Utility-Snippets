import json_editor as jsn

# Use . as delimiter between paths
# You can change the path delimiter in json_editor.py @pathDelimiter
# Function get_value() returns value of the path
# Use function update_json() to update values on the provided path

jsn.update_json('parent1', 1)
jsn.update_json('parent2.child1', 1)
jsn.update_json('parent2.child2.subchild1', 1)


print('parent2.child2.subchild1: ', jsn.get_value('parent2.child2.subchild1'))