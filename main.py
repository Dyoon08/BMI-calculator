n = input("what is your name?")
w = int(input("what is your weight in ponds?"))
h = int(input("what is your height?"))
BMI = (w * 703) / (h * h)

if BMI < 18.5:
    print( " you are underweight!")
elif BMI  < 24.9:
    print( "you are normal!")
elif BMI < 29.9:
    print ("you are overweight!")
elif BMI >30:
    print("you are obese ")



