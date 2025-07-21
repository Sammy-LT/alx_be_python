"""
age = int(input("Enter your age: "))

if age >= 18:
  print("You are eligible to vote.")
else:
  print("You are not eligible to vote yet.")


  purchase_amount= float(input("Enter the purchase amount: "))
  if purchase_amount >= 100.98:
    discount= 0.1 # 10% discount
  elif purchase_amount >= 50.50:
    discount = 0.05
  else: discount=0

  final_price= purchase_amount*(1-discount)
  print("Final price after discount is: $", final_price)

  adj= input("Enter an adjective: ")
  noun= input("Enter a noun: ")
  print(f"The {adj} {noun} jumped over the fence.")


"""
students= "hello world"
for student in students:
    print(student)
    