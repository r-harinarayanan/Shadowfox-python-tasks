# Task 5.2 – Jumping Jack Tracker
completed = 0

while completed < 100:
    print(f"Do 10 jumping jacks! Total done: {completed}")
    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            completed += 10
    elif tired in ["no", "n"]:
        completed += 10
    else:
        print("Please enter yes or no.")

if completed == 100:
    print("🎉 Congratulations! You completed the workout!")
