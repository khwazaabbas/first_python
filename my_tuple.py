my_tuple1 = ("tanakpur", "banbasa", "chakarpur", "khatima", "majhola", "niyoriya", "pilibhit", "shahi", "bijoriya", "sethal", "bhojipura", "dohna", "izzatnagar", "city", "bareilly")
print(my_tuple1[2:7])
print(my_tuple1[ :7])
print(my_tuple1[7: ])
print(my_tuple1[-12: -3]) # negative indexing


print("............................................................................")


my_tuple2 = ("tanakpur", "banbasa", "chakarpur", "khatima", "majhola", "niyoriya", "pilibhit", "shahi", "bijoriya", "sethal", "bhojipura", "dohna", "izzatnagar", "city", "bareilly")
if "bareilly" in my_tuple2:  # check if the item exists
    print("yes, 'bareilly' is in the tuple")



print("...............................................................................................")



my_tuple3 = ("tanakpur", "banbasa", "chakarpur", "khatima", "majhola", "niyoriya", "pilibhit", "shahi", "bijoriya", "sethal", "bhojipura", "dohna", "izzatnagar", "city", "bareilly")
item_to_check = input("enter the name of the place to check  :  ").strip().lower()
if item_to_check in ( place.lower() for place in my_tuple3):
    print("yes", item_to_check, "is in the tuple")
else:
    print("no", item_to_check, "is not in the tuple")