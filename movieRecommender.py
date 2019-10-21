# Python3 code for movie recommendation based on emotion

# bs4 for web scraping
from bs4 import BeautifulSoup as SOUP

# regular expressions for string matching
import re

# requests for making GET request to IMDb API
import requests as HTTP

# Function for scraping and processing
def scrapAndProcess(emotion):

    # URL to which GET request will be made
    url = ""

    # IMDb URL for Drama genre of movie against emotion Sad
    if(emotion == "sad"):
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    # IMDb URL for Musical genre of movie against emotion Disgust
    elif(emotion == "disgust"):
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

    # IMDb URL for Family genre of movie against emotion Anger
    elif(emotion == "anger"):
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

    # IMDb URL for Thriller genre of movie against emotion Anticipation
    elif(emotion == "anticipation"):
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    # IMDb URL for Sport genre of movie against emotion Fear
    elif(emotion == "fear"):
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

    # IMDb URL for Thriller genre of movie against emotion Enjoyment
    elif(emotion == "enjoyment"):
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    # IMDb URL for Western genre of movie against emotion Trust
    elif(emotion == "trust"):
        url = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

    # IMDb URL for Film_noir genre of movie against emotion Surprise
    elif(emotion == "surprise"):
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    # List to store all movie names
    movies = []

    # Try catch block to prevent abrupt termination of code if IMDb server is down
    try:
        # If entered emotion is not from one of the above, return empty movies list
        if not url:
            return movies

        # HTTP request to get the data of the whole page
        response = HTTP.get(url)

        # Accessing the text property of the response object
        data = response.text

        # Parsing the data using BeautifulSoup
        soup = SOUP(data, "lxml")

        # Pruning noisy data - the elements in this list can appear as movie names
        flags = ["None", "X", "\n"]

        # Extract movie titles from the data using regex
        for movieName in soup.findAll('a', attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}):

            # Converting from bs4.element.NavigableString to python3 string
            movieName = str(movieName.string)

            # Checking if movie name is not in noisy data list
            if movieName not in flags:
                movies.append(movieName)

    # Catch exceptions - they might occur if the IMDb server is down
    except Exception as e:
        print(e)

    return movies

# Driver function
if __name__ == '__main__':

    # Converting input string to lower case
    emotion = input("Enter the emotion: ").lower()

    # Calling the scraping function
    movies = scrapAndProcess(emotion)

    # If entered emotion is not from one of the available emotions
    if not movies:
        print("Please enter from one of the available emotions")

    # Print top 10 movies in ascending order
    for count, movie in enumerate(movies):
        if count == 10:
            break
        print(movie)
