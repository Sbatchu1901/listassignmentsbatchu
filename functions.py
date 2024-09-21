#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), int(item_price)

drink_list = []
for drink in drink_items :
    item_info = get_item_information(drink)
    drink_list.append(item_info)
print(f"drink_list: {drink_list}")

appetizer_list = []
for appetizer in appetizer_items :
    item_info = get_item_information(appetizer)
    appetizer_list.append(item_info)
print(f"appetizer_list: {appetizer_list}")

salad_list = []
for salad in salad_items :
    item_info = get_item_information(salad)
    salad_list.append(item_info)
print(f"salad_list: {salad_list}")

entree_list = []
for entree in entree_items :
    item_info = get_item_information(entree)
    entree_list.append(item_info)
print(f"entree_list: {entree_list}")

dessert_list = []
for dessert in dessert_items :
    item_info = get_item_information(dessert)
    dessert_list.append(item_info)
print(f"dessert_list: {dessert_list}")


