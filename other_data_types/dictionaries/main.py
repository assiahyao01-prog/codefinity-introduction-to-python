Dairy={"Milk":13, "Egg":16}
Bakery={"Bread":17}
Produce={"Apples": 141}
grocery_inventory= (Dairy, Bakery,Produce)
bread_details=Bakery["Bread"]
Bakery.update({"Cookies": 143})
print("Inventory after adding Cookies: ", grocery_inventory )
Dairy.pop("Egg")
print("Detail of Bread: ", bread_details)
print("Inventory after removing egg: ", grocery_inventory )
