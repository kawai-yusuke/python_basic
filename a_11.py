height = float(input("Height(m)? > "))
weight = float(input("Weight(kg)? > "))

bmi = round(weight / (height * height), 2)

print(f"Your BMI is {bmi}")

# 例
# $ python bmi.py
# Height(m)? > 170
# Weight(kg)? > 60
# Your BMI is 20.76
# BMI＝体重(kg) ÷ {身長(m) Ｘ 身長(m)}
