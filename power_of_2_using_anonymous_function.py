

terms = int(input("How many terms you want to display?  :   "))
result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])




#terms = int(input("enter the number  :  "))
l=list(map(int,input("enter the number  :  ").split(" ")))
#result = list(map(lambda x: 2 ** x, range(terms)))
result = list(map(lambda x: 2 ** x, l))
print(result)






li = list(map(float,input(" enter the number  :  ").split(" ")))
result = list(map(lambda x: 2 ** x, li))
print(result)