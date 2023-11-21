#To determine if a string has a specific character in it, we
#have a lot of (if not infinite) possibilities

first_str = "Bonjour"
second_str = "Bonjoure"

first_str, second_str = first_str.lower(), second_str.lower()

#First, with the keyword "in":
if "e" in first_str:
    print("e in first_str")
else:
    print("e NOT in first_str")

if "e" in second_str:
    print("e in first_str")
else:
    print("e NOT in first_str")

#We could also check manually each character one by one with a for loop
for i in first_str:
    if i == "e":
        print("e in first_str")

for i in second_str:
    if i == "e":
        print("e in second_str")