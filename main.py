from src.validateimports import validateImports
from src.scrape import ScrapeRatings
from src.graph import Graph

import argparse

argObject = argparse.ArgumentParser()
argObject.add_argument("id", type=str, help="What movie are you trying to find?")
argObject.add_argument("--filepath", type=str, default="output.png", help="Where would you like to save the figure")

argParsed = argObject.parse_args()

validateImports()

data = ScrapeRatings(argParsed.id)

RATINGS = data[0]
X_VALUES, Y_VALUES = data[1], data[2]

Graph(X_VALUES, Y_VALUES, argParsed.filepath)
