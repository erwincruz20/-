# Get height and weight from user
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Calculate body mass index (BMI)
bmi = weight / height**2

# Determine weight category based on BMI
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

# Print result
print("Your BMI is:", bmi)
print("Your weight category is:", category)
