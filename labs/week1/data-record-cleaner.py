raw_name = "  Alice Johnson  "
raw_age = "29"
raw_temperature = "98.6"
raw_is_member = "True"
raw_balance = "1500.75"

#Cleaning & Casting Part
name = raw_name.strip()
age = int(raw_age)
temperature = float(raw_temperature)
is_member = raw_is_member == "True"
balance = float(raw_balance)

#Printing Part
print(f"Name: {name}, {type(name)}")
print(f"Age: {age}, {type(age)}")
print(f"Temperature: {temperature}, {type(temperature)}")
print(f"Member: {is_member}, {type(is_member)}")
print(f"Balance: {balance}, {type(balance)}")
