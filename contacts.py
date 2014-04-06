# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

#contacts = {
#    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
#}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner 

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

for contact in contacts.keys():
    print "{0}'s contact information is:\n Phone:{1}\n Twitter: {2}\n Github: {3}".format(contact,contacts[contact]["phone"],contacts[contact]["twitter"],contacts[contact]["github"])



# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

html_table="""
 <table border="1">
 <tr>
 <td colspan="2"> {0} </td>
 </tr>
 <tr>
 <td> Phone: {1} </td>
 <td> Twitter: {2} </td>
 <td> Github: {3} </td>
 </tr>
 </table>
"""
for contact in contacts.keys():
    print html_table.format(contact,contacts[contact]["phone"],contacts[contact]["twitter"],contacts[contact]["github"])




# ...

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}}

html_table = """
 <table border="1">
 <tr>
 <td colspan="2"> {0} </td>
 </tr>
 <tr>
 <td> Phone: {1} </td>
 <td> Twitter: {2} </td>
 <td> Github: {3} </td>
 </tr>
 </table>
"""
        
with open('contact_html.html', 'w') as contact_list:
    for contact in contacts.keys():
        contact_list.write(html_table.format(contact,contacts[contact]["phone"],contacts[contact]["twitter"],contacts[contact]["github"]))

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).



html_table = """
 <table border="1">
 <tr>
 <td colspan="2"> {0} </td>
 </tr>
 <tr>
 <td> Phone: {1} </td>
 <td> Twitter: {2} </td>
 <td> Github: {3} </td>
 </tr>
 </table>
"""

with open("contacts.csv", "r") as raw_contact_file:
    contacts_list = raw_contact_file.read().split("\n")
    for contact in contacts_list:
       individual_contact = contact.split(",")
       key=individual_contact[0]
       contact_info=individual_contact[1:]
       contactsdict={key:contact_info for contact in contacts_list}
       print contactsdict
       

#Note: Still working on figuring out how to write this to html. Info below not 100% accurate.
#with open('contact_html_2.html', 'w') as contact_list_html:
#   for contact in contactsdict.keys():
#        contact_list_html.write(html_table.format(key,contactsdict[contact_info]["phone"],contactsdict[contact_info]["twitter"],contactsdict[contact_info]["github"]))
