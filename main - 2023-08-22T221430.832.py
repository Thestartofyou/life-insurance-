def calculate_life_insurance_premium(age, height, weight):
    base_premium = 100  # Base premium amount
    
    # Additional premium based on age
    if age < 30:
        age_factor = 0.8
    elif age < 50:
        age_factor = 1.0
    else:
        age_factor = 1.2
    
    # Additional premium based on height and weight
    bmi = weight / ((height / 100) ** 2)  # Calculate BMI
    if bmi < 18.5:
        bmi_factor = 1.1
    elif bmi < 24.9:
        bmi_factor = 1.0
    else:
        bmi_factor = 1.2
    
    # Calculate total premium
    total_premium = base_premium * age_factor * bmi_factor
    return total_premium

# Example usage
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

premium = calculate_life_insurance_premium(age, height, weight)
print(f"Your life insurance premium is: ${premium:.2f}")
