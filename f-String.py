letter="My  name is {1} and I am from {0}"
country="India"
name="Dinesh"
print(letter.format(country,name))
#Using f-String
print(f"My  name is {name} and I am from {country}")
print(f"My  name is {{name}} and I am from {{country}}")
price=49.999999
print(f"For only {price: .2f} dollars!")
print(f"{2*33}")
print(type(f"{2*33}"))