import csv as c
with open ("E:/aro/phyton experiment/File handling/Student.csv ","w") as f:
 e = c.writer(f)
 e.writerow(["Roll no :", "Name :"])
 e.writerow(['32', "Panchajanya"])
 e.writerow(['16', "Animesh"])
