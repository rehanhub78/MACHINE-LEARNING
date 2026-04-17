'''
 Take a year and print the corresponding century (e.g., “19th century”, “20th century”)
'''
while True:
    try:
        year = int(input("Enter year: "))
        if year <=0:
            print("Invalid! Please Enter correct year: ")
            continue

        century = (year-1) // 100+1
        print(f"the corresponding century is the {century}th century.")

    except ValueError:
        print("Invalid input! Please enter numeric digit.")
