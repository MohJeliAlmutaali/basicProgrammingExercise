run = True
while run:
    try:
        score = int(input("Score: "))
    except ValueError:
        print("input must be a number")
        run = True
    else:
        run = False
        if 90 <= score <= 100:
            print("A: With Compliments")
        elif 80 <= score <= 89:
            print("B: Very satisfy")
        elif 70 <= score <= 79:
            print("C: Satisfying")
        elif 60 <= score <= 69:
            print("D: Not satisfactory")
        elif 0 <= score <= 59:
            print("E: Not pass")
        else:
            print("Input score between 0-100 !")
