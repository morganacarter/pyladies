for beer in range(99,1,-1):
    print "{0} bottles of beer on the wall, {0} bottles of beer...\n If one of those bottles should happen to fall,{1} bottles of beer on the wall".format(beer,beer-1)




# Can you make Python print out the song for 99 bottles of beer on the wall?

# Note: You can use range() in three different ways

# First:
# range(5) will give you a list containing [0, 1, 2, 3, 4]
# In this case, range assumes you want to start counting at 0, and the parameter you give is the number to stop *just* short of.

# Second:
# range(5, 10) will give you a list containing [5, 6, 7, 8, 9]
# In this case, the two parameters you give to range() are the number to start at and the number to stop *just* short of.
# Helpful mnemonic: range(start, stop)

# Third:
# range(5, 15, 3) will give you a list containing [5, 8, 11, 14]
# In this case, the three parameters you give to range() are the number to start at, the number to stop *just* short of, and the number to increment each time by.
# Note that normally, the number to increment each time by is assumed to be 1.  (In other words, you add 1 each time through.)
# That's why it goes [0, 1, 2, 3, 4] unless you specify that third parameter, called the step.
# Helpful mnemonic: range(start, stop, step)

# Using range() and a loop, print out the song.  Your output should look like this:

# 99 bottles of beer on the wall, 99 bottles of beer ...
# If one of those bottles should happen to fall, 98 bottles of beer on the wall
# 98 bottles of beer on the wall, 98 bottles of beer ...
# If one of those bottles should happen to fall, 97 bottles of beer on the wall
# 97 bottles of beer on the wall, 97 bottles of beer ...
# If one of those bottles should happen to fall, 96 bottles of beer on the wall
# 96 bottles of beer on the wall, 96 bottles of beer ...
#.
#.
#.
#.
# 4 bottles of beer on the wall, 4 bottles of beer ...
# If one of those bottles should happen to fall, 3 bottles of beer on the wall
# 3 bottles of beer on the wall, 3 bottles of beer ...
# If one of those bottles should happen to fall, 2 bottles of beer on the wall
# 2 bottles of beer on the wall, 2 bottles of beer ...
# If one of those bottles should happen to fall, 1 bottles of beer on the wall
