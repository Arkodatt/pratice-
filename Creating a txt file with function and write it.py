def firstfile ():
    f= open("E:/aro/phyton experiment/File handling/Arko.txt","a")
    s= input("Enter the string write in file :-")
    f.write("\n")
    f.write(s)
    f.close()
firstfile()
