from Centroid import *
from Observation import *
import random



class KMeansCluster:

    def __init__(self, dimensions, observations = []):
        self.__dimensions = dimensions # set number of dimensions in vector space
        self.__observations = observations # Just in case we already have observations made/saved
        self.__centroids = [] # List of all centroids. len(self.__centroids) == number of clusters we expect

    def addObservation(self, location): #location is a tuple
        self.__observations.append(Observation(location))


    def removeObservation(self, location):
        for i in range(len(self.__observations)):
            if self.__observations[i].location() == location:
                self.__observations.remove(self.__observations[i])
                break


    def learn(self, groups):
        done = False # we just started so the AI has stuff to learn
        self.__createCentroids(groups) # initialize all our centroids
        self.__randomAssign() # give all observations away randomly
        while not done: # while the AI still needs to learn...
            self.__update() # move to the weighted geometric center of all observations
            done = self.__calculate() # move observations based on new centroid locations
            self.__checkLonely() # Reassign observations to a centroid if it accidentally lost all of its observations
        return self.__centroidLocations() # these are the weighted geometric centers of the clusters

    def createLabels(self, labels):
        for i in range(len(labels)):
            self.__centroids[i].setLabel(labels[i])

    def guess(self, location): # iterate through all centroids, find the one closest to the location given
        print("")
        guess = self.__centroids[0].label()
        distance = self.__centroids[0].distance(location)
        for centroid in self.__centroids:
            if centroid.distance(location) < distance:
                guess = centroid.label()
                distance = centroid.distance(location)
        return guess


    def __createCentroids(self, groups):
        for i in range(groups): # create centroid for each expected group
            temp = [0] * self.__dimensions
            for j in range(len(temp)):
                temp[j] = random.random() # move centroid to a random starting location
            self.__centroids.append(Centroid(temp))

    def __randomAssign(self): # random assignment of observations to begin with
        for i in range(len(self.__observations)):
            self.__centroids[random.randint(0 ,len(self.__centroids)-1)].add(self.__observations[i])
        self.__checkLonely()

    def __checkLonely(self): # can't have a centroid with no data points
        for j in range(len(self.__centroids)):
            if len(self.__centroids[j].getObservations()) == 0: # find lonely centroid
                for k in range(len(self.__centroids)):
                    test_observations = self.__centroids[k].getObservations()
                    if len(test_observations) > 1: # can't take an observation from a centroid who has none
                        observation = test_observations[random.randint(0, len(test_observations) - 1)] # take random observation from greedy centroid and give it to the lonely one. Sharing is caring!
                        self.__centroids[k].remove(observation)
                        self.__centroids[j].add(observation)
                        break

    def __update(self):
        for i in range(len(self.__centroids)):
            self.__centroids[i].update()

    def __calculate(self): # moving observations to closest centroids
        done = True # set flag
        for centroid in self.__centroids:
            observations = centroid.getObservations()
            for observation in observations:
                location = observation.location()
                closest = centroid
                distance = centroid.distance(location)
                for k in self.__centroids: # check distance to each centroid
                    if k.distance(location) < distance:
                        closest = k
                if closest != centroid: # move observation if currently assigned centroid isn't the closest one
                    centroid.remove(observation)
                    closest.add(observation)
                    done = False

        return done # if done == False, an observation moved which means the AI hasn't finished learning

    def __centroidLocations(self):
        temp = []
        for centroid in self.__centroids:
            temp.append(centroid.location())
        return temp
