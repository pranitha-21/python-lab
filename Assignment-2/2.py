product={}

while True:
    name=input("Enter product name(enter q to quit):")
    if name=='q':
        break
    value=float(input("Enter product value:"))
    product[name]=value

print("Enter products:")
while True:
    product_name=input("Product name:")
    if product_name=='done':
        break
    if product_name in product.keys():
        print(f"price:{product[product_name]}")
    else:
        print("Product is not in dictionary")

