products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products[0][1])

for product in products:
	print(product[0], '的價格是', product[1])

# 清單列表 最常使用csv檔 通常會使用","做區隔
with open('product.csv', 'w') as f:
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')