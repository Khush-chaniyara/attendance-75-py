import sys
total_lec=int(input("enter total number of lectures:"))
attended_lec=int(input("enter attended lectures:"))
attended_per=(attended_lec/total_lec)*100
if attended_lec>total_lec:
   print("you entered more attended lec then total lec")
   sys.exit()
print(f"your total attendance is :{attended_per}")
if attended_per>75:
    x=0
    while ((attended_lec/(total_lec+x))*100)>75:
        x+=1
    print(f"you can bunk {x-1} lectures for 75% attendance")
elif attended_per<75:
    x=0
    while (((attended_lec+x)/(total_lec+x))*100)<75:
        x+=1
    print(f"you have to attend {x} lectures for 75% attendance")