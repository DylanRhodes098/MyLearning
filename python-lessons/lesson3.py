needed = ["milk", "bread", "eggs", "apples"]
item = input("add an item: ")
itemLower = item.lower()
if itemLower in needed:
    print(f"you still need to buy {item}")
else:
    print (f"{item} is not on your list")


