from src.scrape import ScrapeRatings
from src.graph import Graph
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

import argparse

argObject = argparse.ArgumentParser()
argObject.add_argument("id", type=str, help="What movie are you trying to find?")
argObject.add_argument("--filepath", type=str, default="output.png", help="Where would you like to save the figure")

argParsed = argObject.parse_args()

data = ScrapeRatings(argParsed.id)

RATINGS = data[0]
X_VALUES, Y_VALUES = data[1], data[2]
COORDINATES = data[3]
MOVIE_NAME = data[4]

Graph(X_VALUES, Y_VALUES, argParsed.filepath, RATINGS, COORDINATES, MOVIE_NAME)
