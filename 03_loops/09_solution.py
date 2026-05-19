# items = ["apple", "banana", "orange", "apple", "mango"]
# for item in items:
#     if items.count(item) > 1:
#         print("duplicate item found", item)
#         break
#     else:
#         print("no duplicate fruit found")


#  second approach
items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = set()
print(unique_items)
for item in items:
    if item in unique_items:
        print("duplicate item found", item)
        break
    else:
        unique_items.add(item)