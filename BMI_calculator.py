print('This program calculates the BMI index of a person')

name = input("What's your good name")
height, weight = eval(input('Enter your height(m) and weight(kg)'))

def bmi_calc(height, weight):
    bmi = weight / height **2
    return bmi

bmi_index = bmi_calc(height, weight)

if 19 < bmi_index <25:
    print("\n{} is healthy having an bmi index {}".format(name, bmi_index))

else:
    print("\n{} is not healthy having the bmi index {}".format(name, bmi_index))
