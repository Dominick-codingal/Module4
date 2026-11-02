print("=====part1:Creating store item and store count=====\n")

items = ["Pencil", "Eraser","notebook", "shapener", "glue"]
stock_count = [12, 0, 8,5, 3]

print(items)
print(stock_count)

print("\n=====part2: pairing Items with stock Count into a dictionary=====\n")
inventory = {item:count for item, count in zip(items, stock_count)}
print("Full Inventory:", inventory)

print("\n=====part3: Filter items that are still in stock=====\n")
in_stock_item = [item for item in items if inventory[item]>0]
print("items in stock: ", in_stock_item)
print()

print("\npart4: ask the shopper which item they want to buy and stop the function early if the item is out of stock")

chosen_item = input("\nwhich item do you want to buy?: ")

if chosen_item not in inventory or  inventory[chosen_item]== 0:
    print(chosen_item, "is out of stock! stopping the checker")
    exit()
    
# PART 5: Create prices and ask for a markup amount
prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price: "))

marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked Up Prices:", marked_up_prices)

# PART 8: Find the marked up price of the chosen item
item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("Price of", chosen_item, "after markup:", chosen_price)

# PART 9: Reduce the stock count after the purchase
inventory[chosen_item] = inventory[chosen_item] - 1
print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])


