name = input("Enter Your Name: ")
print("Hello", name)
mood = input("How are you feeling: ").strip().lower()
if mood == "good":
    print("That's great!")
elif mood == "not good":
    print("What happened??")
else:
    print("I see. Hope things get better!")
