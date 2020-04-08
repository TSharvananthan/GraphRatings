def validateImports():
    try:
        import matplotlib
        import numpy
        import bs4
        import requests
        import imdb
        import pandas
        import argparse
    except:
        from os import system
        print("Installing required libraries...")
        system("pip3 install bs4 requests numpy imdbpy matplotlib pandas argparse")
