

# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py
#I used the .csv version of this!

with open("statesv2.csv", "r") as states_file:
    states = states_file.read().split("\n")

print "<select>"

for index, state in enumerate(states):
    states[index] = states[index].split(",")
    print "\t <option value='{0}'>{1}</option>".format(states[index][0], states[index][1])
print "</select>"


# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.


with open('statesv2.csv', 'r') as states_file:
    states = states_file.read().split("\n")
    for index, state in enumerate(states):
        states[index] = state.split(",")

with open('states_pop.html', 'w') as population_file:
    population_file.write("<select_name=\state\>\n")
    for index, info in enumerate(states):
        population_file.write("<option value='{0}'>{1}</option>".format(states[index][0],states[index][1]))
    population_file.write("</select>")


# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>


with open('state_info.csv', 'r') as states_file:
    states = states_file.read().split("\n")
    for index, state in enumerate(states[1:]): ##Adding the [1:] removes the header boxes
        states[index] = state.split(",")

html_table="""
<table border="1">
<tr>
<td colspan="2"> {0} </td>
 </tr>
 <tr>
 <td> Rank: {1} </td>
 <td> Percent: {2}% </td>
 </tr>
 <tr>
 <td> US House Members: {3} </td>
 <td> Population: {4} </td>
 </tr>
 </table>
"""

with open('states_info_full.html', 'w') as population_file:
    population_file.write("<select_name=\state\>\n")
    for index, info in enumerate(states[1:]): ##Adding the [1:] removes the header boxes
        population_file.write(html_table.format(states[index][0],states[index][1],states[index][4],states[index][3],states[index][2]))
    population_file.write("</select>")
        


# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.

## I don't have a full answer for this one, sorry. I know very little about HTML/Javascript.
## But maybe YOU can help? Feel free to fork this.
## Achievement 1: I produced a real, live working dropdown menu!
## Problem 1: But instead of listing each state, it lists "Wyoming" 53 times. 
## Problem 2: It also does not take you to any state. So basically, it doesn't really address challenge #4. Baby steps.
## I will keep trying at this. If I make progress, I will update and comment accordingly.


with open('state_info.csv', 'r') as states_file:
    states = states_file.read().split("\n")
    for index, state in enumerate(states[1:]): ##Adding the [1:] removes the header boxes
        states[index] = state.split(",")


html_table="""
<table border="1">
<tr>
<td colspan="2"> {0} </td>
 </tr>
 <tr>
 <td> Rank: {1} </td>
 <td> Percent: {2} </td>
 </tr>
 <tr>
 <td> US House Members: {3} </td>
 <td> Population: {4} </td>
 </tr>
 </table>
"""

with open('states_info_full.html', 'w') as population_file:
    population_file.write("<select>")
    for names in zip(states):
        population_file.write("\t<option value='{0}'>{0}</option>".format(state.split(",")[1]))
    population_file.write("</select>")
    for index, info in enumerate(states[1:]):
       population_file.write(html_table.format(states[index][0],states[index][1],states[index][4],states[index][3],states[index][2]))
    population_file.write("</select>")


