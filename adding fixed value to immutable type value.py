def myfuncl(a):
    print(" \t Inside myfuncl()")
    print("\t Value recived in  'a' as " , a )
    a = a+2
    print("\t Value of 'a' is now changes to " , a)

# main
num = 3
print(" calling myfuncl () by passing 'num' with value " ,num )
myfuncl(num)
print (" back from myfuncl(). Value of 'num' is " , num )
