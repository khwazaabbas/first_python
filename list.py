thislist = ["mango", "banana", "grapes", "pomegranate", "mango", "litchi", "orange", "guava", "litchi"]
thislist2 = [1, 2, 4, 76, 34, 87, 45, 34, 98]
thislist3 = [True, False, True, True, False]
thislist4 = ["mani", 23.43, True, 87, 'mango']
thislist5 = list(("tanakpur", "banbasa", "khatima", "bareilly")) # list() constructor
print(thislist)
print(len(thislist))
print(thislist2)
print(thislist3)
print(thislist4)
print(type(thislist))
print(type(thislist4))
print(thislist5)
print(thislist[3]) # lists are indexed, accessing by the index number
print(thislist[-1]) # negative indexing
print(thislist[2:6]) # range of indexing.... note second (2) member included but (6) sixed member are not included, it a nature of list indexing
print(thislist[:6]) # anothern way of accessing members using through indexing
print(thislist[4:]) # it is also another type of accessing members using through the indexing
print(thislist[-4:-1]) # range of negative indexing


vegilist = ["potato", "tomato", "chilli", "ginger", "garlic"]
if "ginger" in vegilist:# check if item exists
    print("yes, ginger in the above list")

thislist[0] = "papaya" # chnge the item value in place of apple change the papaya
print(thislist)
thislist[1:5] = ["blackcurrent", "chiku"]# change the range of item values
print(thislist)

thislist.insert(2, "kafal") # insert item using through the insert() method
print(thislist)

thislist.append("dragon-fruit") # append() method provide the functionality to add the item end of the list
print(thislist)

newlist = ["ramnagar", "kashipur", "moradabad", "pantnagar"]
print(newlist)
newlist2 = ["haldwani", "nainital", "almora", "ranikhet"]
newlist.extend(newlist2) # merging through the extend() method
print(newlist)

ltstlist = ["bottle", "cup", "mug", "glass"]
ltsttuple = ("pencil", "rubber", "scale", "razer", "pen", "colour")
ltstlist.extend(ltsttuple) # merging the 2 differnd type of items list or tuple using through the extend() method
print(ltstlist)

ltstlist2 = ["india", "china", "nepal", "pakistan", "iran"]
ltstlist2.remove("nepal") # remove specified iten using through the remove() method
print(ltstlist2)

ltstlist3 = ["india", "china", "nepal", "pakistan", "iran"]
ltstlist3.pop(1) # remove specified index using through the pop() method'
ltstlist3.pop() # if you not specified the number of the index in this case pop() method removes the last element item in the list
del ltstlist3[0] # del also remove the specified list item using through the index position
print(ltstlist3)
del thislist3 # del keyward also delte the complete the list
#print(thislist3) # this will cause an error because already deleted the thislist3

ltstlist4 = ["one", "two", "three", "four", "five", "six"]
ltstlist4.clear() # the clear () method empties the entire list, the list still remains but it has no content
print(ltstlist4)

thislist6 = ["mango", "banana", "grapes", "pomegranate", "mango", "litchi", "orange", "guava", "litchi"]
for x in thislist6:# we can loop through the list items by using a for loop
    print(x)

print("..............................................................................................................................")

thislist7 = ["mango", "banana", "grapes", "pomegranate", "mango", "litchi", "orange", "guava", "litchi"]
for i in range(len(thislist7)):
    print(thislist7[i])

print("..............................................................................................................................")

thislist8 = ["levis", "wrangler", "lee", "puma", "adidas","nike", "bata", "sparx", "signature-levis", "monticarlo"]
i = 0
while i < len(thislist8):
    print(thislist8[i])
    i = i + 1
print("..............................................................................................................................") 

thsilist9 = ["apple", "samsung", "nokia", "vivo", "oppo", "realme", "oneplus", "redmi", "poco"]
[print(x) for x in thislist] # looping using list comprehension
print("..............................................................................................................................")

