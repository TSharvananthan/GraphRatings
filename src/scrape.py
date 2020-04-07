from bs4 import BeautifulSoup
from requests import get
from imdb import IMDb
from urllib.request import urlretrieve

def ScrapeRatings(search_term):
    #PART 1: SAERCHING THE WORD
    object = IMDb()
    searchresults = object.search_movie(search_term)
    print("Showing the first 15 results. Choose one movie (type a corresponding number)")
    for x in range(0, 15):
        print("{} - {} - {} | {}".format(x + 1, str(searchresults[x]).lower().title(), searchresults[x].data["kind"].lower().title(), searchresults[x].data["year"]))

    number = int(input())

    id = searchresults[number].getID()

    #PART 2: GETTING THE MOVIE
    movie = object.get_movie(id)

    #PART 3: GETTING THE ICON TO INCLUDE IN THE FINAL IMAGE
    urlretrieve(movie.get_fullsizeURL(), "images/main/icon.jpg")

    #PART 4: UPDATING TO ONLY INCLUDE THE EPISODES OF THE SHOW
    object.update(movie, "episodes")

    #PART 5: GETTING ALL THE EPISODES, SEPERATED BY SEASON
    total = movie["episodes"]

    #PART 5: GETTING SEASONS AND EPISODE VALUES (AS X/Y VALUES TO PLOT)
    seasons = sorted(list(movie["episodes"].keys()))
    episodes = [len(total[y]) for y in seasons]

    #PART 6: COLLECTING RATINGS
    data = []

    for x in range(1, len(seasons) + 1):
        season = []
        for y in range(1, len(total[x]) + 1):
            season.append(round(total[x][y].data["rating"], 3))
        data.append(season)

    return (data, seasons, episodes)
