# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

bread=15
peanut_butter=6
jelly=9

if bread>=2 and peanut_butter>=1 and jelly>=1:
    print "I can make a peanut butter and jelly sandwich!!"
else:
        print "No lunch for me today"


# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

bread=15
peanut_butter=6
jelly=9
min_sandwiches=[peanut_butter, jelly, bread/2]

if bread>=2 and peanut_butter>=1 and jelly>=1:
    print "I can make", min(min_sandwiches),"peanut butter and jelly sandwiches!!"
else:
        print "No lunch for me today"

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )


bread=15
peanut_butter=6
jelly=9
min_sandwiches=[peanut_butter, jelly, bread/2]

if bread>=2 and bread%2=="1" and peanut_butter>=1 and jelly>=1:
   print "I can make", min(min_sandwiches),"peanut butter and jelly sandwiches!!"
elif bread>=2 and peanut_butter>=1 and jelly>=1:
   print "I can make", min(min_sandwiches),"peanut butter and jelly sandwiches and", bread%2 ,"open faced sandwiches"
else:
    print "No lunch for me today"


# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

bread=15
peanut_butter=0
jelly=6
min_sandwiches=[peanut_butter, jelly, bread/2]

if bread==0:
    print "You need more bread"
elif peanut_butter==0:
    print "You need more peanut butter"
elif jelly==0:
    print "You need more jelly"
elif bread>=2 and bread/2==0 and peanut_butter>=1 and jelly>=1:
    print "I can make", min(min_sandwiches),"peanut butter and jelly sandwiches!!"
elif bread>=2 and peanut_butter>=1 and jelly>=1:
    print "I can make", min(min_sandwiches),"peanut butter and jelly sandwiches and", bread/2 ,"open faced sandwiches"
else:
    print "No lunch for me today"

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

bread=15
peanut_butter=14
jelly=0
min_sandwiches=[peanut_butter, jelly, bread/2]

if bread==0:
    print "You need more bread"
elif peanut_butter==0:
    print "You need more peanut butter"
elif jelly==0 and bread>=2 and peanut_butter>=1:
    print "You can make a peanut butter sandwich....I guess. But please, go to Safeway on your way home."
elif bread>=2 and bread%2==0 and peanut_butter>=1 and jelly>=1:
    print "I can make", min(min_sandwiches),"peanut butter and jelly sandwiches!!"
elif bread>=2 and peanut_butter>=1 and jelly>=1:
    print "I can make", min(min_sandwiches),"peanut butter and jelly sandwiches and", bread%2 ,"open faced sandwiches"
else:
    print "No lunch for me today"
