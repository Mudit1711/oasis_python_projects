#BMI CALCULATOR 
wellcome = print("WELLCOME TO BMI CALCULATOR ".center(100))
name = input(" Enter you good name : ")
calculation = print(" Enter you height and weight for BMI")

feet = int(input (" Enter your height in (feet ) :"))
inches = int(input (" Enter your height in ( inches) :"))
height1 = (feet*12 + inches) * 2.54
weight_input = input("Enter your weight (e.g., 70kg or 154lb): ")

# Determine the unit of weight and convert to kg if needed
if 'lb' in weight_input.lower():
    weight = float(weight_input.lower().replace('lb', '').strip()) / 2.2046226
elif 'kg' in weight_input.lower():
    weight = float(weight_input.lower().replace('kg', '').strip())
else:
    weight = float(weight_input)
height1 = height1/100

BMI = weight/ height1 **2
print(f' {name} your BMI is {BMI:.2f}')
if BMI >0:
    if BMI <= 16:
        print(f' {name} you are slverely under weight ')
    elif BMI <= 18.5:
        print(f' {name} you are under weight ')
    elif BMI <= 25:
        print(f' {name} you are in good health state ')
    elif BMI <= 30:
        print(f' {name} you are over weight ')
    elif BMI <= 35:
        print(f' {name} you are in obese class 1') 
    elif BMI <= 40:
        print(f' {name} you are in obese class 2 ')
    else:
        print(f' {name} you are in obese clas 3 ')
else:
    print(" worng data ")
print(f' {name} thanku for visit and take a step toward your health '.center(50))
        
        
        

