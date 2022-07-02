import csv as a
with open ("E:/aro/phyton experiment/File handling/OPERATION DELTA.csv" ,'r')as f :
    reader=a.reader(f,delimiter = "\t")
    for  row in reader :
        print(row)
