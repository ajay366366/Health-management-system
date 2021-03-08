#this program will remind you for 12 hours for different  health exercises and drinking water
# currently program set to just 90 seonds cycle
print ("This is Your health management system \n Maintain your health with us")
def current_time(): #current_time()
   #function to record time
   import time
   local=time.asctime(time.localtime(time.time()))
   return (local)
import time
initial_time =time.time()
a=0
i=1
j=1
print (f"Your day routine started at {current_time()}")
while j<4:
    if i==1: #for 1 and 2 task
        time.sleep(30)
        # to play mp3
        from pygame import mixer
        mixer.init()
        mixer.music.load("waeye.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time} water drinking  time")
        with open("water.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("drunk 250 ml of water ")
        activity_time = current_time()
        print(f"{activity_time}eye exe time ")
        with open("eyesexercise.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("done eye exercise")
    elif i==2: # for task 3 only after 15 minutes (45)
        time.sleep(15)
        from pygame import mixer
        mixer.init()
        mixer.music.load("ph.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time}phtime")
        with open("phactivity.txt", "a") as p1:
            p1.write("\n")
            p1.write(activity_time)
            p1.write(" ")
            p1.write("ph act done")
    elif i==3:  # for 1 and 2 task
        time.sleep(15)
        # to play mp3
        from pygame import mixer
        mixer.init()
        mixer.music.load("waeye.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time} water drinking  time")
        with open("water.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("drunk 250 ml of water ")
        activity_time = current_time()
        print(f"{activity_time}eye exe time ")
        with open("eyesexercise.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("done eye exercise")
    elif i == 4: # for task 1,2,3 at the same time
        time.sleep(30)
        # to play mp3
        from pygame import mixer
        mixer.init()
        mixer.music.load("waeyeph.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time} water drinking  time")
        with open("water.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("drunk 250 ml of water ")
        activity_time = current_time()
        print(f"{activity_time}eye exe time ")
        with open("eyesexercise.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("done eye exercise")
        activity_time = current_time()
        print(f"{activity_time}phtime")
        with open("phactivity.txt", "a") as p1:
            p1.write("\n")
            p1.write(activity_time)
            p1.write(" ")
            p1.write("ph act done")
    else:
        i=1
        j=j+1
        continue
    i=i+1
print ("Good nignt!!! you did great job today ")
