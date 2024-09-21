#user interface to the main menu
import data
import functions
def show_main_menu():
  while True:
    print("Srujan")
    print("_______________________")
    print("N for a new order")
    print("X for close orders and prepare the check")
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Q':
      break
    elif user_menu_choice in 'X':
      close_order()
    elif user_menu_choice in 'N':
      print('\nNew Order')
      make_order(user_menu_choice.upper())
    else:
      print("Please enter the correct choice")

def make_order(menu_choice):
    while True:
        menu_choice = input("Please enter your choice D(drinks)/A(appetizer)/S(salads)/E(entree)/T(desserts)/C(for changing the order): ").upper()
        if menu_choice == 'D':
            print(drink_list)
            item = input("Enter ['D1', 'D2', 'D3', 'D4']: ").upper()
            drinks.append(get_item_information(item))
        elif menu_choice == 'A':
            print(appetizer_list)
            item = input("Enter ['A1', 'A2', 'A3', 'A4', 'A5']: ").upper()
            appetizers.append(get_item_information(item))
        elif menu_choice == 'S':
            print(salad_list)
            item = input("Enter ['S1', 'S2', 'S3']: ").upper()
            salads.append(get_item_information(item))
        elif menu_choice == 'E':
            print(entree_list)
            item = input("Enter ['E1', 'E2', 'E3', 'E4']: ").upper()
            entrees.append(get_item_information(item))
        elif menu_choice == 'T':
            print(dessert_list)
            item = input("Enter ['T1', 'T2', 'T3', 'T4']: ").upper()
            dessert.append(get_item_information(item))
        elif menu_choice == 'C':
          current_order()
          category = input("Which category do you want to change? D(drinks)/A(appetizers)/S(salads)/E(entrees)/T(desserts): ").upper()
          old_item = input("Enter the name of the item you want to replace (e.g., SODA): ").upper()
          new_item = input("Enter the code of the new item to replace it (e.g., 'D4' for WATER): ").upper()
          if category == 'D':
                change_order(drinks, old_item, new_item)
          elif category == 'A':
                change_order(appetizers, old_item, new_item)
          elif category == 'S':
                change_order(salads,  old_item, new_item)
          elif category == 'E':
                change_order(entrees,  old_item, new_item)
          elif category == 'T':
                change_order(dessert,  old_item, new_item)
        else:
            break

        add_choice = input("Add another item to list? (y/n): ").lower()
        if add_choice != 'y':
          break

def close_order():
    tax_rate = 0.08 #assuming
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("\nCheck:\n")
    order_list = drinks + appetizers + salads + entrees + dessert

    drinks_total = calculate_total(drinks)
    appetizer_total = calculate_total(appetizers)
    salad_total = calculate_total(salads)
    entree_total = calculate_total(entrees)
    dessert_total = calculate_total(dessert)

    subtotal = drinks_total + appetizer_total + salad_total + entree_total + dessert_total
    tax = subtotal * tax_rate
    total_price = subtotal + tax

    # Display ordered items
    print("Drinks:")
    for item in drinks:
        print(f"{item[0]}  ${item[1]}")
    print("Appetizers:")
    for item in appetizers:
        print(f"{item[0]}  ${item[1]}")
    print("Salads:")
    for item in salads:
        print(f"{item[0]}  ${item[1]}")
    print("Entrees:")
    for item in entrees:
        print(f"{item[0]}  ${item[1]}")
    print("Desserts:")
    for item in dessert:
        print(f"{item[0]}  ${item[1]}")

    print(f"Items Total: ${subtotal:.2f}")
    print(f"Taxes: ${tax:.2f}")
    print(f"Total: ${total_price:.2f}")
    print("++++++++++++++++++++++++++++++++++++++++++++")

def calculate_total(order_list):
    """Calculate the total price for all items in the order."""
    total_price = 0
    for item in order_list:
        total_price += item[1]
    return total_price

def current_order():
    print("Current Order:")
    print("Drinks:", drinks)
    print("Appetizers:", appetizers)
    print("Salads:", salads)
    print("Entrees:", entrees)
    print("Desserts:", dessert)

def change_order(order_list, old_item_name, new_item_code):

    new_item = get_item_information(new_item_code)
    #print(order_list)
    if new_item:
        for i, item in enumerate(order_list):
            if item[0].upper() == old_item_name.upper():
                order_list[i] = new_item
                print(f"Replaced {old_item_name} with {new_item[0]}")
                return True
        print(f"{old_item_name} not found in the order.")
        return False
    else:
        print(f"New item code {new_item_code} not found.")
        return False

if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    order_list = []
    show_main_menu()