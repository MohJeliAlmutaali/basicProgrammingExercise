import os, platform, colorama
from colorama import Fore

products = []            

def addProduct():
    clearDisplay()
    print("""
 _______     __     __      ______                __              __   
|   _   |.--|  |.--|  |    |   __ \.----.-----.--|  |.--.--.----.|  |_ 
|       ||  _  ||  _  |    |    __/|   _|  _  |  _  ||  |  |  __||   _|
|___|___||_____||_____|    |___|   |__| |_____|_____||_____|____||____|
                                                                       
-----------------------------------------------------------------------
""")
    global product
    product = {}
    product["name"] = input("Product Name   : ")
    product["price"] = int(input("Product Price  : "))
    product["stock"] = int(input("Order Quantity : "))
    product["cost"] = product['price'] * product['stock']
    
    product['percent'] = int(input("Percent        : "))
    product["profit"] = product["price"] * product['percent']/100
    product["selling_price"] = product['price'] + product['profit']
    
    products.append(product)

def purchaseProduct():
    global product
    showProduct()
    
    # global run
    i = 0
    run = True
    while run:
        choose = input("Choose The Number: ")
        if int(choose) <= len(products) > 0:
            order = int(input("Order Quantity: "))
            break
            # isContinue = input("Purchase Again? y/n: ")
            # if isContinue.lower() == 'y':
            #     run = True
            # if isContinue.lower() == 'n':
            #     run = False
        else:
            i += 1
            print("Invalid Input")
            if i == 3:
                break
                 
             
    for i, product in enumerate(products):    
        if int(choose)-1 == i:  
            product["item_sold"] = order  
            total_cost = product['selling_price'] * order 
            product['income'] = product['item_sold'] * product['selling_price']
            product['total_profit'] = product['income'] - product['cost']
            clearDisplay()
            print("""
  _   _   _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( T | r | a | n | s | a | c | t | i | o | n )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
""")
            print(f"Product Name  : {product['name']}")
            print(f"Quantity      : {order}")
            print(f"Total Cost    : {total_cost}")
            print("-"*40) 
            print(f"Percent       : {product['percent']}%")
            print(f"Selling Price : {product['selling_price']}")
            print(f"Income        : {product['income']}")
            print(f"Total Profit  : {product['total_profit']}\n\n\n\n\n")
            
            
            product['stock'] = product['stock'] - order
        
       

def extract(key,list):
    for i in list:
        return i[key]

def menu():
    print("""
1. Show Product
2. Add Product
3. Purchase Product
4. Exit
""")
    
def showProduct():
    os.system("clear")
    print('-'*50)
    # print(f"{'Product': > 10} {'Price': > 10} {'Stock'}")
    print(f'{" No".ljust(6)}{"Product".ljust(19)} {"Price".ljust(17)} Stock')
    print('-'*50)
    
    for i,product in enumerate(products):
        i +=1
        print(f" {str(i).ljust(6)}{str(product['name'].ljust(19))}{(str(product['selling_price']).ljust(18))}{product['stock']}")
    print('\n')
    print('-'*50)
    print("\n" * 4)
    
def title():
    print(Fore.LIGHTYELLOW_EX + """
███╗   ███╗ ██████╗ ██╗  ██╗            ██╗███████╗██╗     ██╗
████╗ ████║██╔═══██╗██║  ██║            ██║██╔════╝██║     ██║
██╔████╔██║██║   ██║███████║            ██║█████╗  ██║     ██║
██║╚██╔╝██║██║   ██║██╔══██║       ██   ██║██╔══╝  ██║     ██║
██║ ╚═╝ ██║╚██████╔╝██║  ██║██╗    ╚█████╔╝███████╗███████╗██║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚════╝ ╚══════╝╚══════╝╚═╝

""")
    
def clearDisplay():
    if platform.system() == "Linux":
        os.system('clear')
    if platform.system() == "Windows":
        os.system('cls')
    
    
def main():
    run = True
    while run:
        menu()
        choose = input("Enter Number: ")
        if choose == "1":
            showProduct()
            
        elif choose == "2":
            addProduct()
        elif choose == "3":
            purchaseProduct()
        elif choose == "4":
            print("Thank for using the app")
            break
        else:
            print("Invalid Input")  
              
            
if __name__ == "__main__":
    clearDisplay()
    title()
    main()       
        
    
