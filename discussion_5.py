import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for char in sentence:
		if char == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

		

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = 0
		max_item = Item("item", 0, 0)
		for item in self.items:
			if item.stock > max_stock: 
				max_stock = item.stock
				max_item = item
				
		return max_item

	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = 0
		max_item = Item("item", 0, 0)
		for item in self.items:
			if item.price > max_price: 
				max_price = item.price
				max_item = item

		return max_item



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("hey"), 0) 
		self.assertEqual(count_a("apple"), 1) 
		self.assertEqual(count_a("apart"), 2) 

		


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		items = []
		w = Warehouse(items)
		w.add_item(self.item1)
		self.assertEqual(w.items[-1], self.item1)
		w.add_item(self.item2)
		self.assertEqual(w.items[-1], self.item2)


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		items = [self.item1, self.item2, self.item3]
		w = Warehouse(items)
		self.assertEqual(w.get_max_stock(), self.item3)



	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		items = [self.item1, self.item2, self.item3]
		w = Warehouse(items)
		self.assertEqual(w.get_max_price(), self.item1)
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()