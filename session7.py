import os

def menu():
    print("""
1. Calculate the Area of triangle
2. Calculate the Area of rectangle
3. Determine odd and even numbers
4. Exit
""")

def triangle():
    
    print("Calculate the Area of triangle")
    base = float(input("Base    : "))
    height = float(input("Height  : "))
    the_area = 0.5 * base * height
    print(f"The Area of Triangle : {the_area}")
    print("\n\n")
    

def rectangle():
    
    print("Calculate the Area of rectangle")
    length = float(input("Length    : "))
    width = float((input("Width     : ")))
    the_area = length * width
    print(f"The Area of rectangle is : {the_area}")
    print("\n\n")

def odd_and_even():
    print("odd and even")
    number = float((input("Number  : ")))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is Odd")

    print("\n\n")

def main():
    while True:
        menu()
        choose = input("choose the number: ")
        if choose == "1":
            os.system('cls')
            triangle()
        elif choose == "2":
            os.system('cls')
            rectangle()
        elif choose == "3":
            os.system('cls')
            odd_and_even()
        elif choose == "4":
            print("thank for using the app ")
            break
        else:
            os.system('cls')
            print("invalid input")
    

if __name__=="__main__":
    main()