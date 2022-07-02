def ro():
    s=5
    firstfile =("E:/aro/phyton experiment/File handling/Alpha.txt","w")
    for a in range (s):
        name = input("Enter the no. of the student :- \t")
        firstfile.write(name)
        firstfile.write("\n")
    firstfile.close()
ro()
    
