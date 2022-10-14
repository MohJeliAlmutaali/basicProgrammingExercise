product_name = input("Produk name: ").title()
product_price = float(input("Prices: "))
order_quantity = int(input("Order Quantity: "))
buying_price = product_price * order_quantity

percent = input("Percent: ").split("%")
profit = (product_price * float(percent[0])/100 )

selling_price = product_price + profit
item_sold = int(input("Item sold: "))

income = item_sold * selling_price
total_profit = income - buying_price

print("="*60)

print(f"Product Name: {product_name}\nPrice: {product_price}\nOrder Quantity: {order_quantity}\n\
Buying price: {buying_price}\nPercent: {percent[0]}%\nProfit: {profit}\nSelling Price: {selling_price}\n\
Item sold: {item_sold}\nIncome: {income}\nTotal Profit: {total_profit}")