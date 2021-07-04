import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8')as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',') #strip是拿掉\n 遇到,分割
			products.append([name, price])
	return products


#讓使用者輸入
def user_input(products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是：', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8')as f: # w寫入模式,f當作前面的檔案 # with自動close檔案
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('找到檔案了!')
		products = read_file(filename) #return存回products
	else:
		print('找不到檔案...')


	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

#refactor 重構


