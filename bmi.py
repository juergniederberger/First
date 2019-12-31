def math(m,kg):
    bmi = kg/m**2
    return bmi

m = float(input("What is your size in meters? "))
kg = float(input("What is your weight in kg? "))
print("Dein BMI ist ", end = '')
print(round(math(m, kg),1))
