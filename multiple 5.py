try:
    a = int(input("insert any number: " ))
    x = a % 5==  0
    if x: 
        print ( "yes, it is multiple of 5")
    else:
        print ( " it is not a multiple of five ")
except:
    print("Invalid input.")