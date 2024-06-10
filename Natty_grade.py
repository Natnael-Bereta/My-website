try:
    subject_name = input("Insert subject name: ")

    score = float(input("Insert your result out of 100: "))

    Help = "You can only insert numbers from 0 to 100"
    x = 2

    if 90 <= score <= 100 :
        print("A+ Excellent.")
    elif 83 <= score < 90:
        print("A ")
    elif 80 <= score < 83:
        print("A- ")
    elif 75 <= score < 80:
        print("B+ Very good!")
    elif  68 <= score < 75:
        print("B")
    elif 65 <= score < 68:
        print("B- Good")
    elif 60 <= score < 65:
        print("C+" )
    elif 50 <= score < 60:
        print("C Satisfactory!")
    elif 45 <= score < 50:
        print("C- Unsatisfactory!")
    elif 40 <= score < 45:
        print("D very poor")
    elif 30 <= score < 40:
        print("Fx Fail")
    elif score < 30 :
        print("Dedeb nek tmrt lante ayidelem!") # No offense just joking
    else :
        print(f'Invalid input.' + Help)
except:
    print(f'Invalid input. You can only insert numbers!')