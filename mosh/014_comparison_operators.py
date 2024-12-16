temperature = 35
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

# > greater than
# < less than
# == equals

name = "Vanya"
lenght = len(name)

if lenght < 3:
    print("Name must be at least 3 characters")
elif lenght > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good ;)")


if 3 <= lenght <= 50:
    print("Name looks good ;)")
else:
    print("Invalid name")


weight = float(input(f"Please enter your weight: "))
metric_system = input(f"Choose is it (L)bs or (K)g: ").lower()
if metric_system == "l":
    print(f"You are {weight * 0.45} kilograms")
elif metric_system == "k":
    print(f"You are {weight / 0.45} pounds")
else:
    print("Oops o o")
