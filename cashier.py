def main():
	receipt = []
	total = .0
	item = input("Item (enter \"done\" when finished): ")
	while item.lower() != "done":
		choice = {}
		price = input("Price: ")
		quantity = input("quantity: ")
		choice = {
			'name' : item,
			'price' : price,
			'quantity' : quantity
			}
		receipt.append(choice)
		item = input("Item (enter \"done\" when finished): ")
	for i in receipt:
		price = int(i['quantity']) * float(i['price'])
		print('%s' % i['quantity'],i['name'],price)
		total += price
	print("Total Price: %fKD" % total)

if __name__ == '__main__':
	main()