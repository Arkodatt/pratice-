#program add.py to add two numbers throuh a function
def calcsum ( x,y):
    s = x+y
    return s
num1 = float(input( " ENTER A 1 ST NUMBER: "))
num2 = float(input( " ENTER A 2 nd NUMBER: "))
sum = calcsum ( num1 , num2 )
print ( "Sum of two given number is :" , sum )
