#testing 1
"""print ("This is Your health management system \n Maintain your health with us")
def current_time(): #current_time()
   #function to record time
   import time
   local=time.asctime(time.localtime(time.time()))
   return (local)
def mp3(): #mp3()
   #to play mp3
   from pygame import mixer
   mixer.init()
   mixer.music.load("tinny.mp3")
   mixer.music.set_volume(0.7)
   c=mixer.music.play()
   return(c)
import time
initial_time =time.time()
i=0
while True :
    final_time=time.time()
    time_diff= int(final_time-initial_time)
    if time_diff==2 :
       #mp3()
       activity_time = current_time()
       print(f"{activity_time}wamp3")
       with open("water.txt", "a") as c1:
          c1.write("\n")
          c1.write(activity_time)
          c1.write(" ")
          c1.write("drunk250 ml")
          i = i + 1
       #mp3()
       activity_time = current_time()
       print(f"{activity_time}eyemp3")
       with open("eyesexercise.txt", "a") as c1:
           c1.write("\n")
           c1.write(activity_time)
           c1.write(" ")
           c1.write("done eye exercise")
           i = i + 1
       initial_time = final_time
       continue
    elif time_diff==3 :
        #mp3()
        activity_time = current_time()
        print(f"{activity_time}phmp3")
        with open("phactivity.txt", "a") as p1:
           p1.write("\n")
           p1.write(activity_time)
           p1.write(" ")
           p1.write("done")
           i = i + 1
        initial_time=final_time
        continue

    else:
        if i<=15:
            continue
        else:
            break"""

#Testing 2
"""print ("This is Your health management system \n Maintain your health with us")
def current_time(): #current_time()
   #function to record time
   import time
   local=time.asctime(time.localtime(time.time()))
   return (local)
def mp3(): #mp3()
   #to play mp3
   from pygame import mixer
   mixer.init()
   mixer.music.load("tinny.mp3")
   mixer.music.set_volume(0.7)
   c=mixer.music.play()
   return(c)
import time
initial_time =time.time()
i=0
while i<=8:
    time.sleep(2)
    mp3()
    activity_time = current_time()
    print(f"{activity_time}wamp3")
    with open("water.txt", "a") as c1:
        c1.write("\n")
        c1.write(activity_time)
        c1.write(" ")
        c1.write("drunk250 ml")
    #mp3()
    activity_time = current_time()
    print(f"{activity_time}eyemp3")
    with open("eyesexercise.txt", "a") as c1:
        c1.write("\n")
        c1.write(activity_time)
        c1.write(" ")
        c1.write("done eye exercise")
    #mp3()
    time.sleep(1)
    activity_time = current_time()
    print(f"{activity_time}phmp3")
    with open("phactivity.txt", "a") as p1:
       p1.write("\n")
       p1.write(activity_time)
       p1.write(" ")
       p1.write("done")
       i = i + 1
"""
"""def mp3(): #mp3()
   #to play mp3
   from pygame import mixer
   mixer.init()
   mixer.music.load("tinny.mp3")
   mixer.music.set_volume(0.7)
   c=mixer.music.play()
   return(c)"""


#testing code with if else
"""print ("This is Your health management system \n Maintain your health with us")
def current_time(): #current_time()
   #function to record time
   import time
   local=time.asctime(time.localtime(time.time()))
   return (local)
def mp3(): #mp3()
   #to play mp3
   from pygame import mixer
   mixer.init()
   mixer.music.load("tinny.mp3")
   mixer.music.set_volume(0.7)
   c=mixer.music.play()
   return(c)
import time
initial_time =time.time()
i=0
while True :
    final_time=time.time()
    time_diff= int(final_time-initial_time)
    if time_diff==9 :
        mp3()
        activity_time = current_time()
        with open("phactivity.txt", "a") as p1:
           p1.write("\n")
           p1.write(activity_time)
           p1.write(" ")
           p1.write(input(f"Your exercise time lazy boy {i}"))
           i = i + 1
        initial_time=final_time
        continue
    elif time_diff==17 :
       mp3()
       activity_time = current_time()
       with open("water.txt", "a") as c1:
          c1.write("\n")
          c1.write(activity_time)
          c1.write(" ")
          c1.write(input(f" time to Drink 500ml  "))
          i = i + 1
       initial_time = final_time
    elif time_diff==29:
        mp3()
        activity_time = current_time()
        with open("eyesexercise.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write(input(f"Time for eyes exercise {i} "))
            i = i + 1
        initial_time = final_time
        continue
    else:
        if i<=15:
            continue
        else:
            break"""

#testing4 code with cotinuity
"""print ("This is Your health management system \n Maintain your health with us")
def current_time(): #current_time()
   #function to record time
   import time
   local=time.asctime(time.localtime(time.time()))
   return (local)
import time
initial_time =time.time()
i=0
while i<=2:
    time.sleep(5)
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
    time.sleep(10)
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
    time.sleep(15)
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
"""
#testing5 # solved problem of time collapse (on main )
"""print ("This is Your health management system \n Maintain your health with us")
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
while j<4:
    if i==1: #for 1 and 2 task
        time.sleep(25)
        # to play mp3
        from pygame import mixer
        mixer.init()
        mixer.music.load("drinkw.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time} water drinking  time")
        with open("water.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("drunk 250 ml of water ")
        time.sleep(5)
        from pygame import mixer
        mixer.init()
        mixer.music.load("eyesexe.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
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
        mixer.music.load("phyact.mp3")
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
        time.sleep(10)
        # to play mp3
        from pygame import mixer
        mixer.init()
        mixer.music.load("drinkw.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time} water drinking  time")
        with open("water.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("drunk 250 ml of water ")
        time.sleep(5)
        from pygame import mixer
        mixer.init()
        mixer.music.load("eyesexe.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
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
        mixer.music.load("drinkw.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time} water drinking  time")
        with open("water.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("drunk 250 ml of water ")
        time.sleep(5)
        from pygame import mixer
        mixer.init()
        mixer.music.load("eyesexe.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        activity_time = current_time()
        print(f"{activity_time}eye exe time ")
        with open("eyesexercise.txt", "a") as c1:
            c1.write("\n")
            c1.write(activity_time)
            c1.write(" ")
            c1.write("done eye exercise")
        time.sleep(5)
        from pygame import mixer
        mixer.init()
        mixer.music.load("phyact.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
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
"""
#testing6 "Solved problem of audio collapse occurs  due to diff tasks at  same time  (on main )"
"""print ("This is Your health management system \n Maintain your health with us")
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
while j<4:
    if i==1: #for 1 and 2 task
        time.sleep(1800)
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
        time.sleep(900)
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
        time.sleep(900)
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
        time.sleep(1800)
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
"""


