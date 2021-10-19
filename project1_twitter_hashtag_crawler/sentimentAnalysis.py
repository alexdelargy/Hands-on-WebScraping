import numpy as np
import csv
from datetime import datetime

sentimentFile = open("sentiment.txt", "r")
current = sentimentFile.readline()
while current:
    current = sentimentFile.readline()   

sentiment = float(current)
sentimentFile.close()

with open("mydata.csv", newline="") as file:
    reader = csv.DictReader(file, dialect="excel")
    for row in reader:
        tweet_text = row["tweet_text"]
        tweet_time = row["tweet_time"]
        tweet_likes = row["number_of_likes"]
        tweet_retweets = row["no_of_retweets"]


with open("sentiment.txt", "a") as sentimentFile:
    sentimentFile.append(str(sentiment) + "\n")
    



