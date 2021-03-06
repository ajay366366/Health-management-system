print ("This is Your health management system \n Maintain your health with us")
def current_time(): #current_time()
   """function to record time"""
   import time
   local=time.asctime(time.localtime(time.time()))
   return (local)
def mp3(): #mp3()
   """to play mp3"""
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
            break

