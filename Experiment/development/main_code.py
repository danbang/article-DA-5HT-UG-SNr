#before experiment Main code
import random

txt_size = 0.07
title_size = 0.1
image_Yloc = [-0.50,-0.2]
image_Ploc = [0.50,-0.2]

#no control offer debug version
noControl = [3,2,3]
random.shuffle(noControl)

#offer list
nc_first = [5]
nc_offer = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9]
random.shuffle(nc_offer)
noControl = nc_first + nc_offer
print("offer", noControl, len(noControl))

#mood sample list
mood_set = [[0,1],[0,1],[0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
print("preset", mood_set, len(mood_set))
random.shuffle(mood_set)
print("shuffle", mood_set)
mood = [item for l in mood_set for item in l]
print("flat", mood, len(mood))

#trigger key listen
#kb = keyboard.Keyboard()
trigger_list = []

#condition folder directory
conditionfolder = ''

jitter = []
for i in range(0,30):
    n = random.uniform(1.5,2.5)
    n = round(n,1)
    jitter.append(n)

print(jitter)
#button code, 4
#3 green
#4 red
#1 blue
#2 yellow
# button code, 2
#3 green
#4 red 