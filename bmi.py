def math(size, weight):
    size = float(size.replace(",", ".").strip())
    weight = float(weight.replace(".", ".").strip())
    bmi = weight / size ** 2
    return bmi


size = input("What is your size in meters? ")
weight = input("What is your weight in kg? ")
print("Your BMI is ", end='')
print(round(math(size, weight), 1))
