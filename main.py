# Build a billing system at check out counter - customer has items in his cart and wants to pay the bill
from collections import defaultdict

class Store:

  def __init__(self):
    self.inventory = defaultdict(dict)

  def add_item(self, item, price, quantity):
    self.inventory[item]['price'] = int(price) 
    self.inventory[item]['quantity'] = int(quantity)

  def update_price(self, item, price):
    self.inventory[item]['price'] = int(price)

  def update_quantity(self, item, quantity):
    self.inventory[item]['quantity'] = int(quantity)

  def get_quantity(self, item):
    quantity = self.inventory[item]['quantity']
    return quantity
  
  def get_price(self, item):
    price = self.inventory[item]['price']
    return price

  def print_inventory(self):
    print("store inventory: ")
    for item in self.inventory:
      print(item, self.inventory[item])
    print()


class Purchase:

  def __init__(self):
    self.cart = defaultdict()

  def add_cart(self, items):
    for item in items:
      self.cart[item]=items[item]
   
  def print_cart(self):
    print("items in the cart: ")
    for item in self.cart:
      print(item, self.cart[item])
    print()


  def checkout(self, store):

    finalBill = 0
    self.print_cart

    for item in self.cart:

      quantity_purchased = customer.cart[item]
      price = store.get_price(item)

      finalBill += price * quantity_purchased

      #update quantity in the store inventory
      quantity_in_store = store.get_quantity(item)
      quantity_change = quantity_in_store - quantity_purchased

      store.update_quantity(item, quantity_change)

    store.print_inventory()

    return finalBill

#create store inventory
store = Store()
store.add_item("juice", 3, 200)
store.add_item("milk", 4, 200)
store.print_inventory()

#customer makes a purchase
customer = Purchase()
items={'juice': 2, 'milk': 4}
customer.add_cart(items)
customer.print_cart()

#check out
finalBill = customer.checkout(store)

print("final bill =", finalBill)

#view store inventory after customer purchase
store.print_inventory()
