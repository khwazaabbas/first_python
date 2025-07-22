
with open("demofile.txt", "r") as demo:
  contnet = demo.read()
  print(contnet)
print("------------------------------------------")


demofile = open("demofile.txt")
read_content = demofile.read()
print(read_content)
demofile.close()
print("------------------------------------------")


demofile2 = open("demofile2.txt", "w")
demofile2.write("khwaza abbas\n")
demofile2.write("mani\n")
print("------------------------------------------")


demofile2 = open("demofile2.txt")
read_content2 = demofile2.read()
print(read_content2)
demofile2.close()
print("------------------------------------------")

demofile3 = open("demofile3.txt")
read_content3 = demofile3.read()
print(read_content3)
demofile3.close()
print("------------------------------------------")


f = open("demofile3.txt", "r")
for x in f:
  print(x)

print("------------------------------------------")

m = open("demofile2.txt", "a")
m.write("add more text content in a file")
m.close()

m = open("demofile2.txt")
read_content4 = m.read()
print(read_content4)

print("------------------------------------------")



n = open("demofile4.txt", "x")
n.close()


n = open("demofile4.txt", "a")
n.write("this is a new file crete throuh the vs code \n")
n.write("this is a new file crete throuh the vs code")
n.close()

demofile4 = open("demofile4.txt")
read_content5 = demofile4.read()
print(read_content5)


import os
if os.path.exists("demofile4.txt"):
   os.remove("demofile4.txt")
   print("the file is deleted")
else:
   print("the file dosen't exists")
   
   

import os
os.rmdir("mani")