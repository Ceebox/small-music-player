import os; from playsound import playsound; import random; import time

songs = os.listdir("./songs")

while True:
    song = "./songs/" + songs[random.randint(0, len(songs))]
    print("Now playing " + song)
    playsound(song)
    time.sleep(1)
