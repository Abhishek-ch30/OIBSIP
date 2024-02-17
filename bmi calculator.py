#function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

#function to interpret BMI into weight categories
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

#get user input for weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

#calculate BMI using the provided weight and height
bmi_result = calculate_bmi(weight, height)

#print the calculated BMI and its interpretation
print(f"Your BMI is: {bmi_result:.2f}")
print(f"You are categorized as: {interpret_bmi(bmi_result)}")
