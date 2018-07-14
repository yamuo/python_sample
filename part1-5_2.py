songs = {
    "1": "fun",
    "2": "blue",
    "3": "me",
    "4": "floor",
    "5": "live"
    }


n = input("please input a number:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("not found")
