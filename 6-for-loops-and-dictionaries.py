#For loops and dictionaries

#suspicious people detector

suspects = ["John Doe", "Coolkid", "1x1x1x1", "Jason"] #suspects
suspects_detected = 0 #suspects detected counter

people = [{"Name": "John Doe", "Location": "Roblox HQ"}, #all people registered
          {"Name": "Elliot", "Location": "Robloxia's Pizzeria"},
          {"Name": "Coolkid", "Location": "Robloxia's Pizzeria"},
          {"Name": "Dusekkar", "Location": "SFOT"},
          {"Name": "1x1x1x1", "Location": "SFOT"},
          {"Name": "Guest1337", "Location": "Park of Robloxia"},
          {"Name": "Builderman", "Location": "Roblox HQ"}
          ]

for person in people: #this makes the program check every person in people
    if person["Name"] in suspects: #this makes so if the program checks a person and their name is in the suspects lists, it executes the code below
        print(f"suspect {person['Name']} detected in {person['Location']}") #this prints the name and the location of the person and then the program warn us that they're suspect
        suspects_detected += 1 #this adds 1 to the suspects counter because we found one
    else:
        print(f"{person['Name']} found in {person['Location']}") #if the person isn't a suspect then it prints their name and their location, but it doesn't warn us

print(f"Total suspects: {suspects_detected}") #this takes the amount of suspects we found and prints it