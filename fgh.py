import csv as c
with open ("E:/aro/phyton experiment/File handling/Student.csv ","w") as f:
 e = c.writer(f)
 e.writerow(l)
 
l = []
a = int(input("Enter the range"))
for i in range(a):
    b=int(input("Enter the element "))
    l.append(b)

print("Element in the list :- ", l)
l.pop()
print("After pop:-",l)

l1= l[-1]
print("Peek vallue :-",l1)
