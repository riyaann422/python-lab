first_name=input("Enter the first name:")
last_name=input("Enter your last name:")
name=first_name+" "+last_name
print (name)
first_name_len=len(first_name)
print(first_name_len)
extracted_last_name=name[first_name_len+1:]
print(extracted_last_name)

