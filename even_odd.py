list1 = [34,25,12,2,56,7,6]
list2 = [98,76,45,34,12]
print("list1",list1)
print("list2",list2)
combined_list = list1+list2
print("combined_list",combined_list)
even_list = []
odd_list = []
for i in combined_list:
    if i%2==0:

        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list = even_list + odd_list
print("merged_list",merged_list)

