# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original list:", justice_league)

# 1. Count members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to front:", justice_league)

# 4. Place someone between Aquaman and Flash
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")  # or "Green Lantern"
print("After separating Aquaman & Flash:", justice_league)

# 5. Replace entire team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

# 6. Sort alphabetically and find new leader
justice_league.sort()
print("Sorted team:", justice_league)
print("New leader (0th index):", justice_league[0])
