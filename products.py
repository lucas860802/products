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

for p in products:
	print(p[0], '的價格是：', p[1])

# with自動close檔案
with open('products.csv', 'w', encoding='utf-8')as f: # w寫入模式,f當作前面的檔案
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')