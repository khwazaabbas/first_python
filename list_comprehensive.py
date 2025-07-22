oldlist = ["bareilly", "khatima", "tanakput", "pilibhit", "chakarpur", "majhola"]
newlist = []
for x in oldlist:
    if "b" in x:
        newlist.append(x)

print(newlist)
print("...............................................................................................")

oldlist2 = ["bareilly", "khatima", "tanakput", "pilibhit", "chakarpur", "majhola"]
newlist2 = [x for x in oldlist2 if "a" in x]
print(newlist2)
print("...............................................................................................")

oldlist3 = ["india", "pakistan", "nepal", "bhutan", "srilanka", "maldives"]
newlist3 = [x for x in oldlist3 if x != "nepal"]
newlist4 = [x for x in oldlist3 if x != "srilanka"]
print(newlist3)
print(newlist4)
print("...............................................................................................")

oldlist4 = ["mani", "aman", "jonti", "jumbo", "shakib", "salmaan"]
newlist5 = [x for x in oldlist4]
print(newlist5)
newlist8 = [x.upper() for x in oldlist4]
print(newlist8)
print("...............................................................................................")

newlist6 = [ x for x in range(20) ] # iterable without any condition
print(newlist6)
newlist7 = [ x for x in range(20) if x < 10]
print(newlist7)
print("...............................................................................................")

oldlist5 = [ "mani", "aman", "jonti", "jumbo", "shakib", "salmaan"]
newlist9 = ['mani' for x in oldlist5]
print(newlist9)
print("...............................................................................................")

