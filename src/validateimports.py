def validateImports():
    try:
        from bs4 import BeautifulSoup
        from requests import get
        from imdb import IMDb
        import numpy
        import matplotlib.pyplot as plt
        import pandas as pd
        import argparse
    except:
        from os import system
        print("Installing required libraries...")
        system("pip3 install bs4 requests numpy imdbpy matplotlib pandas argparse")
