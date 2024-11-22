'''Author:Riya ann mathew
Description:input two list from the user .merge these lists into a third list such as that in the merged list all even numbers occur
first followed by odd numbers .both the even numbers and odd numbers should be in sorted order'''
list1 =[34,25,12,35,8,9]
list2 =[22,67,89,2,4,11,]
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i %2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
print("Even numbers",even_list)
odd_list.sort()
print("odd numbers:",odd_list)
print("final list")
merged_list=even_list+odd_list
print(merged_list)

