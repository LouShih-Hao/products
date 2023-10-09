import os # operating system

# refactor 重構

def read_file(filename):
    products = []
    # 讀取檔案
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 跳過這一迴，繼續下一迴
            products.append(line.strip().split(','))
    print(products)
    return products

def user_input(products):
    # 讓使用者輸入
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        products.append([name, price])
    # print(products[0][1])
    return products

def print_products(products):
    # 印出所有購買紀錄
    for product in products:
        print(product[0], '的價格是', product[1])

def write_file(filename, products):
    # 寫入檔案
    # 清單列表 最常使用csv檔 通常會使用","做區隔
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for product in products:
            f.write(product[0] + ',' + product[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()