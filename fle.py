firstfle  = open("E:/aro/rrq.txt","a") 

s=input("Enter the string to write in file ")
firstfle  = open("E:/aro/rrq.txt","a") 
firstfle.write ("Hello gyus ths is my first file using phython")
firstfle.write("\n")
firstfle.write(s)
firstfle.close()

firstfle  = open("E:/aro/rrq.txt","r")
print(firstfle.read())  #display whole file
print(firstfle.read(30))    #display limided line of file according to no . given
print(firstfle.read())  #display single line of file
print(firstfle.readlines())     #display in list form

s= 5
firstfle  = open("E:/aro/rrq.txt","w")
for a in range (s):
    name = input("Enter the no. of the student :- \t")
    firstfle.write(name)
    firstfle.write("\n")
firstfle.close()    
