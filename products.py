#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8')as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',') #strip是拿掉\n 遇到,分割
		products.append([name, price])
print(products)

#讓使用者輸入
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

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是：', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8')as f: # w寫入模式,f當作前面的檔案 # with自動close檔案
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')