products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	products.append([name, price]) 	
	#p = [name, price]
	#p.append(name)
	#p.append(price)
print(products)