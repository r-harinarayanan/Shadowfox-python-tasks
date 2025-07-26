import random

# Roll dice 20 times
dice_rolls = []
count_6 = 0
count_1 = 0
consecutive_6 = 0

for i in range(20):
    roll = random.randint(1, 6)
    dice_rolls.append(roll)
    
    if roll == 6:
        count_6 += 1
        # Check previous roll
        if i > 0 and dice_rolls[i - 1] == 6:
            consecutive_6 += 1
    elif roll == 1:
        count_1 += 1

# Print results
print("All dice rolls:", dice_rolls)
print("Number of times 6 appeared:", count_6)
print("Number of times 1 appeared:", count_1)
print("Number of times 6 appeared twice in a row:", consecutive_6)
