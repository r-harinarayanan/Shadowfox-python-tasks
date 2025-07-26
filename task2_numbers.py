# 1. Format number using format()
value = 145
formatted = format(value, 'o')  # 'o' stands for octal
print("Formatted value (Octal) of 145:", formatted)

# 2. Pond area & water volume
radius = 84
pi = 3.14
area = pi * radius * radius
print("Area of the pond is:", int(area), "sq. meters")

# Water calculation
water_per_sq_meter = 1.4  # in liters
total_water = area * water_per_sq_meter
print("Total water in the pond (rounded):", int(total_water), "liters")

# 3. Speed calculation
distance = 490  # in meters
time_in_minutes = 7
time_in_seconds = time_in_minutes * 60
speed = distance / time_in_seconds
print("Speed is:", int(speed), "meters/second")
