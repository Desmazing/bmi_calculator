# This is a BMI calculator
# major considerations: mass and height units + all inputs are strings. Negative values
# prompt inputs, calculates the BMI and returns bmi. Returns a message on health status
# final output narrowed down for age 20+ adults.


import math


def bmiCalculator():
    name = input("What is your name? ")
    print(f'Hello {name}. Select your preferred units.\n')
    selected_unit = input("1 for metric, 2 for imperial: ")

    if selected_unit == "1":
        print_bmi(metricCompute())
    elif selected_unit == "2":
        print_bmi(imperialCompute())
    else:
        print("Invalid input. Try again:\n")
        bmiCalculator()


def metricCompute():
    try:
        mheight = abs(float(input("\nHow tall are you in meters?\n")))
        mmass = abs(float(input("Enter your mass in kilograms:\n")))
        
        if 0.65<mheight<2.72 and 0<mmass<635:
            bmi = mmass / (math.pow(mheight, 2))
            return bmi
        else:
            metricCompute()
    except ValueError:
        print("Ensure your input is a number!")
        metricCompute()
        
 
def imperialCompute():
    iheight = abs(float(input("\nHow tall are you in feet?\n")))
    imass = abs(float(input("Enter your mass in pounds:\n")))

    mheight = (iheight * 30.48) / 100
    mmass = imass / 2.2

    if 0.65<mheight<2.72 and mmass<635:
        bmi = mmass / (math.pow(mheight, 2))
        return bmi
    else:
        imperialCompute()

def print_bmi(x):
    print("Your BMI is {}".format(x))
    if x < 18.5:
        print(f"Dear {name}, you could be underweight.")
    elif 18.5<=x<=24.9:
        print(f"Dear {name}, you are of normal weight.")
    elif 25<=x<=29.9:
        print(f"Dear {name}, you are overweight.")
    else:
        print(f"Dear {name}, you are not healthy.")
    

bmiCalculator()
