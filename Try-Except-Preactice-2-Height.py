while True:
    try:
        height = float(input("Enter your height in meters:"))
        break
    except ValueError:
        print("Please enter a valid height in meters e.g. 1.65")
