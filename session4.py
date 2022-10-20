import platform, os

platform = platform.system()
def program_title():
    print("""
Author : Moh.Jeli Almutaali || TI221
#######################################
#######################################
######     Welcome To Program    ######
#######################################
#######################################
   -----------+++====+++------------
""")

def thank():
    print("\nThank for using the program...\n")

def clear_display():
    if platform == "Linux":
        os.system("clear")
    if platform == "Windows":
        os.system("cls")

def sum_list(var_list,t_list):
    total  = sum(var_list)
    t_list.append(total)
    
clear_display()
program_title()

prd_name, prd_price, ordr_quantity, buy_price = [],[],[],[]
prcnt, prft, sllng_price, itm_sld, ttl_prft, ttl_income = [],[],[],[],[],[]

t_income, t_profit = [],[]

def main():
    run = True
    while run:
        # nama produk
        product_name = input("Produk name: ").title()
        prd_name.append(product_name)
        # harga produk
        product_price = float(input("Prices: "))
        prd_price.append(product_price)
        # banyak barang yang diorder
        order_quantity = int(input("Order Quantity: "))
        ordr_quantity.append(order_quantity)

        # harga beli = harga produk * jumlah order
        buying_price = product_price * order_quantity
        buy_price.append(buying_price)

        # keuntungan
        percent = input("Percent: ").split("%")
        
            
        prcnt.append(percent)
        
        
        profit = (product_price * float(percent[0])/100 )
        prft.append(profit)

        # harga jual = harga produk + profit
        selling_price = product_price + profit
        sllng_price.append(selling_price)
        # barang yang terjual
        item_sold = int(input("Item sold: "))
        itm_sld.append(item_sold)
        # total pendapatan
        income = item_sold * selling_price
        ttl_income.append(income)
        # total keuntungan
        total_profit = income - buying_price
        ttl_prft.append(total_profit)
        # Menginput lagi
        enter_again = input("\nEnter Again, y/n: ").lower()
        if enter_again == "y":
            run = True
        elif enter_again == "n":
            run = False
        else:
            print("Invalid input")
            
    clear_display()

    sum_list(ttl_income,t_income)
    sum_list(ttl_prft, t_profit)

    print("="*45)
    print(f"Product Name   : {prd_name}\nPrice          : {prd_price}\nOrder Quantity : {ordr_quantity}\n\
Buying price   : {buy_price} \nPercent        : ",end='')
    if len(prcnt)> 1: 
        for i in range(0, len(prcnt[0])):
            print(prcnt[i][0],"%", end=", ")
    else:
        print(prcnt[0][0],"%")
    print(f"\nMargin Profit  : {prft}\nSelling Price  : {sllng_price}\n\
Item sold      : {itm_sld}\nIncome         : {ttl_income}\nTotal Income   : {t_income[0]}\nProfit         : {ttl_prft}\nTotal Profit   : {t_profit[0]}")
    
    tanda = 45
    if len(prd_name) >= 4:
        tanda += 35
    print('='* tanda)
    
if __name__ =="__main__":
    main()
    thank()
