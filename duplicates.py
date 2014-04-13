# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
# File 1: People who attended your Film Screening event
# https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
# File 2: People who attended your Happy hour
# https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

def textfile_to_string(filename):
    with open(filename,"r") as text_file:
        text_file = text_file.read().split("\n")
    return text_file
hhattendees = textfile_to_string("happy_hour_attendees.txt")

def textfile_to_string1(filename):
        with open(filename,"r") as text_file:
            text_file = text_file.read().split("\n")
        return text_file
filmattendees = textfile_to_string1("film_screening_attendees.txt")

def remove_duplicates(fromlist):
    fromlist = list(set(fromlist))
    return fromlist
allattendees = remove_duplicates(filmattendees + hhattendees)
print allattendees

# Goal 2: Who came to *both* your Film Screening and your Happy hour?

def only_duplicates(fromlist):
    fromlist = list(set(fromlist))
    return fromlist
double_attendees = set(filmattendees) & set(hhattendees)
print list(double_attendees)


###This is another way to get the same thing:
#def textfile_to_string(filename):
#    with open(filename,"r") as text_file:
#        text_file = text_file.read().split("\n")
#    return text_file
#hhattendees = textfile_to_string("happy_hour_attendees.txt")

#def textfile_to_string1(filename):
#        with open(filename,"r") as text_file:
#            text_file = text_file.read().split("\n")
#        return text_file
#filmattendees = textfile_to_string1("film_screening_attendees.txt")

##For a depulicated list:
#allattendees = list(set(filmattendees + hhattendees))
#print allattendees

##For attendees who went to both events:
#double_attendees = set(filmattendees) & set(hhattendees)
#print list(double_attendees)
