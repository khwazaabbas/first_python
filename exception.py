#try:
#    print(x)
#except NameError:
#    print("varible x is not defined")
#except:
#    print("something else went wrong")
#try:
#    print(x)
#except:
#    print("x is not defined")
#else:
#    print("pakistan")
#finally:
#    print("try exception is finished")
#x = input("enter input : ")
#print(x)
#if not type(x) is int:
#  raise TypeError("Only integers are allowed")

'''
a = input("enter a integer :")
print(f"multipication table of {a} is :")
try:
    for i in range(1, 21):
      print(f"{int(a)} * {i} = {int(a)*i}")
except:
    print("invalid input")

    print("try exception is over")
    print("end of the programme")
    '''


'''
def fun1():
    try:
        l =[12, 45, 65, 34, 98, 23, 67, 34, 98, 34]
        i = int(input("enter an integer value  :  "))
        print(l[i])
        return 1
    except:
        print("invalid input")
        return 0
    finally:
        print("finally block always executed")
x = fun1()
print(x)
def fun2():
    try:
        l = ["mani", "khwaza", "abbas", "ansari", "tanakpur", "champawat", "uttrakhand"]
        i = str(input("enter a valid string value  :  "))
        print(l.index(i))
        return 1
    except:
        print("invalid input (takes string value only & inter value in range)")
        return 0
    finally:
        print("finally block always executed")

y = fun2()
print(y)
'''

'''
a = str(input("enter and integer value between 0 and 100  :  "))
def fun3():
  if a == "abbas":
    print("this name is accepted")
  elif (int(a)<0 or int(a)>100):
    raise Exception("invalid input (enter an integar value between 0 and 100)")
    print(" have a nice day ")
    print(a)
b = fun3()
print(b)

'''

