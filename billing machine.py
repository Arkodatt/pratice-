GST=0.12

# Rates of foods

Rate={"Roti" : 5,"Rice_bowl" : 20,"Dal_bowl" : 10,"Mixed_vegitable" : 20, "Paneer_bowl" : 30, "Chicken_bowl" : 50}

print("Restaurant Bill")
print("Enter Quantity")

# Quantity
Roti=int(input("Roti : "))
Rice_bowl=int(input("Rice bowl : "))
Dal_bowl=int(input("Dal bowl : "))
Mixed_vegitable=int(input("Mixed vegitable : "))
Paneer_bowl=int(input("Paneer bowl : "))
Chicken_bowl=int(input("Chicken bowl : "))

# Calculating Formula
cost=Roti*Rate["Roti"]+Rice_bowl*Rate["Rice_bowl"]+Dal_bowl*Rate["Dal_bowl"]+Mixed_vegitable*Rate["Mixed_vegitable"]+Paneer_bowl*Rate["Paneer_bowl"]+Chicken_bowl*Rate["Chicken_bowl"]
Bill = cost+cost*GST
print("Pay Rs. %f" % Bill)
print("Thanking You :)")
