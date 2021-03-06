import numpy as np
import time
from apscheduler.scheduler import Scheduler
import urllib.request

from pymongo import MongoClient

CONST_TIME = 2
CONST_TREESHOLD = 80
CONST_BUZZ = "http://10.100.3.48/on/3"
MONGO_CONNECTION = "mongodb://10.100.1.22:27017"
MONGO_DATABASE = "angularfullstack"
COLLECTION = "mood"
COLLECTION_VECTOR = "mood_vector"


class Subject:
    def __init__(self):
        self.gender = 0
        self.mood = []
        self.scheduler = None
        self.name = "(no collaborator)"
        self.url = CONST_BUZZ

    def evaluate(self):
        current = int(time.time())

        timeView = list(filter(lambda element: current -
                               CONST_TIME <= element[0], self.mood))
        happyView = list(
            filter(lambda element: element[1] == "happy", timeView))

        if(len(timeView) == 0):
            self.unload()
        elif len(happyView)/len(timeView)*100 < CONST_TREESHOLD:
            self.unload()

    def unload(self):
        urllib.request.urlopen(self.url).read()

    def start(self):
        self.scheduler = Scheduler()
        self.scheduler.start()
        self.scheduler.add_interval_job(self.evaluate, seconds=CONST_TIME)

    def stop(self):
        self.scheduler.shutdown()

    def add(self, labels, mood, gender):
        labeledMoods = np.array(list(zip(labels, mood[0])))
        timestamp = int(time.time())

        self.gender = gender

        post = {
            "collaborator": self.name,
            "gender": gender,
            "timestamp": timestamp
        }

        for labeledMood in labeledMoods:
            post[labeledMood[0]] = labeledMood[1]

        #mongo = MongoClient(MONGO_CONNECTION)
        #database = mongo[MONGO_DATABASE]

        # database[COLLECTION_VECTOR].insert_one(post)

    def persist(self, mood, gender, timestamp):
        #mongo = MongoClient(MONGO_CONNECTION)
        #database = mongo[MONGO_DATABASE]

        post = {"collaborator": self.name,
                "mood": mood,
                "gender": gender,
                "timestamp": timestamp}

        # database[COLLECTION].insert_one(post)

    def addMood(self, mood, gender):
        timestamp = int(time.time())

        self.gender = gender
        self.mood.append((timestamp, mood, 1))

        self.persist(mood, gender, timestamp)
