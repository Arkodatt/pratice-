def myfunc3( mylist):
    print( "\t Inside CALLED Function now ")
    print("\t List recived :" , mylist )
    mylist.append(2)
    mylist.extend([5,1])
    print("\t list after adding some elements :" , mylist)
    mylist.remove(5)
    return
List1 = [4]
print("Lst before function call:" , List1 )
myfunc3(List1)
print("\t List after function call :" , List1)
      
