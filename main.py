print ("This is Your health management system \n Maintain your health with us")
def current_time(): #current_time()
   #function to record time
   import time
   local=time.asctime(time.localtime(time.time()))
   return (local)
import time
initial_time =time.time()
i=0
while i<=10:
    time.sleep(1800)
    # to play mp3
    from pygame import mixer
    mixer.init()
    mixer.music.load("drinkw.mp3")
    mixer.music.set_volume(0.7)
    c = mixer.music.play()
    activity_time = current_time()
    print(f"{activity_time} water drinking  time")
    with open("water.txt", "a") as c1:
        c1.write("\n")
        c1.write(activity_time)
        c1.write(" ")
        c1.write("drunk 250 ml of water ")
        # to play mp3
    time.sleep(180)
    from pygame import mixer
    mixer.init()
    mixer.music.load("eyesexe.mp3")
    mixer.music.set_volume(0.7)
    c = mixer.music.play()
    activity_time = current_time()
    print(f"{activity_time}eye exe time ")
    with open("eyesexercise.txt", "a") as c1:
        c1.write("\n")
        c1.write(activity_time)
        c1.write(" ")
        c1.write("done eye exercise")
        # to play mp3
    time.sleep(420)
    from pygame import mixer
    mixer.init()
    mixer.music.load("phyact.mp3")
    mixer.music.set_volume(0.7)
    c = mixer.music.play()
    activity_time = current_time()
    print(f"{activity_time}phtime")
    with open("phactivity.txt", "a") as p1:
       p1.write("\n")
       p1.write(activity_time)
       p1.write(" ")
       p1.write(" phact done")
    i = i + 1


