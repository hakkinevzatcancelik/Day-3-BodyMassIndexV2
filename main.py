height = float(input("Boyunuzu girin:"))

weight = float(input("Kilonuzu girin:"))

bmi = (weight/height**2)
if bmi < 18.5:
  print(f"BMI değeriniz {bmi}, biraz zayıfsınız.")
elif bmi < 25:
  print(f"BMI değeriniz  {bmi}, normal kilodasınız.")
elif bmi < 30:
  print(f"BMI değeriniz  {bmi}, biraz kilolusunuz.")
elif bmi < 35:
  print(f"BMI değeriniz  {bmi}, obezsiniz.")
else:
    print(f"BMI değeriniz  {bmi}, klinikal obezsiniz.")





