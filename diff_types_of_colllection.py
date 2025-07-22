mani_list = ["bareilly", "khatima", "pilibhit", "tanakpur"]
print(mani_list)
mani_list.append("delhi")
print(mani_list)
print(len(mani_list))
print(type(mani_list))
abbas_list = ["agra", "lucknow", "jhansi", "kanpur", "delhi", "meerut"]
if "tanakpur" in abbas_list:
    print("tanakpur is present in the list")
else:
    print("tanakpur is not present in the list")
abbas_list = list(abbas_list)
print(abbas_list)
print(abbas_list[2])
abbas_list[2]= "hyderabad"
print(abbas_list)
print(abbas_list[2])