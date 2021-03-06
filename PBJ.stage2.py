# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

bread=5
peanut_butter=15
jelly=15
start_sandwich=1

while bread>=2 and peanut_butter>=1 and jelly>=1:
    print "Making sandwich {0}".format(start_sandwich)
    bread=bread-2
    peanut_butter=peanut_butter-1
    jelly=jelly-1
    start_sandwich=start_sandwich+1

    if bread<2 or peanut_butter<1 or jelly<1:
        print "All done, only had enough for {0} sandwiches".format(start_sandwich-1)


# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

bread=5
peanut_butter=15
jelly=15
ingrediants=[peanut_butter,jelly,bread]
start_sandwich=1

while bread>=2 and peanut_butter>=1 and jelly>=1:
    print "Making sandwich {0}. \n I have enough bread for {1} more sandwiches, enough peanut butter for {2} more, and enough jelly for {3} more".format(start_sandwich,bread/2,jelly,peanut_butter)
    bread=bread-2
    peanut_butter=peanut_butter-1
    jelly=jelly-1
    start_sandwich=start_sandwich+1

    if bread<2 or peanut_butter<1 or jelly<1:
        print "All done, only had enough for {0} sandwiches".format(start_sandwich-1)
