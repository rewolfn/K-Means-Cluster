#Centroid class, purpose is to work its way to the center of data point clusters
import math

class Centroid:
    
    def __init__(self, location):
        self.__location = location #Tuple (R, G, B)
        self.__observations = []
        self.__label = None # Meant for setting qualitative label for human use, in this case it'll be the name of a color
    
    def length(self): # just returns number of observations
        return len(self.__observations)
    
    def getObservations(self):
        return self.__observations
    
    def remove(self, observation):
        self.__observations.remove(observation)
        
    def add(self, observation):
        self.__observations.append(observation)
        
    def location(self):
        return self.__location
    
    def update(self): # Find the average (R,G,B) values of all data points and set location to new average
        temp = [0] * len(self.__location)
        for i in range(len(temp)):
            value = 0
            for j in range(len(self.__observations)):
                observation = self.__observations[j]
                location = observation.location()
                value += location[i]
            temp[i] = value / len(self.__observations)
        self.__location = tuple(temp)
    
    def distance(self, location): # Returns Euclidean distance between observation and self
        raw = 0
        for i in range(len(location)): # Written as a loop in case I wanted to reuse this code with in a larger vector space
            temp = self.__location[i] - location[i]
            raw += temp * temp
        return math.sqrt(raw) # returns sqrt(n1^2 + n2^2 +...+ nm^2)
    
    def setLabel(self, label):
        self.__label = label

    def label(self):
        return self.__label
