justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("1. Number of members:", len(justice_league))
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("2. After adding Batgirl & Nightwing:", justice_league)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("3. Wonder Woman as leader:", justice_league)
justice_league.remove("Superman")  
index_flash = justice_league.index("Flash")
index_aquaman = justice_league.index("Aquaman")
if index_aquaman < index_flash:
    justice_league.insert(index_flash, "Superman")
else:
    justice_league.insert(index_aquaman + 1, "Superman")

print("4. After resolving conflict between Aquaman & Flash:", justice_league)
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("5. New team assembled by Superman:", justice_league)

justice_league.sort()
print("6. Sorted team:", justice_league)
print("New leader is:", justice_league[0])
