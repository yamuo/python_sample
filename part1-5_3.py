lists = []

rap = ["eminem","kanie","jayz","naz"]
rock = ["bob","beatles","red"]
djs = ["seds","tiest"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

#print(lists)

#print(rap)

#town = (20.4,20.5)
#print(town)

bands = {
    "jazz":"yellow jackets",
    "rock":"screaming",
    "classic":"bach"
    }

n = input("please input genre of music:")

if n in bands:
    print(bands[n])
else:
    print("Whant's?")
