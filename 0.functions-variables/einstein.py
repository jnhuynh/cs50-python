# E = mc^2

# Get mass
mass = input('Enter a mass (int): ')

# Format input
# More precise value
# speed_of_light = 299792458
speed_of_light = 300000000
energy = int(mass) * (speed_of_light**2)

# Print formatted input
print(f"Energy: {energy}")
