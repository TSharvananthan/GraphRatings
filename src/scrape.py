from bs4 import BeautifulSoup
from requests import get
from imdb import IMDb
from urllib.request import urlretrieve
from itertools import chain

def ScrapeRatings(id):
    object = IMDb()

    #PART 1: GETTING THE MOVIE
    movie = object.get_movie(id)

    #PART 2: GETTING THE ICON TO INCLUDE IN THE FINAL IMAGE
    urlretrieve(movie.get_fullsizeURL(), "icon.jpg")

    #PART 3: UPDATING TO ONLY INCLUDE THE EPISODES OF THE SHOW
    object.update(movie, "episodes")

    #PART 4: GETTING ALL THE EPISODES, SEPERATED BY SEASON
    total = movie["episodes"]

    #PART 5: GETTING SEASONS AND EPISODE VALUES (AS X/Y VALUES TO PLOT)
    total_episode_number = list(chain.from_iterable([[(y, x) for x in range(1, len(total[y]) + 1)] for y in sorted(list(total.keys()))]))

    seasons = [x[0] for x in total_episode_number]
    episodes = [y[1] for y in total_episode_number]

    #PART 6: COLLECTING RATINGS
    ratings = []

    for se in total.keys():
        for ep in total[se].keys():
            ratings.append(round(total[se][ep].data["rating"], 3))
    return (ratings, seasons, episodes)
