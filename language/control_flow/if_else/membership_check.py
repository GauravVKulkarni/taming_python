list1 = ["Apple", "Banana", "Orange"]
list2 = ["Sparrow", "Hummingbird", "Pelican"]
list3 = ["Platipus", "Anteater", "Iguana"]

random_thing = "Koala"

if random_thing in list1:
    print("Its a fruit.")

elif random_thing in list2:
    print("Its a bird.")

elif random_thing in list3:
    print("Its a bizarre animal.")

else:
    print("What the heck is it?")