'''

mani_list = [ "tanakpur", "banbasa", "agra", "bly", "tnk", "chpt", "hyd", "delhi", "hld"]
abbas_list = []
khwaza_list = []
etc_list = []
for x in mani_list:
    if "a" in x:
        abbas_list.append(x)
    elif "d" in x:
        khwaza_list.append(x)
    else :
        etc_list.append(x)

print(mani_list)
print(abbas_list)
print(khwaza_list)
print(etc_list)


'''


thislist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
manilist = thislist.copy()
print(manilist)

print("............................................................................")

pri_list = ["sab", "ko", "sab", "nahi", "milta"]
sec_list = list(pri_list)
print(sec_list)

print("............................................................................")

x = ["tanakpur", "bareilly", "agra", "delhi", "haldwani"]
y = x[:]
print(y)

print("............................................................................")

list1 = ["khwaza", "abbas", "ansari"]
list2 = ["tanakpur", "khatima", "pilibhit"]
list3 = list1 + list2
print(list3)

print("............................................................................")


list3 = ["nepal", "china", "russia", "england"]
list4 = ["america", "canada", "germany"]
for x in list4:
    list3.append(x)

print(list3)

print("............................................................................")


list5 = ["tanakpur", "champawat", "ramnagar", "srinagar"]
list6 = ["rudrapur", "delhi", "jhansi"]
list5.extend(list6)
print(list5)


print("............................................................................")

