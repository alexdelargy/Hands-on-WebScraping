from matplotlib import pyplot as plt
from datetime import time
import csv
gameSentiment = []
with open("sentiment.csv", newline="") as sentimentFile:
    reader = csv.DictReader(sentimentFile, dialect='excel')
    for row in reader:
        time24 = lambda x: x if int(row["time"].split(':')[0]) <= 12 else int(row["time"].split(':')[0]) + 12
        gameSentiment.append((float(row["sentiment"]), time(hour=time24, minute=row['time'].split(':')[1])))

plt.plot([x[1] for x in gameSentiment], x[0] for x in gameSentiment)
plt.show()

