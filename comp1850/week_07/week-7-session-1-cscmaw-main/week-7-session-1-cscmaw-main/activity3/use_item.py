# write code to import the item module



# write code to create an instance of IventoryItem with values such as
# name = "Laptop", sku = "LAP24", quantity=12, price_per_unit = 750.99

# write code to display the item details


# write code to add stock by calling the add_stock method, e.g., to add 25 items


# write code to remove stock by calling the remove_stock method, e.g., to remove 8 items
import item
inventory_item = item.InventoryItem(name="Laptop", sku="LAP24", quantity=12, price_per_unit=750.99)
inventory_item.display_item_details()
inventory_item.add_stock(25)
inventory_item.remove_stock(8)