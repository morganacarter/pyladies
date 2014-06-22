import requests
response = requests.get("http://bechdeltest.com/api/v1/getMoviesByTitle?title=matrix").json()
print response
#print response
for movie in response:
    print movie['title'],movie['rating']
    #for title in movie_database:
import requests
title_endpoint = raw_input("what movie do you want to see?")
if title_endpoint[0:4] == 'The ':
    title_endpoint = title_endpoint[4:]
if title_endpoint == []:
    print "Sorry not found"
if len(title_endpoint) == 7 and title_endpoint.isdigit() == True:
    raw_response = "http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid={0}".format(title_endpoint)
else:
    raw_response = "http://bechdeltest.com/api/v1/getMoviesByTitle?title={0}".format(title_endpoint).replace(" ","+")
response = requests.get(raw_response).json()
print response

#import requests
# Goal 3:
# Integrate this with the Open Movie Database API: http://www.omdbapi.com/
# Display all of the details from both APIs when searching for a movie.
# Note that you may need to prefix your ImdbIDs with 'tt' to get the search to work.

import requests
title_endpoint = raw_input("what movie do you want to see?")
if title_endpoint[0:4] == 'The ':
    title_endpoint = title_endpoint[4:]
if title_endpoint == []:
    print "Sorry not found"
if len(title_endpoint) == 7 and title_endpoint.isdigit() == True:
    raw_response = "http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid={0}".format(title_endpoint)
else:
    raw_response = "http://bechdeltest.com/api/v1/getMoviesByTitle?title={0}".format(title_endpoint).replace(" ","+")
response = requests.get(raw_response).json()
print response


if len(title_endpoint) == 7 and title_endpoint.isdigit() == True:
    raw_response2 = "http://www.omdbapi.com/?i=tt{0}&t=".format(title_endpoint)
else:
    raw_response2 ="http://www.omdbapi.com/?i&t={0}".format(title_endpoint).replace(" ","+")
response2 = requests.get(raw_response2).json()
print response2
